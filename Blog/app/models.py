from abc import ABC, abstractmethod

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from djongo import models
from embed_video.fields import EmbedVideoField


# Create your models here.

class Blog(models.Model):
    blog = models.CharField(max_length=250)
    blog_url = models.URLField(blank=True, default='')
    description = models.TextField()

    def __str__(self):
        return self.blog


class Bookmarks(models.Model):
    # bookmark = models.EmbeddedModelField()
    name = models.CharField(max_length=200)
    bookmark = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_created=True)

    def __str__(self):
        return self.name


class Video(models.Model):
    title = models.CharField(max_length=250)
    video = EmbedVideoField()
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_created=True)

    def __str__(self):
        return self.video


class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    image = models.ImageField(max_length=200)
    # image = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_created=True)

    def __str__(self):
        return self.name


class GitHub(models.Model):
    id = models.IntegerField(primary_key=True)
    github_name = models.CharField(max_length=200)
    github = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True, auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_created=True)

    def __str__(self):
        return self.github_name


class VideoEmbed(models.Model):
    title = models.CharField(max_length=250)
    video = EmbedVideoField()

    def __str__(self):
        return self.title

    def clean(self):
        if self.video is None:
            raise ValidationError('Please upload you video')

    def save(self, *args, **kwargs):
        super(VideoEmbed, self).save(*args, **kwargs)


class ImageEmbed(models.Model):
    image_name = models.EmbeddedField(
        Image,
    )

    def __str__(self):
        return self.image_name


class GithubEmbed(models.Model):
    name = models.CharField(max_length=200)
    image = models.EmbeddedField(
        model_container=GitHub,
    )

    def __str__(self):
        return self.name


class Quote(models.Model):
    name = models.CharField(max_length=200)
    blog_url = models.URLField(blank=True, default='')
    description = models.TextField()

    def __str__(self):
        return self.name


# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        super(Task, self).save(*args, **kwargs)


class TaskImage(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    image = models.FileField(blank=True)

    def __str__(self):
        return self.task.title


class Photo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.name
