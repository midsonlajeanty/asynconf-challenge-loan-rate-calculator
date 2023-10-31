from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .base import BaseModel

# Fixtures
FIXTURES = [
    {
        "name": "Essence",
        "note": 5
    },
    {
        "name": "Electrique",
        "note": 9
    },
    {
        "name": "Gaz",
        "note": 6
    },
    {
        "name": "Diesel",
        "note": 4
    },
    {
        "name": "Hybride",
        "note": 7
    }
]


class Energy(BaseModel):

    class Meta:
        db_table = 'energies'
        verbose_name_plural = _('Energies')


# Signal(S)
def energy_post_migrate_receiver(sender, **kwargs):
    for item in FIXTURES:
        Energy.objects.get_or_create(
            **item
        )


#  ModelAdmin
class EnergyAdmin(admin.ModelAdmin):
    list_display = ['name', "note"]
