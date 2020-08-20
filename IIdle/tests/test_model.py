from django.contrib.auth.models import User
from django.test import TestCase

from IIdle.models import UserData, Timetable


class UserDataAndSemesterEndAdded(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='abc')
        self.user2 = User.objects.create(username='xyz')

    def test_user_data_created(self):
        first = UserData.objects.get(user__username='abc')
        second = UserData.objects.get(user__username='xyz')
        self.assertTrue(first.cash == second.cash == 500)
        self.assertTrue(first.energy == second.energy == 50)
        self.assertTrue(first.mood == second.mood == 50)

    def test_semester_end_created(self):
        self.assertEqual(Timetable.objects.filter(user=self.user1, action='Finish Semester').count(), 1)
        self.assertEqual(Timetable.objects.filter(user=self.user2, action='Finish Semester').count(), 1)
        self.assertEqual(Timetable.objects.filter(action='End Day').count(), 28)
