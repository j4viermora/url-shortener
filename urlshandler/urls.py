from .views import ShortUrlViewSet
from rest_framework.routers import DefaultRouter

urlshandler_router = DefaultRouter()
urlshandler_router.register(
    r'',
    ShortUrlViewSet
)

urlpatterns = urlshandler_router.urls
