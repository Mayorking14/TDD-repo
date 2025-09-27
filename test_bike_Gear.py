import unittest
from bike_Gear import Bike


class TestBikeDefaultPower(unittest.TestCase):
    def setUp(self):
        self.bike1 = Bike()

    def test_that_bike_is_off_at_default(self):
        power = self.bike1.get_is_power()
        self.assertFalse(power, False)

    def test_that_bike_is_turn_on_when_off(self):
        self.bike1.power()
        self.assertTrue(self.bike1.get_is_power())

    def test_that_bike_is_turn_on_when_off_and_can_be_turned_on(self):
        self.bike1.power()
        self.bike1.power()
        self.bike1.power()
        self.assertTrue(self.bike1.get_is_power())

    def test_that_the_bike_accelerates_when_on(self):
        self.bike1.power()
        self.bike1.set_gear()
        self.bike1.accelerate()
        self.bike1.accelerate()
        self.assertEqual(2, self.bike1.get_speed())

    def test_that_the_bike_changes_gear_with_speed(self):
        self.bike1.power()
        self.bike1.set_speed(35)
        self.bike1.set_gear()
        self.assertEqual(3, self.bike1.get_gear())

    def test_that_the_speed_increases_by_1_when_gear_is_1(self):
        self.bike1.power()
        self.bike1.set_gear()
        self.bike1.accelerate()
        self.assertEqual(1, self.bike1.get_speed())


    def test_that_speed_increases_by_2_when_gear_is_2(self):
         self.bike1.power()
         self.bike1.set_speed(27)
         self.bike1.set_gear()
         self.bike1.accelerate()
         self.assertEqual(29, self.bike1.get_speed())

    def test_that_speed_increases_by_3_when_gear_is_3(self):
        self.bike1.power()
        self.bike1.set_speed(35)
        self.bike1.set_gear()
        self.bike1.accelerate()
        self.assertEqual(38, self.bike1.get_speed())

    def test_that_speed_increases_by_4_when_gear_is_4(self):
        self.bike1.power()
        self.bike1.set_speed(45)
        self.bike1.set_gear()
        self.bike1.accelerate()
        self.assertEqual(49, self.bike1.get_speed())

    def test_that_bike_do_not_change_when_bike_is_off(self):
        self.bike1.get_is_power()
        self.bike1.set_speed(10)
        self.bike1.set_gear()
        self.assertEqual(0, self.bike1.get_gear())



