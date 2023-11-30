# customer_support/admin.py
from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'subject', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('subject', 'description')
    date_hierarchy = 'created_at'

    fieldsets = [
        ('Ticket Information', {'fields': ['user', 'subject', 'description']}),
        ('Status and Time', {'fields': ['status', 'created_at'], 'classes': ['collapse']}),
    ]

    readonly_fields = ('created_at',)

admin.site.register(Ticket, TicketAdmin)
