from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth.views import LoginView


class IndexViewTests(TestCase):
    def test_no_question(self):
        """
        Если нет ни одного вопроса, то пользователь должен видет соответствующее сообщение.
        """
        response = self.client.get(reverse('qa:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No questions!")
        self.assertQuerysetEqual(response.context['question_list'], [])


class LoginViewTests(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(username='test_user', email='test@example.com', password='secret')

    def test_logout_button_for_authenticated_user(self):
        """
        Если пользователь уже авторизован, то ему должна показываться кнопка "Logout".
        """
        request = self.factory.get(reverse('qa:login'))

        # Simulate logged-in user
        request.user = self.user

        response = LoginView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Logout")

    def test_no_logout_button_for_not_authenticated_user(self):
        """
        Если пользователь не залогинен, то кнопка "Logout" не должна быть показана.
        """
        request = self.factory.get(reverse('qa:login'))

        request.user = AnonymousUser()
        response = LoginView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Logout")
