from django.db import models
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone


class JournalEnteryLines(models.Model):

    accounting_date = models.DateField() 
    account = models.CharField(max_length=255, unique=True)
    state = models.CharField(max_length=255, blank=False)
    description = models.CharField(max_length=255)
    reconciled = models.BooleanField(default=False)
    currency = models.CharField(max_length=6, blank=False)
    amount =models.IntegerField()
    accounting_type = models.CharField(max_length=6, blank=False)
    
    def __str__(self):
        return str(self.id)


    
class Account(models.Model):
    account_number = models.CharField(max_length=4, unique=True, blank=False, validators=[RegexValidator(r'^\d{4}$', 'Account number must be exactly 4 digits')])
    name = models.CharField(max_length=255, blank=False)
    default_accounting_type = models.CharField(max_length=6, blank=False)
    
    def __str__(self):
        return str(self.name)


class Currency(models.Model):
    currency_code = models.CharField(max_length=3, blank=False)
    name = models.CharField(max_length=255, blank=False)
    
    def __str__(self):
        return str(self.name)
    
    