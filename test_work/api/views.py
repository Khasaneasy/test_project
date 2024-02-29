from rest_framework import viewsets, permissions
from .serializers import ProductSerializer, LessonSerializer
from project.models import Product, Lesson


class ProductView(viewsets.ModelViewSet):
    """Представление для работы с продуктами."""

    queryset = Product.objects.filter(
        accesscontrol__has_access=True
        ).distinct()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


class LessonView(viewsets.ModelViewSet):
    """Представление для работы с уроками."""

    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]
