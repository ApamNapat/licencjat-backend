from datetime import datetime, timezone, timedelta

from django.contrib.auth.models import User

from IIdle.actions import ACTION_TO_CLASS, Class
from IIdle.consts import HOURS_IN_DAY
from IIdle.models import Timetable


def process_timetable(user: User) -> None:
    timetable_to_process = Timetable.objects.filter(user=user, time__lte=datetime.now(tz=timezone.utc))
    for entry in timetable_to_process:
        processor = ACTION_TO_CLASS[entry.action]
        processor.process(user)
        entry.delete()


def validate_and_process_timetable_change(user: User, data: list) -> (bool, str):
    current_hour = datetime.now(tz=timezone.utc).replace(minute=59, second=59, microsecond=1000000 - 1)
    valid_hours = {hour % HOURS_IN_DAY for hour in range(current_hour.hour, current_hour.hour + 12)}
    actions_and_times = []
    for action in data:
        action_hour = int(action['hour'])
        action_name = action['action']
        if action_hour not in valid_hours:
            return False, f'Invalid timetable. Chosen time: {action_hour} is too far into the future'
        action_class = ACTION_TO_CLASS[action_name]
        if action_class.time is not None and action_hour not in action_class.time:
            return False, f'Invalid timetable. Chosen action: {action_name} cannot be performed at {action_hour}'
        if issubclass(action_class, Class) and action_class.semester % 2 != user.data.semester % 2:
            return False, "Invalid timetable. You can't take summer classes in the winter and vice versa"
        next_day_offset = timedelta(days=1 if action_hour < current_hour.hour else 0)
        time_to_fill = current_hour.replace(hour=action_hour) + next_day_offset
        actions_and_times.append({'action': action_name, 'time': time_to_fill})
    times = [action_with_time['time'] for action_with_time in actions_and_times]
    if len(set(times)) != len(times):
        return False, 'Invalid timetable. Each hour can only appear once'
    for i in actions_and_times:
        Timetable.objects.filter(time=i['time']).delete()
        Timetable.objects.create(user=user, **i)
    return True, 'Timetable successfully saved'


def list_valid_actions(user: User) -> list:
    now = datetime.now(tz=timezone.utc)
    current_hour = now.hour
    valid_hours = [hour % HOURS_IN_DAY for hour in range(current_hour, current_hour + 12)]
    return [
        {'hour': hour,
         'actions': [
             action.name
             for action in ACTION_TO_CLASS.values()
             if ((action.time is None or hour in action.time)
                 and (not issubclass(action, Class) or action.semester % 2 == user.data.semester % 2))
         ]}
        for hour in valid_hours
    ]
