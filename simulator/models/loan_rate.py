from django.db import models
from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator
from .base import note_validator

# Fixtures
FIXTURES = [
    {
        "score_from": 0,
        "score_to": 10.99,
        "rate": 3
    },
    {
        "score_from": 11,
        "score_to": 15.99,
        "rate": 2.74
    },
    {
        "score_from": 16,
        "score_to": 25.99,
        "rate": 2.52
    },
    {
        "score_from": 26,
        "score_to": 33.99,
        "rate": 2.10
    },
    {
        "score_from": 34,
        "score_to": 40,
        "rate": 1.85
    },
]


class LoanRate(models.Model):

    class Meta:
        db_table = 'loan_rates'
        constraints = [
            models.UniqueConstraint(
                fields=['score_from', 'score_to'],
                name='unique_from_to_score'
            )
        ]

    score_from = models.FloatField(
        _("Score From"),
        validators=note_validator,
    )

    score_to = models.FloatField(
        _("Score To"),
        validators=note_validator,
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
        return "%s - %s" % (self.score_from, self.score_to)
    
    @property
    def display_rate(self):
        return "%s%%" % self.rate
    
    def __str__(self) -> str:
        return self.display_name + " | " + self.display_rate


# Signal(S)
def loan_rate_post_migrate_receiver(sender, **kwargs):
    for item in FIXTURES:
        LoanRate.objects.get_or_create(
            **item
        )


#  ModelAdmin
class LoanRateAdmin(admin.ModelAdmin):
    list_display = ['display_name', "display_rate"]
