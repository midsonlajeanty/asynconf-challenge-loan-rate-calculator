import random
from django.db import IntegrityError
from django.test import TestCase
from django.core.exceptions import ValidationError

from simulator.models.vehicle_type import VehicleType, FIXTURES

class VehicleTypeModelTestCase(TestCase):
    def setUp(self):
        self.vehicle_type_citadine = VehicleType.objects.get(name="Citadine")

    def test_vehicle_type_meta_options(self):
        self.assertEqual(VehicleType._meta.db_table, 'vehicle_types')

    def test_vehicle_type_post_migrate_receiver(self):
        self.assertEqual(VehicleType.objects.count(), len(FIXTURES))

    def test_vehicle_type_str_representation(self):
        self.assertEqual(str(self.vehicle_type_citadine), "Citadine - 8000-1300kg")

    def test_vehicle_type_fixture_data(self):
        vehicle_type_berline = VehicleType.objects.get(name="Berline")
        self.assertEqual(vehicle_type_berline.note, 6.5)

    def test_vehicle_type_creation(self):
        new_vehicle_type = VehicleType.objects.create(name="SUV", medium_weight="2000-2500", note=7)
        self.assertEqual(new_vehicle_type.note, 7)
        self.assertEqual(new_vehicle_type.medium_weight, "2000-2500")

    def test_unique_name_constraint(self):
        with self.assertRaises(IntegrityError):
            VehicleType.objects.create(name="Berline", medium_weight="2023-2600", note=random.randint(1, 10))

    def test_vehicle_type_update(self):
        self.vehicle_type_citadine.note = 7
        self.vehicle_type_citadine.save()
        updated_vehicle_type = VehicleType.objects.get(name="Citadine")
        self.assertEqual(updated_vehicle_type.note, 7)
