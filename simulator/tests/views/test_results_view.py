import json
from django.test import TestCase
from django.urls import reverse

from simulator.models.year import Year
from simulator.models.energy import Energy
from simulator.models.mileage import Mileage
from simulator.models.vehicle_type import VehicleType
from simulator.models.loan_rate_ajustement import LoanRateAjustement
from simulator.models.loan_rate import LoanRate

class ResultsViewTestCase(TestCase):
    def test_results_view_with_valid_data(self):
        data = {
            "year": Year.objects.filter(name='2000-2010').first().id,
            "energy": Energy.objects.filter(name='Electrique').first().id,
            "mileage": Mileage.objects.filter(name='20-25').first().id,
            "vehicle_type": VehicleType.objects.filter(name='Citadine').first().id,
            "ajustement": LoanRateAjustement.objects.filter(nb_passenger=1).first().id
        }

        response = self.client.post(
            reverse('results'), 
            json.dumps(data), 
            content_type='application/json', 
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )

        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.content.decode('utf-8'))

        self.assertEqual(json_response['status'], 'success')
        self.assertEqual(json_response['message'], 'Les données envoyées sont valides')
        self.assertEqual(json_response['data']['rate'], 2.63)

    def test_results_view_with_invalid_data(self):
        data = {
            "year": Year.objects.filter(name='2000-2010').first().id,
            "energy": Energy.objects.filter(name='Electrique').first().id,
            "mileage": Mileage.objects.filter(name='20-25').first().id,
            "vehicle_type": VehicleType.objects.filter(name='Citadine').first().id,
            "ajustement": 20
        }
        response = self.client.post(
            reverse('results'), 
            json.dumps(data), 
            content_type='application/json', 
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )

        self.assertEqual(response.status_code, 400)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['status'], 'error')
        self.assertEqual(json_response['message'], 'Les données envoyées sont invalides')
        self.assertIn('ajustement', json_response['errors'])

    def test_results_view_with_no_loan_rate(self):
        data = {
            "year": Year.objects.filter(name='2000-2010').first().id,
            "energy": Energy.objects.filter(name='Electrique').first().id,
            "mileage": Mileage.objects.filter(name='20-25').first().id,
            "vehicle_type": VehicleType.objects.filter(name='Citadine').first().id,
            "ajustement": LoanRateAjustement.objects.filter(nb_passenger=1).first().id
        }

        LoanRate.objects.all().delete()

        response = self.client.post(
            reverse('results'), 
            json.dumps(data), 
            content_type='application/json', 
            HTTP_X_REQUESTED_WITH='XMLHttpRequest'
        )

        self.assertEqual(response.status_code, 404)
        json_response = json.loads(response.content.decode('utf-8'))
        self.assertEqual(json_response['status'], 'error')
        self.assertEqual(json_response['message'], "Le taux de prêt n'est pas disponible")

    def test_results_view_with_no_post_request(self):
        response = self.client.get(reverse('results'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('index'))