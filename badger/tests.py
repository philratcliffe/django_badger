from django.contrib.auth.models import Permission
from django.urls import resolve
from django.urls import reverse
from django.test import TestCase
from django.views.generic import TemplateView
from django.http import HttpRequest
from .models import Employee, Badge
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


class BadgeListViewTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='user1')
        self.user.set_password('pass')
        self.user.save()
        self.badge_name = "testing 123 badge"
        Badge.objects.create(
            name=self.badge_name)


    def test_list_badges(self):
        self.client.login(username='user1', password='pass')
        response = self.client.get(reverse('badger:badge_list'))
        html = response.content.decode('utf8')
        self.assertIn(self.badge_name, html)


class BadgeCreateViewTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='user1')
        self.user.set_password('pass')
        permission = Permission.objects.get(codename='add_badge')
        self.user.user_permissions.add(permission)
        self.user.save()

    def test_create_badge(self):
        self.client.login(username='user1', password='pass')
        response = self.client.post(
            reverse('badger:badge_create'), {
                'name': "test-badge",
            },
            follow=True)
        html = response.content.decode('utf8')
        self.assertIn("test-badge", html)
        self.assertEqual(Badge.objects.last().name, "test-badge")

class EmployeeCreateViewTests(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create(username='user1')
        self.user.set_password('pass')
        self.user.save()

    def test_create_employee(self):
        self.client.login(username='user1', password='pass')
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
        self.user = CustomUser.objects.create(username='user1')
        self.user.set_password('pass')
        self.user.save()
        employee = Employee.objects.create(
            first_name='fred', last_name='flintstone')
        self.slug = employee.slug

    def test_details_view_shows_employee_name(self):
        self.client.login(username='user1', password='pass')
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
        self.user = CustomUser.objects.create(username='user1')
        self.user.set_password('pass')
        self.user.save()
        self.first_name = "fred"
        self.last_name = "flintstone"

        Employee.objects.create(
            first_name=self.first_name, last_name=self.last_name)

    def test_list_employees_page_returns_correct_html(self):
        self.client.login(username='user1', password='pass')
        response = self.client.get(reverse('badger:employee_list'))
        self.assertEqual(response.status_code, 200)
        html = response.content.decode('utf8').strip('\n')
        self.assertTrue(html.startswith('<!doctype html>'))
        self.assertIn(self.first_name, html)
        self.assertIn(self.last_name, html)
