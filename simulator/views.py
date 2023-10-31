import json
from django.http import JsonResponse
from django.shortcuts import redirect, render

from .utils import validate_data

from .models.year import Year
from .models.energy import Energy
from .models.mileage import Mileage
from .models.loan_rate import LoanRate
from .models.vehicle_type import VehicleType
from .models.loan_rate_ajustement import LoanRateAjustement


# Create your views here.
def index(request):

    # Get all years
    years = Year.objects.all()

    # Get all energy types
    energies = Energy.objects.all()

    # Get all mileage types
    mileages = Mileage.objects.all()

    # Get all vehicle types
    vehicle_types = VehicleType.objects.all()

    # Get all loan adjustments rates
    loan_rates_adjustments = LoanRateAjustement.objects.all()

    return render(
        request,
        template_name='simulator/index.html',
        context={
            'years': years,
            'energies': energies,
            'mileages': mileages,
            'vehicle_types': vehicle_types,
            'loan_rates_adjustments': loan_rates_adjustments
        }
    )


def results(request):
    if (request.method != 'POST') or not request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        return redirect('index')
    else:
        data: dict = json.load(request)

        valid, data_or_error = validate_data(data)
        if not valid:
            json_data = {
                'status': 'error',
                'message': 'Les données envoyées sont invalides',
                'errors': data_or_error
            }
            return JsonResponse(json_data, status=400)

        year, energy, mileage, vehicle_type, ajustement = data_or_error

        # Calculate Total Note
        total_note = year.note + energy.note + mileage.note + vehicle_type.note

        loan_rate = LoanRate.objects.filter(
            score_from__lte=total_note,
            score_to__gte=total_note
        ).first()

        if loan_rate == None:
            json_data = {
                'status': 'error',
                'message': 'Le taux de prêt n\'est pas disponible'
            }
            return JsonResponse(json_data, status=404)

        rate = loan_rate.rate
        if ajustement.type == 'bonus':
            rate += ajustement.rate
        else:
            rate -= ajustement.rate

        json_data = {
            'status': 'success',
            'message': 'Les données envoyées sont valides',
            'data': {
                'rate': round(rate, 2)
            }
        }

        return JsonResponse(json_data, status=200)
