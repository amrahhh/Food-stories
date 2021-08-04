from rest_framework import serializers
from django.contrib.auth import  get_user_model

from accounts.api.serializers import UserSerializer
from stories.models import Recipe, Story, Tag, Category, Comment, Subscriber

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    reply = serializers.SerializerMethodField()
    author = UserSerializer()
    class Meta:
        model = Comment
        fields = [
            'id',
            'recipe',
            'author',
            'context',
            'reply',

        ]

    def get_reply(self, obj):
        reply = obj.sub_comments.all()  
        return CommentSerializer(reply, many =True).data


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'context',
            'author',
        ]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = [
            'id',
            'title'
        ]


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'title'
        ]


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'title'
        ]



class RecipeSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    author = UserSerializer()
    tags = TagSerializer(many=True)
    comments= serializers.SerializerMethodField()
    comment_count = serializers.SerializerMethodField()

    class Meta:
        model = Recipe
        fields = [
            'id',
            'title',
            'slug',
            'order',
            'short_description',
            'image',
            'description',
            'created_at',
            'category',
            'author',
            'comments',
            'comment_count',
            'tags',
        ]

    def get_comments(self, obj):
        return CommentSerializer(obj.comment.filter(parent_comment__isnull=True), many=True).data

    def get_comment_count(self, obj):
        return obj.comment.count()

class RecipeCreateSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = Recipe
        fields = [
            'id',
            'title',
            'order',
            'slug',
            'short_description',
            'image',
            'description',
            'created_at',
            'category',
            'author',
            'tags',
        ]

    def validate(self, data):
        request = self.context.get('request')
        data['author'] = request.user
        attrs = super().validate(data)
        return attrs
        
class StorySerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    author = UserSerializer()
    tags = TagSerializer(many=True)

    class Meta:
        model = Story
        fields = [
            'id',
            'title',
            'slug',
            'order',
            'image',
            'description',
            'created_at',
            'category',
            'author',
            'tags',
        ]


class StoryCreateSerializer(serializers.ModelSerializer):
    slug = serializers.CharField(read_only=True)

    class Meta:
        model = Story
        fields = [
            'id',
            'title',
            'order',
            'slug',
            'image',
            'description',
            'created_at',
            'category',
            'author',
            'tags',
        ]


class SubscriberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscriber
        fields = [
            'id',
            'email',
            'created_at',
            'updated_at',
        ] 