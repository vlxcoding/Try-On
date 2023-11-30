# checkout/admin.py
from django.contrib import admin
from .models import Order, OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'appointment', 'total_price', 'payment_status', 'created_at')
    list_filter = ('payment_status', 'created_at')
    search_fields = ('id', 'appointment__user__username')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'subtotal_price')
    list_filter = ('order__payment_status',)
    search_fields = ('order__id', 'product__name')
