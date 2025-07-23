from django.contrib import admin
from .models import Product, Category, Feedback

# Register your models here.
#admin.site.register(Product)
#admin.site.register(Category)
admin.site.register(Feedback)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':("text",)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':("name",)}