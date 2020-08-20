from datetime import datetime, timedelta, timezone

from django.contrib.auth.models import User
from django.db.models.signals import post_save

from IIdle.actions import FinishSemester, EndDay
from IIdle.consts import DAYS_IN_FORTNIGHT, HOURS_IN_DAY
from IIdle.models import UserData, Timetable


def create_user_data(sender, instance: User, created: bool, **kwargs):
    if created:
        UserData.objects.create(user=instance)
        now = datetime.now(tz=timezone.utc)
        semester_end_date = now.replace(hour=now.hour + 1 % HOURS_IN_DAY,
                                        minute=0, second=0, microsecond=0) + timedelta(days=DAYS_IN_FORTNIGHT)
        for i in range(DAYS_IN_FORTNIGHT):
            Timetable.objects.create(user=instance,
                                     time=now.replace(hour=0, minute=0,
                                                      second=0, microsecond=1) + timedelta(days=1 + i),
                                     action=EndDay.name)

        Timetable.objects.create(user=instance,
                                 time=semester_end_date,
                                 action=FinishSemester.name)


post_save.connect(receiver=create_user_data, sender=User, weak=False, dispatch_uid='User data handler')
