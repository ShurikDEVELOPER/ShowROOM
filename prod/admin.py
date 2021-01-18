from django.contrib import admin
from .models import Images, Sex, Product, Brand, Material, ZipType
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'price',)


admin.site.register(Product, ProductAdmin)


# admin.site.register(Product)
admin.site.register(Sex)
admin.site.register(Brand)
admin.site.register(Material)
admin.site.register(ZipType)

# Images
admin.site.register(Images)
