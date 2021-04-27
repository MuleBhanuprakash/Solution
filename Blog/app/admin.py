from django.contrib import admin
from .models import Blog, Bookmarks, VideoEmbed, ImageEmbed, GithubEmbed, TaskImage, Quote, Photo
# Register your models here.

admin.site.register([Blog, Bookmarks, VideoEmbed, ImageEmbed, GithubEmbed, TaskImage, Quote, Photo])
