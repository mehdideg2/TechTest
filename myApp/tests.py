from django.test import TestCase
from .models import Investment


class InvestmentModelTests(TestCase):
    def investment_false_date(self):   # TODO: complete
        """ not a test """
        new_investment = Investment()
        self.assertIs(new_investment.check(), False)
