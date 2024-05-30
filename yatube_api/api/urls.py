from django.urls import include, path
from rest_framework.routers import SimpleRouter

from api.views import (CommentModelViewSet,
                       FollowModelViewSet,
                       GroupReadOnlyModelViewSet,
                       PostModelViewSet)


v1_router = SimpleRouter()
v1_router.register('posts', PostModelViewSet)
v1_router.register('groups', GroupReadOnlyModelViewSet)
v1_router.register('follow', FollowModelViewSet, basename='follow')
v1_router.register(r'posts/(?P<post_id>[\d]+)/comments',
                   CommentModelViewSet, basename='comments')

urlpatterns = [
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(v1_router.urls)),
]
