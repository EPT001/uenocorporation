from django.contrib import admin
from uenowebsite.models import Category, Page, Enquiry, Product, Building


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class EnquiryAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_name', 'email', 'phone_number', 'product_choice', 'enquiry',)  # Display these fields
    list_filter = ('product_choice',)  # Filter by product choice
    search_fields = ('name', 'company_name', 'email')  # Search by these fields

class BuildingAdmin(admin.ModelAdmin):
    list_display = ('name', 'series')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)
admin.site.register(Enquiry, EnquiryAdmin)
admin.site.register(Product)
admin.site.register(Building)
