from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import JournalListCreate, JournalRetrieveUpdateDestroy, AccountListCreate, AccountRetrieveUpdateDestroy, CurrencyListCreate, CurrencyRetrieveUpdateDestroy
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Bank API",
        default_version='v1',
        description="Test description",
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    
    path('journal/', JournalListCreate.as_view(), name='journal-list'),
    path('journal/<int:pk>/', JournalRetrieveUpdateDestroy.as_view(), name='journal-detail'),
    
    path('account/', AccountListCreate.as_view(), name='account-list'),
    path('account/<int:pk>/', AccountRetrieveUpdateDestroy.as_view(), name='account-detail'),
    
    path('currency/', CurrencyListCreate.as_view(), name='currency-list'),
    path('currency/<int:pk>/', CurrencyRetrieveUpdateDestroy.as_view(), name='currency-detail'),
]

