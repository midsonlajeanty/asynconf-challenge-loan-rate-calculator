from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.utils.deconstruct import deconstructible

from .base import BaseModel


# Fixtures
FIXTURES = [
    {
        "name": "Citadine",
        "medium_weight": "8000-1300",
        "note": 8
    },
    {
        "name": "Cabriolet",
        "medium_weight": "1300-2000",
        "note": 6
    },
    {
        "name": "Berline",
        "medium_weight": "1300-1800",
        "note": 6.5
    },
    {
        "name": "SUV / 4x4",
        "medium_weight": "1500-2500",
        "note": 4.10
    }
]


# Helper(s)
@deconstructible
class MediumWeightValidator(RegexValidator):
    regex = r'^\d-\d$'


# Model
class VehicleType(BaseModel):

    class Meta:
        db_table = 'vehicle_types'

    medium_weight = models.CharField(
        _('Medium weight'),
        max_length=20,
        validators=[MediumWeightValidator()]
    )

    @property
    def display_medium_weight(self):
        return self.medium_weight + "kg"

    def __str__(self):
        return "%s - %s" % (self.name, self.display_medium_weight)


# Signal(S)
def vehicle_type_post_migrate_receiver(sender, **kwargs):
    for item in FIXTURES:
        VehicleType.objects.get_or_create(
            **item
        )


#  ModelAdmin
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_medium_weight', "note"]
