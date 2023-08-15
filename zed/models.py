from django.db import models
from datetime import datetime

class BlogPost(models.Model):
    image_1 = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    image_2 = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

class BlogDetail(models.Model):
    blog_post = models.OneToOneField(BlogPost, on_delete=models.CASCADE)
    content = models.TextField()
    comment = models.TextField()
    reply_to_comment = models.TextField()
    image_3 = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    image_4 = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    comment_author = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Blog Detail'
        verbose_name_plural = 'Blog Details'