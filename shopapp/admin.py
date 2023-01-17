from django.contrib import admin
from .models import NewProduct
# Register your models here.

class NewproductAdmin(admin.ModelAdmin):
    list_display=["Name","Description","Price"]


admin.site.register(NewProduct,NewproductAdmin)