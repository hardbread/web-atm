from decimal import Decimal
from django.db import models


class Card(models.Model):
    card_id = models.CharField('Card id', max_length=16, unique=True, blank=True)
    pin = models.IntegerField('Pin code', blank=True)
    is_active = models.BooleanField('Card status', default=True)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default=Decimal(0))

    class Meta:
        db_table = u'card'
        verbose_name = "Card"


class CardOperation(models.Model):
    _operation_codes = {
        'balance': 1,
        'withdrawal': 2
    }

    card = models.ForeignKey(Card)
    _operation = models.IntegerField('Pin code', blank=True)
    operation_time = models.DateTimeField('Operation time', auto_now=True)
    amount = models.DecimalField('Amount', max_digits=8, decimal_places=2, default=Decimal(0))

    class Meta:
        db_table = u'card_operations'
        verbose_name = "Card operations"

    @property
    def operation(self):
        return self.get_operation_by_code(self._operation)

    @operation.setter
    def operation(self, key):
        self._operation = self.get_operation_by_key(key)
        print None

    @classmethod
    def get_operation_by_code(cls, code):
        return next((k for k, v in cls._operation_codes.items() if v == code), None)

    @classmethod
    def get_operation_by_key(cls, key):
        return cls._operation_codes.get(key)