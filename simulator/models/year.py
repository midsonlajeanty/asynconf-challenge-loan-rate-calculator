from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .base import BaseModel

# Fixtures
FIXTURES = [
    {
        "name": "1960-1970",
        "note": 1
    },
    {
        "name": "1970-1980",
        "note": 2
    },
    {
        "name": "1990-2000",
        "note": 4
    },
    {
        "name": "2000-2010",
        "note": 5
    },
    {
        "name": "Après 2010",
        "note": 7
    }
]


class Year(BaseModel):

    class Meta:
        db_table = 'years'

    def __str__(self) -> str:
        return self.name


# Signal(S)
def year_post_migrate_receiver(sender, **kwargs):
    for item in FIXTURES:
        Year.objects.get_or_create(
            **item
        )


#  ModelAdmin
class YearAdmin(admin.ModelAdmin):
    list_display = ['name', "note"]
