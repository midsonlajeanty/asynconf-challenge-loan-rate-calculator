from django.contrib import admin

from .models.year import Year, YearAdmin
from .models.energy import Energy, EnergyAdmin
from .models.mileage import Mileage, MileageAdmin
from .models.loan_rate import LoanRate, LoanRateAdmin
from .models.vehicle_type import VehicleType, VehicleTypeAdmin
from .models.loan_rate_ajustement import LoanRateAjustement, LoanRateAjustementAdmin


# Register ModelAdmin
admin.site.register(Year, YearAdmin)
admin.site.register(Energy, EnergyAdmin)
admin.site.register(Mileage, MileageAdmin)
admin.site.register(LoanRate, LoanRateAdmin)
admin.site.register(VehicleType, VehicleTypeAdmin)
admin.site.register(LoanRateAjustement, LoanRateAjustementAdmin)
