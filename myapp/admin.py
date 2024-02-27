from django.contrib import admin
from .models import JournalEnteryLines, Account, Currency


@admin.register(JournalEnteryLines)
class JournalEnteryLinesAdmin(admin.ModelAdmin):
    list_display=['id', 'accounting_date', 'account', 'state', 'description', 'reconciled', 'currency', 'amount', 'accounting_type']


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display=['id','account_number', 'name', 'default_accounting_type']

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display=['id','currency_code', 'name']

