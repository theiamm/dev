# myapp/tests.py

from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Создаем тестовые данные, которые будут использоваться во всех методах тестирования
        Post.objects.create(title='Test Title', content='Test Content')

    def test_title_content(self):
        post = Post.objects.get(id=1)
        expected_title = f'{post.title}'
        expected_content = f'{post.content}'
        self.assertEqual(expected_title, 'Test Title')
        self.assertEqual(expected_content, 'Test Content')

    def test_str_method(self):
        post = Post.objects.get(id=1)
        self.assertEqual(str(post), 'Test Title')

