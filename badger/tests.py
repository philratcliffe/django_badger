from django.urls import resolve
from django.test import TestCase
from django.views.generic import TemplateView
from django.http import HttpRequest
from .models import Employee

class BadgerHomePageTest(TestCase):

    def test_root_url_resolves_to_template_view(self):
        found = resolve('/badger/')
        self.assertEqual(found.func.__name__, "TemplateView")

    def test_badger_home_page_returns_correct_html(self):
        response = self.client.get('/badger/')

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
        self.client.post('/badger/employee_create/',
                {'first_name':"fred", 'last_name': "bloggs",  })
        self.assertEqual(Employee.objects.last().first_name, "fred")

class EmployeeUpdateViewTests(TestCase):

    def setUp(self):
        self.first_name = "fred"
        self.last_name = "flintstone"
        self.updated_first_name="wilma"

        Employee.objects.create(first_name=self.first_name,
                last_name=self.last_name)

    def test_update_employee(self):
        employee = Employee.objects.first()
        pk = employee.pk
        response = self.client.post('/badger/employee_update/{}/'.format(pk),
                {'first_name':self.updated_first_name,
                'last_name':self.last_name})
        self.assertEqual(response.status_code, 302)
        first_name = Employee.objects.first().first_name
        self.assertEqual(self.updated_first_name, first_name)


