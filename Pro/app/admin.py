from django.contrib import admin
from app.models import Product,ProductImage


class ProductAdmin(admin.ModelAdmin):
    search_fields = ['title','description']
    list_display = ['__str__','active','price','slug','created']
    list_filter = ['created','updated']
    list_editable = ['price','active']
    # date_hierarchy = ['created']
    prepopulated_fields = {"slug":("title",)}
    class Meta:
        model = Product


admin.site.register(Product,ProductAdmin)

admin.site.register(ProductImage)
# Register your models here.
