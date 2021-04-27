from django.shortcuts import render
from rest_framework.response import Response

from .models import Blog, Bookmarks, VideoEmbed, ImageEmbed, GithubEmbed, Task, Quote, Photo
from .serializers import BlogSerializer, BookmarkSerializer, VideoSerializer, ImageEmbedSerializer, GithubSerializer, \
    PhotoSerializer, QuoteSerializer, TaskSerializer
from rest_framework.viewsets import ModelViewSet


class BlogViewSet(ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()

    def get_queryset(self):
        return self.request.all()

class BookmarkViewSet(ModelViewSet):
    serializer_class = BookmarkSerializer
    queryset = Bookmarks.objects.all()


class VideoViewSet(ModelViewSet):
    serializer_class = VideoSerializer
    queryset = VideoEmbed.objects.all()


class ImageEmbedViewSet(ModelViewSet):
    serializer_class = ImageEmbedSerializer
    queryset = ImageEmbed.objects.all()


class GithubViewSet(ModelViewSet):
    serializer_class = GithubSerializer
    queryset = GithubEmbed.objects.all()


class UploadViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class QuoteViewSet(ModelViewSet):
    serializer_class = QuoteSerializer
    queryset = Quote.objects.all()

class PhotViewSet(ModelViewSet):
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()