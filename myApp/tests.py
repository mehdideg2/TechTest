from django.test import TestCase
from .models import Investment
from django.test.utils import setup_test_environment


class InvestmentModelTests(TestCase):
    def investment_false_date(self):   # TODO: complete
        """ test if investment model is good"""
        new_investment = Investment()
        self.assertIs(new_investment.check(), False)
