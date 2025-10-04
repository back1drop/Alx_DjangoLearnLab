from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post

class PostCRUDTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='testpass123')
        self.user2 = User.objects.create_user(username='user2', password='testpass123')
        self.post = Post.objects.create(title='Test Post', content='Content here', author=self.user1)

    def test_posts_list_view(self):
        resp = self.client.get(reverse('posts-list'))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'Test Post')

    def test_create_post_requires_login(self):
        create_url = reverse('post-create')
        # not logged in
        resp = self.client.get(create_url)
        self.assertNotEqual(resp.status_code, 200)
        self.client.login(username='user2', password='testpass123')
        resp = self.client.get(create_url)
        self.assertEqual(resp.status_code, 200)

    def test_update_post_by_author(self):
        update_url = reverse('post-update', kwargs={'pk': self.post.pk})
      
        self.client.login(username='user2', password='testpass123')
        resp = self.client.get(update_url)
        
        self.assertNotEqual(resp.status_code, 200)

        
        self.client.login(username='user1', password='testpass123')
        resp = self.client.get(update_url)
        self.assertEqual(resp.status_code, 200)

    def test_delete_post_by_author(self):
        delete_url = reverse('post-delete', kwargs={'pk': self.post.pk})
        self.client.login(username='user2', password='testpass123')
        resp = self.client.post(delete_url)
      
        self.assertEqual(Post.objects.count(), 1)

        self.client.login(username='user1', password='testpass123')
        resp = self.client.post(delete_url)
        self.assertEqual(Post.objects.count(), 0)
