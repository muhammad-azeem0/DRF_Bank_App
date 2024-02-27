
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from .models import JournalEnteryLines, Account, Currency


class AccountTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.account_url = reverse('account-list')
        
        self.valid_payload = {
            'account_number':'1234',
            'name': 'Ali',
            'default_accounting_type': 'Debit'
        }
        self.invalid_payload = {
            'account_number':'1934',
            'name': '',
            'default_accounting_type': 'Debit'
        }
        self.valid_entery = Account.objects.create(
            account_number = '1654',
            name = 'Hammad',
            default_accounting_type = 'Credit'
        )
        
        
        
    def test_create_valid_account(self):
        response = self.client.post(self.account_url, data=self.valid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        
    def test_create_invalid_account(self):
        response = self.client.post(self.account_url, data=self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        
        
    def test_retrieve_account_list(self):
        response = self.client.get(self.account_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
      
      
    def test_retrieve_specific_account(self):
        account_detail_url = reverse('account-detail', kwargs={'pk': self.valid_entery.pk})
        response = self.client.get(account_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    
    def test_delete_account(self):
        self.delete_account_url = reverse('account-detail', kwargs={'pk': self.valid_entery.pk})
        response = self.client.delete(self.delete_account_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)    

        
#---------------------------------------------------------------------------------------------------------------------------------

class JournalTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.journal_url = reverse('journal-list')
        self.valid_payload = {
            'accounting_date': '2024-02-22',
            'account': 'Sample Account',
            'state': 'Sample State',
            'description': 'Sample Description',
            'reconciled': False,
            'currency': 'USD',
            'amount': 100,
            'accounting_type': 'Debit'
        }
        self.invalid_payload = {
            'accounting_date': '2024-02-22',
            'account': '',  # Invalid: Account field is required
            'state': 'Sample State',
            'description': 'Sample Description',
            'reconciled': False,
            'currency': 'USD',
            'amount': 100,
            'accounting_type': 'Debit'
        }
        # Creating a valid payload object
        self.valid_entry = JournalEnteryLines.objects.create(
            accounting_date='2024-02-22',
            account='Unique Account',
            state='Sample State',
            description='Sample Description',
            reconciled=False,
            currency='USD',
            amount=100,
            accounting_type='Debit'
        )

    def test_create_valid_journal(self):
        response = self.client.post(self.journal_url, data=self.valid_payload, format='json')
        print("Response ======================> ", response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_journal(self):
        response = self.client.post(self.journal_url, data=self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_journal_list(self):
        response = self.client.get(self.journal_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

      
    def test_retrieve_specific_journal(self):
        response = self.client.get(reverse('journal-detail', kwargs={'pk': self.valid_entry.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_journal(self):
        self.delete_journal_url = reverse('journal-detail', kwargs={'pk': self.valid_entry.pk})
        response = self.client.delete(self.delete_journal_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)    


#---------------------------------------------------------------------------------------------------------------------------------



class CurrencyTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.currency_url = reverse('currency-list')
        
        self.valid_payload = {
            'currency_code':'INR',
            'name' :'Ans'
        }
        self.invalid_payload = {
            'currency_code':'USD',
            'name' :''
        }

        self.valid_entry = Currency.objects.create(
            currency_code='PKR',
            name='Azeem'
        )

    def test_create_valid_currency(self):
        response = self.client.post(self.currency_url, data=self.valid_payload, format='json')
        print("Response ======================> ", response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_currency(self):
        response = self.client.post(self.currency_url, data=self.invalid_payload, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_currency_list(self):
        response = self.client.get(self.currency_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

      
    def test_retrieve_specific_currency(self):
        response = self.client.get(reverse('currency-detail', kwargs={'pk': self.valid_entry.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_delete_journal(self):
        print("==================> Delete specific Currency test")
        self.delete_currency_url = reverse('currency-detail', kwargs={'pk': self.valid_entry.pk})
        response = self.client.delete(self.delete_currency_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT) 
        
#---------------------------------------------------------------------------------------------------------------------------------