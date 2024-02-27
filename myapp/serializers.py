from rest_framework import serializers
from .models import JournalEnteryLines, Account, Currency


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = JournalEnteryLines
        fields = ['id', 'accounting_date', 'account', 'state', 'description', 'reconciled', 'currency', 'amount', 'accounting_type']


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['id','account_number', 'name', 'default_accounting_type']
        

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id','currency_code', 'name']