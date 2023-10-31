# Generated by Django 4.2.6 on 2023-10-31 03:59

import django.core.validators
from django.db import migrations, models
import simulator.models.vehicle_type


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Energy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Name')),
                ('note', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Note')),
            ],
            options={
                'verbose_name_plural': 'Energies',
                'db_table': 'energies',
            },
        ),
        migrations.CreateModel(
            name='LoanRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_from', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Score From')),
                ('score_to', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Score To')),
                ('rate', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Rate')),
            ],
            options={
                'db_table': 'loan_rates',
            },
        ),
        migrations.CreateModel(
            name='LoanRateAjustement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nb_passenger', models.IntegerField(unique=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(4)], verbose_name='Nb Passengers')),
                ('type', models.CharField(choices=[('bonus', 'Bonus'), ('penalty', 'Penalty')], max_length=200, verbose_name='Type')),
                ('rate', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)], verbose_name='Rate')),
            ],
            options={
                'db_table': 'loan_rate_ajustements',
            },
        ),
        migrations.CreateModel(
            name='Mileage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Name')),
                ('note', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Note')),
            ],
            options={
                'db_table': 'mileages',
            },
        ),
        migrations.CreateModel(
            name='VehicleType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Name')),
                ('note', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Note')),
                ('medium_weight', models.CharField(max_length=20, validators=[simulator.models.vehicle_type.MediumWeightValidator()], verbose_name='Medium weight')),
            ],
            options={
                'db_table': 'vehicle_types',
            },
        ),
        migrations.CreateModel(
            name='Year',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='Name')),
                ('note', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)], verbose_name='Note')),
            ],
            options={
                'db_table': 'years',
            },
        ),
        migrations.AddConstraint(
            model_name='loanrate',
            constraint=models.UniqueConstraint(fields=('score_from', 'score_to'), name='unique_from_to_score'),
        ),
    ]