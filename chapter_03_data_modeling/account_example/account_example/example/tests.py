from django.test import TestCase

# Create your tests here.
from example.models import Log, Account


class AccountTestCase(TestCase):

    def test_operation(self):
        account1 = Account(account_number=1, amount=100)
        account2 = Account(account_number=2, amount=100)

        account2.lodge(source_account=account1, amount=50)

        self.assertEqual(account1.amount, 50)
        self.assertEqual(account2.amount, 150)

    def test_operation2(self):
        account1 = Account(account_number=3, amount=100)
        account2 = Account(account_number=4, amount=100)

        account2.withdraw(dest_account=account1, amount=50)

        self.assertEqual(account1.amount, 150)
        self.assertEqual(account2.amount, 50)

    def test_logs(self):
        account1 = Account(account_number=5, amount=100)
        account2 = Account(account_number=6, amount=100)

        account2.withdraw(dest_account=account1, amount=50)

        self.assertEqual(account1.amount, 150)
        self.assertEqual(account2.amount, 50)

        print(Log.objects.all())
        # breakpoint()
        # assert False
