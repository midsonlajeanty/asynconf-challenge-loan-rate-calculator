from django.test import TestCase
from django.urls import reverse

from simulator.models.year import Year, FIXTURES as YEAR_FIXTURES
from simulator.models.energy import Energy, FIXTURES as ENERGY_FIXTURES
from simulator.models.mileage import Mileage, FIXTURES as MILEAGE_FIXTURES
from simulator.models.vehicle_type import VehicleType, FIXTURES as VEHICLE_TYPE_FIXTURES
from simulator.models.loan_rate_ajustement import LoanRateAjustement, FIXTURES as LOAN_RATE_AJUSTEMENT_FIXTURES


class IndexViewTestCase(TestCase):
    def test_index_view_uses_correct_template(self):
        response = self.client.get(reverse('index'))
        self.assertTemplateUsed(response, 'simulator/index.html')

    def test_index_view_context_data(self):
        response = self.client.get(reverse('index'))
        
        self.assertEqual(len(response.context['years']), len(YEAR_FIXTURES))
        self.assertEqual(len(response.context['energies']), len(ENERGY_FIXTURES))
        self.assertEqual(len(response.context['mileages']), len(MILEAGE_FIXTURES))
        self.assertEqual(len(response.context['vehicle_types']), len(VEHICLE_TYPE_FIXTURES))
        self.assertEqual(len(response.context['loan_rates_adjustments']), len(LOAN_RATE_AJUSTEMENT_FIXTURES))

    def test_index_view_context_data_empty(self):
        Year.objects.all().delete()
        Energy.objects.all().delete()
        Mileage.objects.all().delete()
        VehicleType.objects.all().delete()
        LoanRateAjustement.objects.all().delete()
        
        response = self.client.get(reverse('index'))

        self.assertEqual(len(response.context['years']), 0)
        self.assertEqual(len(response.context['energies']), 0)
        self.assertEqual(len(response.context['mileages']), 0)
        self.assertEqual(len(response.context['vehicle_types']), 0)
        self.assertEqual(len(response.context['loan_rates_adjustments']), 0)
