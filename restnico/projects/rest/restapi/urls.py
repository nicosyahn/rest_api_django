from .views import KotaViewset, DistrikViewset 
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'kota', KotaViewset, basename='kota')
router.register(r'distrik', DistrikViewset, basename='distrik')

urlpatterns = router.urls