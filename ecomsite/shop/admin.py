from django.contrib import admin
from .models import Products, Order
# Register your models here.

# This changes name from Django Administration to E-commerce site when access the admin panel
admin.site.site_header = 'E-commerce Site'

# Changes the site title from Document to SwiftCart
admin.site.site_title = 'SwiftCart' 

# Changes the site Index from Site Administration to Manage SwiftCart
admin.site.index_title= "Manage SwiftCart"


class ProductsAdmin(admin.ModelAdmin):

    def change_category_to_default(self, request, queryset):
        queryset.update(category="default")

    change_category_to_default.short_description = 'Default Category'
    list_display = ('title', 'price', 'discount', 'category', 'description')
    search_fields = ('title',)  # must be a list or tuple
    actions = ('change_category_to_default',)
    fields = ('title', 'price')
    list_editable = ('price', 'category',)

admin.site.register(Products, ProductsAdmin)
admin.site.register(Order)