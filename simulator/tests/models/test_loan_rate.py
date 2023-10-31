from django.db import IntegrityError
from django.test import TestCase
from django.core.exceptions import ValidationError

from simulator.models.loan_rate import LoanRate, FIXTURES

class LoanRateModelTestCase(TestCase):
    def setUp(self):
        self.loan_rate_0_10 = LoanRate.objects.get(score_from=0, score_to=10.99)

    def test_loan_rate_meta_options(self):
        self.assertEqual(LoanRate._meta.db_table, 'loan_rates')

    def test_loan_rate_post_migrate_receiver(self):
        self.assertEqual(LoanRate.objects.count(), len(FIXTURES))

    def test_loan_rate_str_representation(self):
        self.assertEqual(str(self.loan_rate_0_10), "0.0 - 10.99 | 3.0%")

    def test_loan_rate_fixture_data(self):
        loan_rate_16_25 = LoanRate.objects.get(score_from=16, score_to=25.99)
        self.assertEqual(loan_rate_16_25.rate, 2.52)
    
    def test_loan_rate_creation(self):
        new_loan_rate = LoanRate.objects.create(score_from=41, score_to=49.99, rate=2.10)
        self.assertEqual(new_loan_rate.rate, 2.10)
        self.assertEqual(new_loan_rate.score_from, 41)
        self.assertEqual(new_loan_rate.score_to, 49.99)

    def test_loan_rate_unique_constraint(self):
        with self.assertRaises(IntegrityError):
            LoanRate.objects.create(score_from=0, score_to=10.99, rate=4)

    def test_loan_rate_update(self):
        self.loan_rate_0_10.rate = 2.5
        self.loan_rate_0_10.save()
        updated_loan_rate = LoanRate.objects.get(score_from=0, score_to=10.99)
        self.assertEqual(updated_loan_rate.rate, 2.5)
