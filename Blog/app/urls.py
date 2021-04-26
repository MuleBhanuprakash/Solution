from rest_framework.routers import DefaultRouter, BaseRouter, SimpleRouter
from .views import *

router = DefaultRouter()
# router = BaseRouter.register(self, viewset=[DefaultRouter, SimpleRouter], prefix=True)
# router = SimpleRouter()
router.register('upload', UploadViewSet, basename='users')
router.register('blog', BlogViewSet, basename='blog')
router.register('bookmark', BookmarkViewSet, basename='bookmark')
router.register('video', VideoViewSet, basename='video')
router.register('image_embed', ImageEmbedViewSet, basename='image_embed')
router.register('github', GithubViewSet, basename='github')
# router.register('image_upload', ImageUploadViewSet, basename='image_upload')
router.register('quote', QuoteViewSet, basename='quote')

urlpatterns = router.urls
