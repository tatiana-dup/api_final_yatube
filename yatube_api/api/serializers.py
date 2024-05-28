from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from posts.models import Comment, Follow, Group, Post


User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели поста."""
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели комментария."""
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели группы."""

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')
        read_only_fields = ('id', 'title', 'slug', 'description')


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для модели подписок."""
    user = serializers.SlugRelatedField(
        slug_field='username', read_only=True)
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Follow
        fields = ('user', 'following')

    def validate_following(self, value):
        user = self.context['request'].user
        if user == value:
            raise ValidationError('Вы не можете подписаться на самого себя.')
        if Follow.objects.filter(user=user, following=value).exists():
            raise ValidationError('Вы уже подписаны на этого пользователя.')
        return value
