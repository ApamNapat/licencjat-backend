from unittest.mock import patch

from django.contrib.auth.models import User
from django.test import TestCase

from IIdle.actions import (
    Sleep, Logic, CalculusI, IntroToProgrammingPython, IntroToCS, Work, LearnMath,
    LearnProgramming, LearnAlgorithms, EndDay, Relax, Party, FinishSemester, OOP, CppProgramming, Algebra, Programming,
    NumericalAnalysis, DiscreteMath, FunctionalProgramming, Probability, AlgorithmsAndDataStructures,
    LinuxAdministration, ScalaProgramming, LambdaCalculus, SoftwareEngineering, EmbeddedSystems, MachineLearning,
    RustProgramming, OperatingSystems, ArtificialIntelligence, JFIZO, ComputerNetworks, Databases
)
from IIdle.models import CompletedCourses


class GoodFirstSemester(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')
        for x in range(14):
            if x % 2 == 0:
                Party.process(self.user)
            for _ in range(7):
                Sleep.process(self.user)
            for _ in range(3):
                Work.process(self.user)
            Logic.process(self.user)
            CalculusI.process(self.user)
            IntroToProgrammingPython.process(self.user)
            IntroToCS.process(self.user)
            for _ in range(2):
                Relax.process(self.user)
                LearnMath.process(self.user)
                LearnProgramming.process(self.user)
                LearnAlgorithms.process(self.user)
            EndDay.process(self.user)

    @patch('IIdle.actions.uniform', return_value=1)
    def test_near_perfect_semester(self, _):
        FinishSemester.process(self.user)
        self.user.refresh_from_db()
        self.assertEqual(CompletedCourses.objects.all().count(), 4)
        self.assertEqual(self.user.data.semester, 2)


class AverageFirstSemester(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')
        for x in range(10):
            if x % 2 == 0:
                Party.process(self.user)
            for _ in range(7):
                Sleep.process(self.user)
            for _ in range(3):
                Work.process(self.user)
            Logic.process(self.user)
            CalculusI.process(self.user)
            IntroToProgrammingPython.process(self.user)
            IntroToCS.process(self.user)
            for _ in range(2):
                Relax.process(self.user)
                LearnMath.process(self.user)
                LearnProgramming.process(self.user)
                LearnAlgorithms.process(self.user)
            EndDay.process(self.user)

    @patch('IIdle.actions.uniform', return_value=1.5)
    def test_average_semester(self, _):
        FinishSemester.process(self.user)
        self.user.refresh_from_db()
        self.assertEqual(CompletedCourses.objects.all().count(), 4)
        self.assertEqual(self.user.data.semester, 2)


class SecondSemester(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')
        self.user.data.algorithms = 6
        self.user.data.math = 16
        self.user.data.programming = 12
        self.user.data.work_experience = 12
        self.user.data.semester = 2
        self.user.data.save()
        for course in [
            'Logic', 'Calculus I', 'Intro To Programming - C', 'Introduction To Computer Science',
        ]:
            CompletedCourses.objects.create(user=self.user, course=course)

        for x in range(12):
            if x % 2 == 0:
                Party.process(self.user)
            for _ in range(7):
                Sleep.process(self.user)
            for _ in range(3):
                Work.process(self.user)
            Programming.process(self.user)
            Algebra.process(self.user)
            CppProgramming.process(self.user)
            OOP.process(self.user)
            for _ in range(2):
                Relax.process(self.user)
                LearnMath.process(self.user)
                LearnProgramming.process(self.user)
                LearnAlgorithms.process(self.user)
            EndDay.process(self.user)

    @patch('IIdle.actions.uniform', return_value=1.5)
    def test_second_semester(self, _):
        FinishSemester.process(self.user)
        self.user.refresh_from_db()
        self.assertEqual(CompletedCourses.objects.all().count(), 8)
        self.assertEqual(self.user.data.semester, 3)


class ThirdSemester(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')
        self.user.data.algorithms = 13
        self.user.data.math = 30
        self.user.data.programming = 30
        self.user.data.work_experience = 25
        self.user.data.semester = 3
        self.user.data.save()
        for course in [
            'Logic', 'Calculus I', 'Intro To Programming - C', 'Introduction To Computer Science', 'Programming',
            'Algebra', 'C++ Programming', 'Object Oriented Programming',
        ]:
            CompletedCourses.objects.create(user=self.user, course=course)

        for x in range(12):
            if x % 2 == 0:
                Party.process(self.user)
            for _ in range(7):
                Sleep.process(self.user)
            for _ in range(3):
                Work.process(self.user)
            NumericalAnalysis.process(self.user)
            DiscreteMath.process(self.user)
            Probability.process(self.user)
            FunctionalProgramming.process(self.user)
            for _ in range(2):
                Relax.process(self.user)
                LearnMath.process(self.user)
                LearnProgramming.process(self.user)
                LearnAlgorithms.process(self.user)
            EndDay.process(self.user)

    @patch('IIdle.actions.uniform', return_value=1.7)
    def test_third_semester(self, _):
        FinishSemester.process(self.user)
        self.user.refresh_from_db()
        self.assertEqual(CompletedCourses.objects.all().count(), 12)
        self.assertEqual(self.user.data.semester, 4)


class FourthSemester(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')
        self.user.data.algorithms = 20
        self.user.data.math = 50
        self.user.data.programming = 42
        self.user.data.work_experience = 37
        self.user.data.semester = 4
        self.user.data.save()
        for course in [
            'Logic', 'Calculus I', 'Intro To Programming - C', 'Introduction To Computer Science', 'Programming',
            'Algebra', 'C++ Programming', 'Object Oriented Programming', 'Numerical Analysis', 'Discrete Math',
            'Probability', 'Functional Programming',
        ]:
            CompletedCourses.objects.create(user=self.user, course=course)

        for x in range(12):
            if x % 2 == 0:
                Party.process(self.user)
            for _ in range(7):
                Sleep.process(self.user)
            for _ in range(3):
                Work.process(self.user)
            AlgorithmsAndDataStructures.process(self.user)
            LinuxAdministration.process(self.user)
            ScalaProgramming.process(self.user)
            LambdaCalculus.process(self.user)
            for _ in range(2):
                Relax.process(self.user)
                LearnMath.process(self.user)
                LearnProgramming.process(self.user)
                LearnAlgorithms.process(self.user)
            EndDay.process(self.user)

    @patch('IIdle.actions.uniform', return_value=1.7)
    def test_fourth_semester(self, _):
        FinishSemester.process(self.user)
        self.user.refresh_from_db()
        self.assertTrue(CompletedCourses.objects.all().count() in (15, 16))
        self.assertEqual(self.user.data.semester, 5)


class FifthSemester(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')
        self.user.data.algorithms = 40
        self.user.data.math = 60
        self.user.data.programming = 58
        self.user.data.work_experience = 50
        self.user.data.semester = 5
        self.user.data.save()
        for course in [
            'Logic', 'Calculus I', 'Intro To Programming - C', 'Introduction To Computer Science', 'Programming',
            'Algebra', 'C++ Programming', 'Object Oriented Programming', 'Numerical Analysis', 'Discrete Math',
            'Probability', 'Functional Programming', 'Algorithms And Data Structures', 'Linux Administration',
            'Scala Programming', 'Lambda Calculus'
        ]:
            CompletedCourses.objects.create(user=self.user, course=course)

        for x in range(12):
            if x % 2 == 0:
                Party.process(self.user)
            for _ in range(7):
                Sleep.process(self.user)
            for _ in range(3):
                Work.process(self.user)
            OperatingSystems.process(self.user)
            RustProgramming.process(self.user)
            MachineLearning.process(self.user)
            EmbeddedSystems.process(self.user)
            SoftwareEngineering.process(self.user)
            for _ in range(2):
                Relax.process(self.user)
                LearnMath.process(self.user)
                LearnProgramming.process(self.user)
                LearnAlgorithms.process(self.user)
            EndDay.process(self.user)

    @patch('IIdle.actions.uniform', return_value=1.5)
    def test_fifth_semester(self, _):
        FinishSemester.process(self.user)
        self.user.refresh_from_db()
        self.assertEqual(CompletedCourses.objects.all().count(), 21)
        self.assertEqual(self.user.data.semester, 6)


class SixthSemester(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')
        self.user.data.algorithms = 50
        self.user.data.math = 70
        self.user.data.programming = 70
        self.user.data.work_experience = 75
        self.user.data.semester = 6
        self.user.data.save()
        for course in [
            'Logic', 'Calculus I', 'Intro To Programming - C', 'Introduction To Computer Science', 'Programming',
            'Algebra', 'C++ Programming', 'Object Oriented Programming', 'Numerical Analysis', 'Discrete Math',
            'Probability', 'Functional Programming', 'Algorithms And Data Structures', 'Linux Administration',
            'Scala Programming', 'Lambda Calculus', 'Operating Systems', 'Rust Programming', 'Software Engineering',
            'Machine Learning', 'Embedded Systems'
        ]:
            CompletedCourses.objects.create(user=self.user, course=course)

        for x in range(12):
            if x % 2 == 0:
                Party.process(self.user)
            for _ in range(7):
                Sleep.process(self.user)
            for _ in range(3):
                Work.process(self.user)
            Databases.process(self.user)
            ComputerNetworks.process(self.user)
            JFIZO.process(self.user)
            ArtificialIntelligence.process(self.user)
            for _ in range(2):
                Relax.process(self.user)
                LearnMath.process(self.user)
                LearnProgramming.process(self.user)
                LearnAlgorithms.process(self.user)
            EndDay.process(self.user)

    @patch('IIdle.actions.uniform', return_value=1.5)
    def test_sixth_semester(self, _):
        FinishSemester.process(self.user)
        self.user.refresh_from_db()
        self.assertTrue(CompletedCourses.objects.all().count() in (24, 25))
        self.assertEqual(self.user.data.semester, 6)
