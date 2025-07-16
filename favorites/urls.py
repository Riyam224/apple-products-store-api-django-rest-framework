from rest_framework.routers import DefaultRouter
from .views import FavoriteViewSet

router = DefaultRouter()
router.register("favorites", FavoriteViewSet)


urlpatterns = router.urls
