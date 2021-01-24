from unittest import TestCase
from blog import Blog


class BlogIntegrationTest(TestCase):
    def test_create_post_in_blog(self):
        b = Blog('Test Blog', 'Test Author')
        
        b.create_post('Post','Content')

        self.assertEqual(1,len(b.posts))
        self.assertEqual(b.posts[0].title, 'Post')
        self.assertEqual(b.posts[0].content, 'Content')

    def test_json(self):
        b = Blog('Test Blog', 'Test Author')
        b.create_post('Post','Content')

        expected = {
            'title': 'Test Blog',
            'author': 'Test Author',
            'posts': [{
                'title': 'Post',
                'content': 'Content',
                }
            ],
        }

        actual = b.json()

        self.assertDictEqual(expected, actual)