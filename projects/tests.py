from django.test import TestCase, Client
from django.urls import reverse
from django.test.utils import setup_test_environment

from .forms import RegistrationForm

from projects.models import *

import time

client = Client()

# length of base template, used to test for empty pages
LEN_BASE = 2760

# Create your tests here.

class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="tom",
                            display_name="Tom Magnanti",
                            graduation_year=2018,
                            pillar="ISTD")

        User.objects.create(username="jane",
                            display_name="Jane Tan",
                            graduation_year=2021,
                            pillar="ESD")

    def test_user_basic_info(self):
        tom = User.objects.get(username="tom")
        self.assertEqual(tom.pillar, "ISTD")
        self.assertEqual(tom.graduation_year, 2018)
        self.assertEqual(tom.display_name, "Tom Magnanti")

        jane = User.objects.get(username="jane")
        self.assertEqual(jane.pillar, "ESD")
        self.assertEqual(jane.graduation_year, 2021)
        self.assertEqual(jane.display_name, "Jane Tan")

    def test_user_page(self):
        url = reverse('projects:user', args=("tom",))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.content), LEN_BASE)

        url = reverse('projects:user', args=("jane",))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.content), LEN_BASE)

    def test_user_page_contents(self):
        url = reverse('projects:user', args=("tom",))
        response = str(self.client.get(url).content)
        self.assertEqual("Tom Magnanti" in response, True)

        url = reverse('projects:user', args=("jane",))
        response = str(self.client.get(url).content)
        self.assertEqual("Jane Tan" in response, True)

    def test_user_page_performance(self):
        start = time.time()

        for i in range(10):
            url = reverse('projects:user', args=("tom",))
            response = self.client.get(url)
            url = reverse('projects:user', args=("jane",))
            response = self.client.get(url)

        duration = time.time() - start
        self.assertLess(duration, 1.0)

class ProjectShowcaseTestCase(TestCase):
    def setUp(self):
        Project.objects.create(title="OpenSUTD Web Platform",
                               project_uid="ACAD_00001",
                               caption="Sample project 1",
                               category="ACAD",
                               url="https://github.com/OpenSUTD/web-platform-prototype",
                               status="ACCEPT")

        User.objects.create(username="tom",
                            display_name="Tom Magnanti",
                            graduation_year=2018,
                            pillar="ISTD")

        User.objects.create(username="jane",
                            display_name="Jane Tan",
                            graduation_year=2021,
                            pillar="ESD")

    def test_add_user_project(self):
        tom = User.objects.get(username="tom")
        jane = User.objects.get(username="jane")

        proj = Project.objects.get(project_uid="ACAD_00001")
        proj.users.add(tom)
        proj.users.add(jane)

        self.assertEqual(len(proj.users.all()), 2)

    def test_add_del_user_project(self):
        tom = User.objects.get(username="tom")
        jane = User.objects.get(username="jane")

        proj = Project.objects.get(project_uid="ACAD_00001")
        proj.users.add(tom)
        proj.users.add(jane)

        proj.users.remove(jane)

        self.assertEqual(len(proj.users.all()), 1)

    def test_project_page(self):
        url = reverse('projects:showcase', args=("ACAD_00001",))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.content), LEN_BASE)

    # TODO: test project page contents

    def test_project_page_performance(self):
        start = time.time()

        for i in range(10):
            url = reverse('projects:showcase', args=("ACAD_00001",))
        response = self.client.get(url)

        duration = time.time() - start
        self.assertLess(duration, 1.0)


class TestRegistrationForm(TestCase):

    # https://www.agiliq.com/blog/2018/05/django-unit-testing/#writing-tests-for-forms

    def test_registration_form(self):
        # test invalid data
        invalid_data = {
            "username": "user@test.com",
            "password": "secret",
            "confirm": "not secret"
        }
        form = RegistrationForm(data=invalid_data)
        form.is_valid()
        self.assertTrue(form.errors)

        # test valid data
        valid_data = {
            "username": "user@test.com",
            "password": "secret",
            "confirm": "secret"
        }

        form = RegistrationForm(data=valid_data)
        form.is_valid()
        self.assertFalse(form.errors)