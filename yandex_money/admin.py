# -*- coding: utf-8 -*-

from django.contrib import admin
from .models import Payment


class PaymentAdmin(admin.ModelAdmin):
    list_display_links = ('customer_number',)
    list_display = ('customer_number', 'payment_type', 'shop_amount',
                    'shop_currency', 'invoice_id', 'status', 'pub_date', 'user', 'cps_phone')
    list_filter = ('pub_date', 'status')
    search_fields = ('customer_number', 'cps_email', 'cps_phone', 'scid', 'shop_id', 'invoice_id')

admin.site.register(Payment, PaymentAdmin)