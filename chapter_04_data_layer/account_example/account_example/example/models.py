from django.db import models
from django.db import transaction


# Create your models here.
class InternalAccount(models.Model):
    ''' This is the model related to a DB table '''
    account_number = models.IntegerField(unique=True)
    initial_amount = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    branch_id = models.IntegerField()

    def recalculate(self):
        '''
        Calculate the amount
        '''
        total_credit = sum(log.amount for log in self.credit.all())
        total_debit = sum(log.amount for log in self.debit.all())
        return self.initial_amount + total_credit - total_debit


class Log(models.Model):
    ''' This models stores the operations '''
    source = models.ForeignKey('InternalAccount',
                               related_name='debit',
                               on_delete=models.CASCADE)
    destination = models.ForeignKey('InternalAccount',
                                    related_name='credit',
                                    on_delete=models.CASCADE)
    amount = models.IntegerField()

    def commit(self):
        ''' this produces the operation '''
        with transaction.atomic():
            # Update the amounts
            self.source.amount -= self.amount
            self.destination.amount += self.amount
            # save everything
            self.source.save()
            self.destination.save()
            self.save()


class Account(object):
    ''' This is the exposed object that handled the operations '''

    def __init__(self, account_number, amount=0):
        '''
        To initialisation
        '''
        self.internal, _ = InternalAccount.objects.get_or_create(
            account_number=account_number,
            initial_amount=amount,
            amount=amount)

    @property
    def amount(self):
        return self.internal.amount

    def lodge(self, source_account, amount):
        '''
        This operation adds funds from the source
        '''
        log = Log(source=source_account.internal, destination=self.internal,
                  amount=amount)
        log.commit()

    def withdraw(self, dest_account, amount):
        '''
        This operation transfer funds to the destination
        '''
        log = Log(source=self.internal, destination=dest_account.internal,
                  amount=amount)
        log.commit()
