from django.contrib import admin
from .models import Product, AccessControl, Lesson, Group

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'creator', 'start_date', 'cost')
    search_fields = ('creator',)


admin.site.register(Product, ProductAdmin)
admin.site.register(AccessControl)
admin.site.register(Lesson)
admin.site.register(Group)
