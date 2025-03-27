from django.contrib import admin
from img.models import *

# Register your models here.
class PictureInline(admin.StackedInline):
    model = Picture
    # Allows adding one extra image by default
    # extra = 1
class ProductAdmin(admin.ModelAdmin):
    inlines = [PictureInline]

admin.site.register(Product, ProductAdmin)