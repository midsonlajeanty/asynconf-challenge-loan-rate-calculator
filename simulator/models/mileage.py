from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .base import BaseModel

# Fixtures
FIXTURES = [
    {
        "name": "5-10",
        "note": 9
    },
    {
        "name": "10-15",
        "note": 7
    },
    {
        "name": "15-20",
        "note": 5
    },
    {
        "name": "20-25",
        "note": 3
    },
    {
        "name": "25-30",
        "note": 1
    }
]


class Mileage(BaseModel):

    class Meta:
        db_table = 'mileages'

    @property
    def display_name(self):
        return self.name + "K/km"
    
    def __str__(self) -> str:
        return self.display_name


# Signal(S)
def mileage_post_migrate_receiver(sender, **kwargs):
    for item in FIXTURES:
        Mileage.objects.get_or_create(
            **item
        )


#  ModelAdmin
class MileageAdmin(admin.ModelAdmin):
    list_display = ['display_name', "note"]
