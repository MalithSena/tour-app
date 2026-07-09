from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'nationality', 'passport_number', 'created_at')
    search_fields = ('full_name', 'passport_number', 'nationality')
    list_filter = ('nationality',)