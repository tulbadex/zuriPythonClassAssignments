from django.contrib.auth import get_user_model, get_user
from django.contrib import auth

from django.test import TestCase, Client
from django.urls import reverse

from .models import Post, Comment
# Create your tests here.


class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@gmail.com',
            password='secrete'
        )

        self.post = Post.objects.create(
            title='create title',
            body='Nice body',
            author=self.user
        )

        self.client = Client()

        self.comment = Comment.objects.create(
            comment='create title',
            author=self.user,
            post=self.post
        )

    def test_string_representation(self):
        post = Post(title="A simple title")
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'create title')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'Nice body')

    def test_post_list_view(self):
        response = self.client.get(reverse('posts:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Nice body')
        self.assertTemplateUsed(response, 'home.html')

    def test_post_detail_views(self):
        response = self.client.get('/blog/1/')
        no_response = self.client.get('/blog/99/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'create title')
        self.assertTemplateUsed(response, 'post_detail.html')

    def test_login(self):
        response = self.client.post(
            '/accounts/login/', {'username': self.user.username, 'password': self.user.password})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_logout(self):
        # self.assertTrue(self.user.is_authenticated)
        response = self.client.post(
            '/accounts/logout/', {'username': self.user.username, 'password': self.user.password})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/blog/', status_code=302,
                             target_status_code=200, fetch_redirect_response=True)
        # print(self.user.is_authenticated)

    def test_auth_user_can_comment(self):
        login = self.client.login(username='testuser', password='secrete')

        """ response = self.client.post('/blog/1/comment/', {"comment":"life is good"})
        print(response) """
        # self.assertRedirects(response, '/blog/1/', status_code=302)

        """ comment = Comment(comment="A simple title")
        self.assertEqual(str(comment), comment.comment) """
        
        response = self.client.post('/blog/1/comment/', {"comment":"A simple title"})
        print(response)

    def test_non_auth_user_can_not_comment(self):
        response = self.client.get('/blog/1/comment/')
        self.assertEqual(response.status_code, 404)
