from rest_framework import serializers

from project.models import Product, Lesson


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор дляч Product."""

    lesson_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('name', 'start_date', 'cost', 'lesson_count')

    def get_lesson_count(self, obj):
        """Получение кол-ва уроков."""
        return Lesson.objects.filter(product=obj).count()


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор дляч Lesson."""

    class Meta:
        model = Lesson
        fields = ('name', 'video_link')
