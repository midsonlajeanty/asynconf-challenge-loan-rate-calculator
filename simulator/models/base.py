from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator


note_validator = [
    MinValueValidator(1),
    MaxValueValidator(10)
]


# Create your models here.
class BaseModel(models.Model):

    class Meta:
        abstract = True

    name = models.CharField(
        _('Name'),
        max_length=200,
        unique=True
    )

    note = models.FloatField(
        _('Note'),
        validators=note_validator
    )

    def __str__(self):
        return self.name
