from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from .base import note_validator

# Fixtures
FIXTURES = [
    {
        "nb_passenger": 1,
        "type": 'bonus',
        "rate": 0.11
    },
    {
        "nb_passenger": 2,
        "type": "penalty",
        "rate": 0.17
    },
    {
        "nb_passenger": 3,
        "type": "penalty",
        "rate": 0.29
    },
    {
        "nb_passenger": 4,
        "type": "penalty",
        "rate": 0.53
    },
]


class LoanRateAjustement(models.Model):

    class Meta:
        db_table = 'loan_rate_ajustements'

    class AjustementType(models.TextChoices):
        BONUS = 'bonus', _('Bonus')
        MALUS = 'penalty', _('Penalty')

    nb_passenger = models.IntegerField(
        _("Nb Passengers"),
        unique=True,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(4)
        ],
    )

    type = models.CharField(
        _("Type"),
        max_length=200,
        choices=AjustementType.choices,
    )

    rate = models.FloatField(
        _("Rate"),
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ],
    )

    @property
    def display_name(self):
        return "x%s" % (self.nb_passenger)

    @property
    def display_rate(self):
        if self.type == self.AjustementType.BONUS:
            return "+%s%%" % self.rate
        else:
            return "-%s%%" % self.rate

    def __str__(self):
        return self.display_name + " | " + self.display_rate


# Signal(S)
def loan_rate_ajustement_post_migrate_receiver(sender, **kwargs):
    for item in FIXTURES:
        LoanRateAjustement.objects.get_or_create(
            **item
        )


#  ModelAdmin
class LoanRateAjustementAdmin(admin.ModelAdmin):
    list_display = ['display_name', "display_rate"]
