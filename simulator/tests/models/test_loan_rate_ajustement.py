from django.db import IntegrityError
from django.test import TestCase
from django.core.exceptions import ValidationError
from simulator.models.loan_rate_ajustement import LoanRateAjustement, FIXTURES

class LoanRateAjustementModelTestCase(TestCase):
    def setUp(self):
        self.ajustement_1 = LoanRateAjustement.objects.get(nb_passenger=1)

    def test_ajustement_meta_options(self):
        self.assertEqual(LoanRateAjustement._meta.db_table, 'loan_rate_ajustements')

    def test_loan_rate_post_migrate_receiver(self):
        self.assertEqual(LoanRateAjustement.objects.count(), len(FIXTURES))

    def test_ajustement_str_representation(self):
        self.assertEqual(str(self.ajustement_1), "x1 | +0.11%")

    def test_ajustement_fixture_data(self):
        ajustement_3 = LoanRateAjustement.objects.get(nb_passenger=3, type='penalty')
        self.assertEqual(ajustement_3.rate, 0.29)

    def test_ajustement_creation(self):
        new_ajustement = LoanRateAjustement.objects.create(nb_passenger=5, type='penalty', rate=0.53)
        self.assertEqual(new_ajustement.rate, 0.53)

    def test_ajustement_update(self):
        self.ajustement_1.rate = 0.15
        self.ajustement_1.save()
        updated_ajustement = LoanRateAjustement.objects.get(nb_passenger=1, type='bonus')
        self.assertEqual(updated_ajustement.rate, 0.15)
