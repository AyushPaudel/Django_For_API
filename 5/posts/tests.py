from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post

class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username="username1", password="123abc@"
        )
        testuser1.save()

        test_post = Post.objects.create(
            author= testuser1,
            title="Blog test",
            body="Something"
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'

        self.assertEqual(author, "username1")
        self.assertEqual(title, "Blog test")
        self.assertEqual(body, "Something")