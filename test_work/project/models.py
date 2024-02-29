from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    """Доступный продукт."""

    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)


class AccessControl(models.Model):
    """Управление доступом к продуктам."""

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    has_access = models.BooleanField(default=False)


class Lesson(models.Model):
    """Уроки."""

    name = models.CharField(max_length=50)
    video_link = models.URLField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Group(models.Model):
    """Группы пользователей для обучения."""

    name = models.CharField(max_length=50)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    min_students = models.PositiveIntegerField()
    max_students = models.PositiveIntegerField()
    students = models.ManyToManyField(User)
