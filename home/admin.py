from django.contrib import admin
from .models import ClothingProduct, Contact, users

# Register your models here.

admin.site.register(users)
admin.site.register(Contact)
admin.site.register(ClothingProduct)

