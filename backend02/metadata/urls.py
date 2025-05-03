from rest_framework.routers import DefaultRouter
from .views import TitleRecordViewSet

router = DefaultRouter()
router.register(r'titles', TitleRecordViewSet, basename='title')

urlpatterns = router.urls

