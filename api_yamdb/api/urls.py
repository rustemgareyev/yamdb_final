from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import (CategoryViewSet, CommentsViewSet, GenreViewSet,
                       ReviewViewSet, SignUpViewSet, TitleViewSet,
                       TokenViewSet, UserViewSet)

app_name = 'reviews'
app_name = 'api'

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'titles', TitleViewSet, basename='titles')
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='reviews')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentsViewSet,
    basename='comments')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/signup/', SignUpViewSet.as_view()),
    path('v1/auth/token/', TokenViewSet.as_view()),
]
