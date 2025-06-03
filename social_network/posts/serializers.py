from rest_framework import serializers
from .models import Post, Comment, Like
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = ['author', 'text', 'created_at']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'text', 'image', 'created_at', 'comments', 'likes_count']

    def get_likes_count(self, obj):
        return obj.likes.count()
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['key']  

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'post', 'user']  
