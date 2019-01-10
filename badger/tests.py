from django.urls import resolve
from django.urls import reverse
from django.test import TestCase
from django.views.generic import TemplateView
from django.http import HttpRequest
from .models import Employee
from users.models import CustomUser


class BadgerHomePageTest(TestCase):
    def test_badger_root_url_resolves_to_template_view(self):

        url = reverse('badger:index')

        found = resolve(url)
        self.assertEqual(found.func.__name__, "TemplateView")

    def test_badger_home_page_returns_correct_html(self):
        url = reverse('badger:index')
        response = self.client.get(url)

        #
        # Decode the response and strip the newlines so startswith and
        # endwith calls will work.
        #
        html = response.content.decode('utf8').strip('\n')

        self.assertTrue(html.startswith('<!doctype html>'))
        self.assertIn('Badger', html)
        self.assertTrue(html.endswith('</html>'))


class EmployeeCreateViewTests(TestCase):
    def test_create_employee(self):
        response = self.client.post(
            reverse('badger:employee_create'), {
                'first_name': "fred",
                'last_name': "bloggs",
            },
            follow=True)
        html = response.content.decode('utf8')
        self.assertIn("fred bloggs", html)
        self.assertEqual(Employee.objects.last().first_name, "fred")


class DetailViewTests(TestCase):
    def setUp(self):
        employee = Employee.objects.create(
            first_name='fred', last_name='flintstone')
        self.slug = employee.slug

    def test_details_view_shows_employee_name(self):
        response = self.client.get(
            reverse('badger:employee_detail', args=[self.slug]))
        self.assertEqual(response.status_code, 200)
        html = response.content.decode('utf8')
        self.assertIn("fred flintstone", html)


class EmployeeUpdateViewTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='user1')
        self.user.set_password('pass')
        self.user.save()
        self.first_name = "fred"
        self.last_name = "flintstone"
        self.updated_first_name = "wilma"

        Employee.objects.create(
            first_name=self.first_name, last_name=self.last_name)

    def test_update_employee(self):
        employee = Employee.objects.first()
        slug = employee.slug
        self.client.login(username='user1', password='pass')
        response = self.client.post(
            reverse('badger:employee_update', args=[slug]), {
                'first_name': self.updated_first_name,
                'last_name': self.last_name
            },
            follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "wilma flintstone")
        first_name = Employee.objects.first().first_name
        self.assertEqual(self.updated_first_name, first_name)
        last_name = Employee.objects.first().last_name
        self.assertEqual(self.last_name, last_name)


class EmployeeListViewTests(TestCase):
    def setUp(self):
        self.first_name = "fred"
        self.last_name = "flintstone"

        Employee.objects.create(
            first_name=self.first_name, last_name=self.last_name)

    def test_list_employees_page_returns_correct_html(self):
        response = self.client.get(reverse('badger:employee_list'))
        self.assertEqual(response.status_code, 200)
        html = response.content.decode('utf8').strip('\n')
        self.assertTrue(html.startswith('<!doctype html>'))
        self.assertIn(self.first_name, html)
        self.assertIn(self.last_name, html)
