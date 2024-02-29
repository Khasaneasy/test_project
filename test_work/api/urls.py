from django.urls import include, path
from rest_framework import routers

from api.views import ProductView, LessonView


router = routers.DefaultRouter()
router.register(r'products', ProductView, basename='product')
router.register(r'lessons', LessonView, basename='lesson')

urlpatterns = [
    path('v1/', include(router.urls)),
]
