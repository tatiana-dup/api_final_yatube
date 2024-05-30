from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from api.permissions import IsAuthorOrCreateReadOnly
from api.serializers import (CommentSerializer,
                             FollowSerializer,
                             GroupSerializer,
                             PostSerializer)
from api.viewsets import ListOrCreateViewSet
from posts.models import Group, Post


User = get_user_model()


class PostModelViewSet(viewsets.ModelViewSet):
    """Класс для обработки всех запросов, связанных с постами."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrCreateReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    """Класс для обработки запросов на чтение, связанных с группами."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


class CommentModelViewSet(viewsets.ModelViewSet):
    """Класс для обработки всех запросов, связанных с комментариями."""
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrCreateReadOnly,)

    def get_queryset(self):
        post = self.get_post_obj()
        return post.comments.all()

    def perform_create(self, serializer):
        post = self.get_post_obj()
        serializer.save(post=post, author=self.request.user)

    def get_post_obj(self):
        return get_object_or_404(Post, pk=self.kwargs['post_id'])


class FollowModelViewSet(ListOrCreateViewSet):
    """Класс для обработки запросов, связанных с подпиской."""
    serializer_class = FollowSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.followers.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
