from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase

from IIdle.actions import (FinishSemester, ACTION_TO_CLASS, Sleep, Logic, CalculusI, EndDay, Work, LearnMath,
                           LearnProgramming, LearnAlgorithms, Party, Relax)
from IIdle.models import ClassesTaken, CompletedCourses, UserData, Timetable, Abilities, ACTIONS_CHOICES


class TestMappingIntegrityWithModel(TestCase):
    def test_process_end_semester(self):
        self.assertTrue(len(ACTIONS_CHOICES) == len(ACTION_TO_CLASS))
        self.assertTrue(set(ACTION_TO_CLASS) - set(ACTIONS_CHOICES) == set())


class SemesterEndWorksPassed(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')
        UserData.objects.filter(user=self.user).update(math=50, programming=50, algorithms=50)
        ClassesTaken.objects.create(user=self.user, course='Logic', times_present=12)
        ClassesTaken.objects.create(user=self.user, course='Calculus I', times_present=8)
        ClassesTaken.objects.create(user=self.user, course='Intro To Programming - Python', times_present=12)
        ClassesTaken.objects.create(user=self.user, course='Introduction To Computer Science', times_present=10)

    def test_process_end_semester(self):
        FinishSemester.process(self.user)
        self.assertTrue(ClassesTaken.objects.filter(user=self.user).count() == 0)
        self.assertTrue(CompletedCourses.objects.filter(user=self.user).count() == 3)
        self.assertTrue(UserData.objects.get(user=self.user).semester == 2)


class SemesterEndWorksFailed(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')
        UserData.objects.filter(user=self.user).update(math=30)
        ClassesTaken.objects.create(user=self.user, course='Logic', times_present=6)
        ClassesTaken.objects.create(user=self.user, course='Calculus I', times_present=10)

    def test_process_end_semester(self):
        FinishSemester.process(self.user)
        self.assertTrue(ClassesTaken.objects.filter(user=self.user).count() == 0)
        self.assertTrue(CompletedCourses.objects.get(user=self.user).course == 'Calculus I')
        self.assertTrue(UserData.objects.get(user=self.user).semester == 1)


class SemesterEndWorksGotKickedOut(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')
        UserData.objects.filter(user=self.user).update(math=30, semester=5, failed_last_semester=True)
        CompletedCourses.objects.create(user=self.user, course='Logic')

    def test_process_end_semester(self):
        FinishSemester.process(self.user)
        self.assertTrue(ClassesTaken.objects.filter(user=self.user).count() == 0)
        self.assertFalse(CompletedCourses.objects.exists())
        self.assertTrue(UserData.objects.get(user=self.user).semester == 1)
        self.assertTrue(Timetable.objects.filter(user=self.user).count() == 30)


class SemesterEndWontRunExamTwice(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')
        UserData.objects.filter(user=self.user).update(math=30, programming=30)
        ClassesTaken.objects.create(user=self.user, course='Logic', times_present=15)

    def test_process_end_semester(self):
        end_semester = Timetable.objects.get(action='Finish Semester')
        FinishSemester.process(self.user)
        end_semester.delete()  # Would have been done by process_timetable
        ClassesTaken.objects.create(user=self.user, course='Logic', times_present=15)
        ClassesTaken.objects.create(user=self.user, course='Calculus I', times_present=15)
        ClassesTaken.objects.create(user=self.user, course='Intro To Programming - Python', times_present=15)
        ClassesTaken.objects.create(user=self.user, course='Introduction To Computer Science', times_present=15)
        FinishSemester.process(self.user)
        self.assertTrue(CompletedCourses.objects.filter(user=self.user).count() == 4)
        self.assertFalse(ClassesTaken.objects.exists())


class SleepingWorks(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')

    @patch('IIdle.actions.uniform', return_value=0.5)
    def test_sleeping(self, _):
        for x in range(20):
            Sleep.process(self.user)
        self.assertTrue(UserData.objects.get(user=self.user).energy == 60)
        self.assertTrue(UserData.objects.get(user=self.user).mood == 60)


class WorkingWorks(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')

    @patch('IIdle.actions.uniform', return_value=0.5)
    def test_working(self, _):
        for x in range(20):
            Work.process(self.user)
        self.assertTrue(UserData.objects.get(user=self.user).cash == 719)
        self.assertTrue(UserData.objects.get(user=self.user).mood == 60)
        self.assertTrue(UserData.objects.get(user=self.user).energy == 40)
        self.assertTrue(UserData.objects.get(user=self.user).work_experience == 10)


class LearningWorks(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')

    @patch('IIdle.actions.uniform', return_value=0.5)
    def test_learning(self, _):
        for x in range(20):
            LearnMath.process(self.user)
            LearnProgramming.process(self.user)
            LearnAlgorithms.process(self.user)
        self.assertTrue(UserData.objects.get(user=self.user).energy == 20)
        self.assertTrue(UserData.objects.get(user=self.user).mood == 80)
        self.assertTrue(UserData.objects.get(user=self.user).programming > 10)
        self.assertTrue(UserData.objects.get(user=self.user).math > 10)
        self.assertTrue(UserData.objects.get(user=self.user).algorithms > 10)


class RelaxingWorks(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')

    @patch('IIdle.actions.uniform', return_value=0.5)
    def test_relaxing(self, _):
        for x in range(200):
            Relax.process(self.user)
        self.assertTrue(UserData.objects.get(user=self.user).mood == 100)


class PartyingWorks(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')

    @patch('IIdle.actions.uniform', return_value=0.5)
    def test_partying(self, _):
        for x in range(20):
            Party.process(self.user)
        self.assertTrue(UserData.objects.get(user=self.user).energy == 60)
        self.assertTrue(UserData.objects.get(user=self.user).mood == 60)


class DayEndWorks(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')

    def test_sleeping(self):
        for _ in range(15):
            EndDay.process(self.user)
        self.user.refresh_from_db()
        self.assertTrue(self.user.data.cash == 0)
        self.assertTrue(self.user.data.energy == 0)
        self.assertTrue(self.user.data.mood == 0)


class ClassesCanGiveAbilities(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')

    @patch('IIdle.actions.random', side_effect=[0.1, 0.3, 0.001])
    def test_sleeping(self, _):
        Logic.process(self.user)
        CalculusI.process(self.user)
        self.assertTrue(Abilities.objects.get(user=self.user, ability='Logic'))
        self.assertFalse(Abilities.objects.filter(user=self.user, ability='Basic Calculus').exists())
        self.assertTrue(Abilities.objects.filter(user=self.user, ability='Intermediate Calculus').exists())
