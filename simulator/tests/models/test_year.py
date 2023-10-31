import random
from django.db import IntegrityError
from django.test import TestCase

from simulator.models.year import Year, FIXTURES

class YearModelTestCase(TestCase):

    def setUp(self):
        self.year_1960_1970 = Year.objects.get(name="1960-1970")

    def test_year_meta_options(self):
        self.assertEqual(Year._meta.db_table, 'years')

    def test_year_post_migrate_receiver(self):
        self.assertEqual(Year.objects.count(), len(FIXTURES))

    def test_year_str_representation(self):
        self.assertEqual(str(self.year_1960_1970), "1960-1970")

    def test_year_fixture_data(self):
        year_after_2010 = Year.objects.get(name="Après 2010")
        self.assertEqual(year_after_2010.note, 7)

    def test_year_creation(self):
        new_year = Year.objects.create(name="2020-2030", note=8)
        self.assertEqual(new_year.note, 8)

    def test_unique_name_constraint(self):
        with self.assertRaises(IntegrityError):
            Year.objects.create(name="1960-1970", note=random.randint(1, 10))

    def test_year_update(self):
        self.year_1960_1970.note = 3
        self.year_1960_1970.save(update_fields=['note'])
        updated_year = Year.objects.get(name="1960-1970")
        self.assertEqual(updated_year.note, 3)