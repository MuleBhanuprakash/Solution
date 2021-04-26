from rest_framework import serializers
from .models import Blog, Bookmarks, VideoEmbed, ImageEmbed, GithubEmbed, TaskImage, Task, Quote, Photo
from rest_framework.serializers import ModelSerializer


class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


class BookmarkSerializer(ModelSerializer):
    class Meta:
        model = Bookmarks
        fields = '__all'


class VideoSerializer(ModelSerializer):
    class Meta:
        model = VideoEmbed
        fields = '__all__'


class ImageEmbedSerializer(ModelSerializer):
    class Meta:
        model = ImageEmbed
        fields = '__all__'


class GithubSerializer(ModelSerializer):
    class Meta:
        model = GithubEmbed
        fields = '__all__'

class TaskImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskImage
        fields = ('image',)

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    images = TaskImageSerializer(source='taskimage_set', many=True, read_only=True)

    class Meta:
        model = Task
        fields = ('id', 'title', 'user', 'images')

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        task = Task.objects.create(title=validated_data.get('title', 'no-title'),
                                   user_id=1)
        for image_data in images_data.values():
            TaskImage.objects.create(task=task, image=image_data, many=True)
        return task

class QuoteSerializer(ModelSerializer):
    class Meta:
        model = Quote
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):

    image = serializers.ListField(
        child=serializers.ImageField(allow_empty_file=False)
        )

    class Meta:
        model = Photo
        fields = ['name', 'image']

    def create(self, validated_data):
        images = validated_data.pop('image')
        for image in images:
            photo = Photo.objects.create(image=image, **validated_data)
        return photo
