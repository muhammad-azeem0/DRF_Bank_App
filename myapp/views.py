from rest_framework import generics
from rest_framework.response import Response
from .models import JournalEnteryLines, Account, Currency
from .serializers import JournalSerializer, AccountSerializer, CurrencySerializer

# Second Commit

# Views for JournalEnteryLines model
class JournalListCreate(generics.ListCreateAPIView):
    queryset = JournalEnteryLines.objects.all()
    serializer_class = JournalSerializer


class JournalRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = JournalEnteryLines.objects.all()
    serializer_class = JournalSerializer



# Views for Account model
class AccountListCreate(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    
    
class AccountRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


# Views for Currency model
class CurrencyListCreate(generics.ListCreateAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class CurrencyRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
