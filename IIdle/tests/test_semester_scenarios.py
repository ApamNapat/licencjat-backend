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
                Party.process_action(self.user)
            for _ in range(7):
                Sleep.process_action(self.user)
            for _ in range(3):
                Work.process_action(self.user)
            Logic.process_action(self.user)
            CalculusI.process_action(self.user)
            IntroToProgrammingPython.process_action(self.user)
            IntroToCS.process_action(self.user)
            for _ in range(2):
                Relax.process_action(self.user)
                LearnMath.process_action(self.user)
                LearnProgramming.process_action(self.user)
                LearnAlgorithms.process_action(self.user)
            EndDay.process_action(self.user)

    @patch('IIdle.actions.uniform', return_value=1)
    def test_near_perfect_semester(self, _):
        FinishSemester.process(self.user)
        self.user.refresh_from_db()
        self.assertEqual(CompletedCourses.objects.all().count(), 4)


class AverageFirstSemester(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')
        for x in range(10):
            if x % 2 == 0:
                Party.process_action(self.user)
            for _ in range(7):
                Sleep.process_action(self.user)
            for _ in range(3):
                Work.process_action(self.user)
            Logic.process_action(self.user)
            CalculusI.process_action(self.user)
            IntroToProgrammingPython.process_action(self.user)
            IntroToCS.process_action(self.user)
            for _ in range(2):
                Relax.process_action(self.user)
                LearnMath.process_action(self.user)
                LearnProgramming.process_action(self.user)
                LearnAlgorithms.process_action(self.user)
            EndDay.process_action(self.user)

    @patch('IIdle.actions.uniform', return_value=1.5)
    def test_average_semester(self, _):
        FinishSemester.process_action(self.user)
        self.user.refresh_from_db()
        self.assertEqual(CompletedCourses.objects.all().count(), 4)


class SecondSemester(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')
        self.user.data.algorithms = 6
        self.user.data.math = 16
        self.user.data.programming = 12
        self.user.data.work_experience = 12
        self.user.data.save()
        for course in [
            'Logic', 'Calculus I', 'Intro To Programming - C', 'Introduction To Computer Science',
        ]:
            CompletedCourses.objects.create(user=self.user, course=course)

        for x in range(12):
            if x % 2 == 0:
                Party.process_action(self.user)
            for _ in range(7):
                Sleep.process_action(self.user)
            for _ in range(3):
                Work.process_action(self.user)
            Programming.process_action(self.user)
            Algebra.process_action(self.user)
            CppProgramming.process_action(self.user)
            OOP.process_action(self.user)
            for _ in range(2):
                Relax.process_action(self.user)
                LearnMath.process_action(self.user)
                LearnProgramming.process_action(self.user)
                LearnAlgorithms.process_action(self.user)
            EndDay.process_action(self.user)

    @patch('IIdle.actions.uniform', return_value=1.5)
    def test_second_semester(self, _):
        FinishSemester.process_action(self.user)
        self.user.refresh_from_db()
        self.assertEqual(CompletedCourses.objects.all().count(), 8)


class ThirdSemester(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')
        self.user.data.algorithms = 13
        self.user.data.math = 30
        self.user.data.programming = 30
        self.user.data.work_experience = 25
        self.user.data.save()
        for course in [
            'Logic', 'Calculus I', 'Intro To Programming - C', 'Introduction To Computer Science', 'Programming',
            'Algebra', 'C++ Programming', 'Object Oriented Programming',
        ]:
            CompletedCourses.objects.create(user=self.user, course=course)

        for x in range(12):
            if x % 2 == 0:
                Party.process_action(self.user)
            for _ in range(7):
                Sleep.process_action(self.user)
            for _ in range(3):
                Work.process_action(self.user)
            NumericalAnalysis.process_action(self.user)
            DiscreteMath.process_action(self.user)
            Probability.process_action(self.user)
            FunctionalProgramming.process_action(self.user)
            for _ in range(2):
                Relax.process_action(self.user)
                LearnMath.process_action(self.user)
                LearnProgramming.process_action(self.user)
                LearnAlgorithms.process_action(self.user)
            EndDay.process_action(self.user)

    @patch('IIdle.actions.uniform', return_value=2)
    def test_third_semester(self, _):
        FinishSemester.process_action(self.user)
        self.user.refresh_from_db()
        self.assertEqual(CompletedCourses.objects.all().count(), 12)


class FourthSemester(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')
        self.user.data.algorithms = 20
        self.user.data.math = 50
        self.user.data.programming = 42
        self.user.data.work_experience = 37
        self.user.data.save()
        for course in [
            'Logic', 'Calculus I', 'Intro To Programming - C', 'Introduction To Computer Science', 'Programming',
            'Algebra', 'C++ Programming', 'Object Oriented Programming', 'Numerical Analysis', 'Discrete Math',
            'Probability', 'Functional Programming',
        ]:
            CompletedCourses.objects.create(user=self.user, course=course)

        for x in range(12):
            if x % 2 == 0:
                Party.process_action(self.user)
            for _ in range(7):
                Sleep.process_action(self.user)
            for _ in range(3):
                Work.process_action(self.user)
            AlgorithmsAndDataStructures.process_action(self.user)
            LinuxAdministration.process_action(self.user)
            ScalaProgramming.process_action(self.user)
            LambdaCalculus.process_action(self.user)
            for _ in range(2):
                Relax.process_action(self.user)
                LearnMath.process_action(self.user)
                LearnProgramming.process_action(self.user)
                LearnAlgorithms.process_action(self.user)
            EndDay.process_action(self.user)

    @patch('IIdle.actions.uniform', return_value=2)
    def test_fourth_semester(self, _):
        FinishSemester.process_action(self.user)
        self.user.refresh_from_db()
        self.assertTrue(CompletedCourses.objects.all().count() in (15, 16))


class FifthSemester(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')
        self.user.data.algorithms = 40
        self.user.data.math = 60
        self.user.data.programming = 58
        self.user.data.work_experience = 50
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
                Party.process_action(self.user)
            for _ in range(7):
                Sleep.process_action(self.user)
            for _ in range(3):
                Work.process_action(self.user)
            OperatingSystems.process_action(self.user)
            RustProgramming.process_action(self.user)
            MachineLearning.process_action(self.user)
            EmbeddedSystems.process_action(self.user)
            SoftwareEngineering.process_action(self.user)
            for _ in range(2):
                Relax.process_action(self.user)
                LearnMath.process_action(self.user)
                LearnProgramming.process_action(self.user)
                LearnAlgorithms.process_action(self.user)
            EndDay.process_action(self.user)

    @patch('IIdle.actions.uniform', return_value=1.5)
    def test_fifth_semester(self, _):
        FinishSemester.process_action(self.user)
        self.user.refresh_from_db()
        self.assertEqual(CompletedCourses.objects.all().count(), 21)


class SixthSemester(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='abc')
        self.user.data.algorithms = 50
        self.user.data.math = 70
        self.user.data.programming = 70
        self.user.data.work_experience = 75
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
                Party.process_action(self.user)
            for _ in range(7):
                Sleep.process_action(self.user)
            for _ in range(3):
                Work.process_action(self.user)
            Databases.process_action(self.user)
            ComputerNetworks.process_action(self.user)
            JFIZO.process_action(self.user)
            ArtificialIntelligence.process_action(self.user)
            for _ in range(2):
                Relax.process_action(self.user)
                LearnMath.process_action(self.user)
                LearnProgramming.process_action(self.user)
                LearnAlgorithms.process_action(self.user)
            EndDay.process_action(self.user)

    @patch('IIdle.actions.uniform', return_value=1.5)
    def test_sixth_semester(self, _):
        FinishSemester.process_action(self.user)
        self.user.refresh_from_db()
        self.assertTrue(CompletedCourses.objects.all().count() in (24, 25))
