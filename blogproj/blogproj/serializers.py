from rest_framework import serializers
from django.contrib.auth.models import User
from blog.models import Post

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'