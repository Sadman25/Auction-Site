from django.contrib import admin
from .models import product,images,status,category

# Register your models here.
admin.site.register(category)
admin.site.register(product)
admin.site.register(images)
admin.site.register(status)