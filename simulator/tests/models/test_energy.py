import random
from django.db import IntegrityError
from django.test import TestCase
from simulator.models.energy import Energy, FIXTURES

class EnergyModelTestCase(TestCase):
    def setUp(self):
        self.energy_essence = Energy.objects.get(name="Essence")

    def test_energy_meta_options(self):
        self.assertEqual(Energy._meta.db_table, 'energies')
        self.assertEqual(Energy._meta.verbose_name_plural, 'Energies')

    def test_energy_post_migrate_receiver(self):
        self.assertEqual(Energy.objects.count(), len(FIXTURES))

    def test_energy_str_representation(self):
        self.assertEqual(str(self.energy_essence), "Essence")

    def test_energy_fixture_data(self):
        energy_hybride = Energy.objects.get(name="Hybride")
        self.assertEqual(energy_hybride.note, 7)

    def test_energy_creation(self):
        new_energy = Energy.objects.create(name="Nouvelle Energie", note=8)
        self.assertEqual(new_energy.note, 8)

    def test_unique_name_constraint(self):
        with self.assertRaises(IntegrityError):
            Energy.objects.create(name="Hybride", note=random.randint(1, 10))

    def test_energy_update(self):
        self.energy_essence.note = 12
        self.energy_essence.save()
        updated_energy = Energy.objects.get(name="Essence")
        self.assertEqual(updated_energy.note, 12)
