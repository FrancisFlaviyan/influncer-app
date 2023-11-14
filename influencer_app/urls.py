from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AllDataViewSet

router = DefaultRouter()
router.register(r'alldata', AllDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('all-data/', AllDataViewSet.as_view({'get': 'list', 'post': 'create'}), name='all-data'),
]
