from .models.year import Year
from .models.energy import Energy
from .models.mileage import Mileage
from .models.loan_rate import LoanRate
from .models.vehicle_type import VehicleType
from .models.loan_rate_ajustement import LoanRateAjustement

def validate_data(data:dict) -> tuple[bool, object]:
    errors = {}

    if 'year' not in data.keys():
        errors.update({'year': 'L\'année n\'est pas renseignée'})
        return False, errors
    
    year = Year.objects.filter(id=data['year']).first()
    if year == None:
        errors.update({'year': 'L\'année n\'est pas valide'})
        return False, errors

    if 'energy' not in data.keys():
        errors.update({'energy': 'L\'énergie n\'est pas renseignée'})
        return False, errors
    
    energy =Energy.objects.filter(id=data['energy']).first()
    if energy == None:
        errors.update({'energy': 'L\'énergie n\'est pas valide'})
        return False, errors
    
    if 'mileage' not in data.keys():
        errors.update({'mileage': 'Le kilométrage n\'est pas renseigné'})
        return False, errors
    
    mileage = Mileage.objects.filter(id=data['mileage']).first()
    if mileage == None:
        errors.update({'mileage': 'Le kilométrage n\'est pas valide'})
        return False, errors
    
    if 'vehicle_type' not in data.keys():
        errors.update({'vehicle_type': 'Le type de véhicule n\'est pas renseigné'})
        return False, errors
    
    vehicle_type = VehicleType.objects.filter(id=data['vehicle_type']).first()
    if vehicle_type == None:
        errors.update({'vehicle_type': 'Le type de véhicule n\'est pas valide'})
        return False, errors
    
    if 'ajustement' not in data.keys():
        errors.update({'ajustement': 'Le nombre de personne n\'est pas renseigné'})
        return False, errors
    
    ajustement = LoanRateAjustement.objects.filter(id=data['ajustement']).first()
    if ajustement == None:
        errors.update({'ajustement': 'L\'nombre de personne selectionné n\'est pas valide'})
        return False, errors

    return True, (year, energy, mileage, vehicle_type, ajustement)