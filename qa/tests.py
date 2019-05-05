from django.test import TestCase
from django.urls import reverse


class IndexViewTests(TestCase):
    def test_no_question(self):
        """
        Если нет ни одного вопроса, то пользователь должен видет соответствующее сообщение.
        """
        response = self.client.get(reverse('qa:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No questions!")
        self.assertQuerysetEqual(response.context['question_list'], [])
