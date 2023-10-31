import random
from django.db import IntegrityError
from django.test import TestCase
from simulator.models.mileage import Mileage, FIXTURES

class MileageModelTestCase(TestCase):
    def setUp(self):
        self.mileage_5_10 = Mileage.objects.get(name="5-10")

    def test_mileage_meta_options(self):
        self.assertEqual(Mileage._meta.db_table, 'mileages')

    def test_mileage_post_migrate_receiver(self):
        self.assertEqual(Mileage.objects.count(), len(FIXTURES))

    def test_mileage_str_representation(self):
        self.assertEqual(str(self.mileage_5_10), "5-10K/km")

    def test_mileage_display_name_property(self):
        self.assertEqual(self.mileage_5_10.display_name, "5-10K/km")

    def test_mileage_fixture_data(self):
        mileage_25_30 = Mileage.objects.get(name="25-30")
        self.assertEqual(mileage_25_30.note, 1)

    def test_mileage_creation(self):
        new_mileage = Mileage.objects.create(name="30-35", note=8)
        self.assertEqual(new_mileage.note, 8)

    def test_unique_name_constraint(self):
        with self.assertRaises(IntegrityError):
            Mileage.objects.create(name="5-10", note=random.randint(1, 10))

    def test_mileage_update(self):
        self.mileage_5_10.note = 23
        self.mileage_5_10.save()
        updated_mileage = Mileage.objects.get(name="5-10")
        self.assertEqual(updated_mileage.note, 23)
