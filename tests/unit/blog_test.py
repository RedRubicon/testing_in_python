from unittest import TestCase
from blog import Blog
from post import Post


class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog('Test', 'Test Author')

        self.assertEqual(b.title, 'Test')
        self.assertEqual(b.author, 'Test Author')
        self.assertListEqual(b.posts, [])

    def test_repr(self):
        b = Blog('Test', 'Test Author')

        expected = "Test: Test Author"
        actual = repr(b)

        self.assertEqual(actual, expected)