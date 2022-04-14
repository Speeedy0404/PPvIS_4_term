import unittest
from garden_area import *


class TestSeedBedAndOrchard(unittest.TestCase):

    def test_presence_objects_in_seed_bed(self):
        test = SeedBed()
        name = ["Морковка", "Свекла", "Редиска"]
        length = len(name)
        iterator = 0
        for i in name:
            test.new_object(i, 0)
            self.assertEqual(i, SeedBed.objects_in_garden(iterator, 0))
            iterator += 1
        for i in range(0, length):
            SeedBed.deleting_information(0, param=0)

    def test_presence_objects_in_orchard(self):
        test = Orchard()
        name = ["Груша", "Вишня", "Яблоня"]
        length = len(name)
        iterator = 0
        for i in name:
            test.new_object(i, 1)
            self.assertEqual(i, Orchard.objects_in_garden(iterator, 1))
            iterator += 1
        for i in range(0, length):
            Orchard.deleting_information(0, param=1)

    def test_check_conditions_seed_bed(self):
        test = SeedBed()
        test.new_object("Морковка", 0)
        self.assertEqual(0, SeedBed.check_weeds(0))
        self.assertEqual(0, SeedBed.check_illness(0, 0))
        self.assertEqual(0, SeedBed.check_vermin(0, 0))
        SeedBed.deleting_information(0, 0)

    def test_check_conditions_orchard(self):
        test = Orchard()
        test.new_object("Груша", 1)
        self.assertEqual(0, SeedBed.check_illness(0, 1))
        self.assertEqual(0, SeedBed.check_vermin(0, 1))
        SeedBed.deleting_information(0, 1)

    def test_water_height_seed_bed(self):
        test = SeedBed()
        test.new_object("Морковка", 0)
        self.assertEqual(0, SeedBed.check_level_of_water(0, 0))
        self.assertEqual("Первые 2-3 настоящих листа", SeedBed.check_height(0, 0))
        SeedBed.deleting_information(0, 0)

    def test_water_height_orchard(self):
        test = Orchard()
        test.new_object("Груша", 1)
        self.assertEqual(0, Orchard.check_level_of_water(0, 1))
        self.assertEqual("Семечко в земле", Orchard.check_height(0, 1))
        Orchard.deleting_information(0, 1)

    def test_array_names_seed_bed(self):
        way = "vegetables_in_garden.txt"
        test = SeedBed()
        name = ["Морковка", "Свекла", "Редиска"]
        length = len(name)
        iterator = 0
        for i in name:
            test.new_object(i, 0)
            self.assertIn(name[iterator], SeedBed.names(way))
            iterator += 1
        for i in range(0, length):
            SeedBed.deleting_information(0, param=0)

    def test_array_names_orchard(self):
        way = "fruits_in_garden.txt"
        test = Orchard()
        name = ["Груша", "Вишня", "Яблоня"]
        length = len(name)
        iterator = 0
        for i in name:
            test.new_object(i, 1)
            self.assertIn(name[iterator], Orchard.names(way))
            iterator += 1
        for i in range(0, length):
            Orchard.deleting_information(0, param=1)


class TestPoorConditions(unittest.TestCase):

    def test_info_and_changing_illness(self):
        message = "Все хорошо, никаких болезней"
        illness = Illness(name='Test', creation=1, param=0)
        self.assertEqual(message, illness.info_condition)
        for i in range(0, 20):
            illness.changing_condition(param=0)
        self.assertNotEqual(message, illness.info_condition)
        illness.del_condition(0)

    def test_info_and_changing_vermin(self):
        message = "Все хорошо, никаких вредителей"
        vermin = Vermin(name='Test', creation=1, param=1)
        self.assertEqual(message, vermin.info_condition)
        for i in range(0, 20):
            vermin.changing_condition(param=1)
        self.assertNotEqual(message, vermin.info_condition)
        vermin.del_condition(1)

    def test_info_and_changing_weeds(self):
        message = "Все хорошо, никаких сорняков"
        weeds = Weeds(name='Test', creation=1, param=1)
        self.assertEqual(message, weeds.info_condition)
        for i in range(0, 20):
            weeds.changing_condition(param=1)
        self.assertNotEqual(message, weeds.info_condition)
        weeds.del_condition(1)


class TestVegetablesFruits(unittest.TestCase):

    def test_day_today_level_change_and_regeneration_hp_vegetables(self):
        vegetable = Vegetables("Морковка", 1, 0)
        self.assertEqual(0, vegetable.day_today)
        self.assertNotEqual(10, vegetable.info_lever_of_hp)
        for i in range(0, 3):
            vegetable.change_hp(0)
        self.assertEqual(6, vegetable.info_lever_of_hp)
        vegetable.regeneration_hp(0)
        self.assertEqual(9, vegetable.info_lever_of_hp)
        vegetable.del_object(0)

    def test_day_today_level_change_and_regeneration_hp_fruits(self):
        fruits = Fruits("Груша", 1, 1)
        self.assertEqual(0, fruits.day_today)
        self.assertNotEqual(10, fruits.info_lever_of_hp)
        for i in range(0, 3):
            fruits.change_hp(1)
        self.assertEqual(6, fruits.info_lever_of_hp)
        fruits.regeneration_hp(1)
        self.assertEqual(9, fruits.info_lever_of_hp)
        fruits.del_object(1)

    def test_info_change_water_vegetables(self):
        vegetable = Vegetables("Морковка", 1, 0)
        self.assertNotEqual(6, vegetable.info_lever_of_water)
        vegetable.change_level_of_water(-3, 0)
        self.assertEqual(2, vegetable.info_lever_of_water)
        vegetable.del_object(0)

    def test_info_change_water_fruits(self):
        fruits = Fruits("Груша", 1, 1)
        self.assertNotEqual(6, fruits.info_lever_of_water)
        fruits.change_level_of_water(-3, 1)
        self.assertEqual(2, fruits.info_lever_of_water)
        fruits.del_object(1)

    def test_info_name_height_growth_vegetables(self):
        vegetable = Vegetables("Морковка", 1, 0)
        self.assertEqual("Морковка", vegetable.info_name)
        self.assertEqual("Первые 2-3 настоящих листа", vegetable.info_height)
        vegetable.fetal_growth(6, 0)
        self.assertEqual("Плод созрел", vegetable.info_height)
        vegetable.del_object(0)

    def test_info_name_height_growth_fruits(self):
        fruits = Fruits("Груша", 1, 1)
        self.assertEqual("Груша", fruits.info_name)
        self.assertEqual("Семечко в земле", fruits.info_height)
        fruits.fetal_growth(6, 1)
        self.assertEqual("Период плодоношения", fruits.info_height)
        fruits.del_object(1)

if __name__ == '__main__':
    unittest.main()
