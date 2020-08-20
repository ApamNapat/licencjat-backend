from datetime import datetime, timezone, timedelta

from django.contrib.auth.models import User
from django.test import TestCase

from IIdle.consts import HOURS_IN_DAY
from IIdle.models import UserData, Timetable, Abilities, ACTIONS_CHOICES
from IIdle.timetable_processor import process_timetable, validate_and_process_timetable_change, list_valid_actions


class UserDataAndSemesterEndAdded(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')
        delta = timedelta(microseconds=1)
        for action in ACTIONS_CHOICES:
            if action != 'Finish Semester':
                Timetable.objects.create(user=self.user, time=datetime.now(tz=timezone.utc) - delta, action=action)
        for x in range(30):  # Let's hope this doesn't happen IRL
            Timetable.objects.create(user=self.user, time=datetime.now(tz=timezone.utc) - delta, action='Logic')
            Timetable.objects.create(user=self.user, time=datetime.now(tz=timezone.utc) - delta, action='Calculus I')
            Timetable.objects.create(user=self.user, time=datetime.now(tz=timezone.utc) - delta,
                                     action='Introduction To Computer Science')
            Timetable.objects.create(user=self.user, time=datetime.now(tz=timezone.utc) - delta,
                                     action='Intro To Programming - C')
        Timetable.objects.filter(action='Finish Semester').update(time=datetime.now(tz=timezone.utc))

    def test_semester_end_created(self):
        process_timetable(user=self.user)
        user_data = UserData.objects.get(user=self.user)
        self.assertTrue(user_data.semester == 2)
        self.assertTrue(user_data.math >= 15)
        self.assertTrue(Abilities.objects.filter(user=self.user, ability='Logic').exists())  # sette per mille che falla
        timetable = Timetable.objects.filter(action='Finish Semester')
        self.assertTrue(timetable.count() == 1)
        timetable = Timetable.objects.filter(action='End Day')
        self.assertTrue(timetable.count() == 28)


class ExtendTimetable(TestCase):
    def setUp(self):
        self.now = datetime.now(tz=timezone.utc)
        self.user = User.objects.create(username='abc')
        self.data = [
            {'hour': self.now.hour, 'action': 'Sleep'},
            {'hour': self.now.hour + 1, 'action': 'Sleep'},
        ]

    def test_valid_timetable(self):
        result = validate_and_process_timetable_change(self.user, self.data)
        self.assertTrue(result[1] == 'Timetable successfully saved')
        self.assertTrue(Timetable.objects.filter(user=self.user).count() == 17)

    def test_invalid_timetable(self):
        result = validate_and_process_timetable_change(self.user, [
            *self.data, {'hour': self.now.hour + 15 % HOURS_IN_DAY, 'action': 'Sleep'}
        ])
        self.assertTrue(result[1] == f'Invalid timetable. '
                                     f'Chosen time: {self.now.hour + 15 % HOURS_IN_DAY} is too far into the future')
        self.assertTrue(Timetable.objects.filter(user=self.user).count() == 15)


class TestValidActions(TestCase):
    def setUp(self):
        self.now = datetime.now(tz=timezone.utc)
        self.user = User.objects.create(username='abc')
        self.data = [
            {'hour': self.now.hour, 'action': 'Sleep'},
            {'hour': self.now.hour + 1, 'action': 'Sleep'},
        ]

    def test_list_valid(self):
        res = list_valid_actions(self.user)
        self.assertEqual(len(res), 12)
        self.assertTrue(all(len(x['actions']) >= 6 for x in res))
