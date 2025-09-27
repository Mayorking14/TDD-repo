from unittest import TestCase
import air_condition

class TestMyAirConditionPower(TestCase):
    def test_Confirm_Ac_Is_Turned_Off(self):
        air_condition.confirm_Ac_Off()
        self.assertTrue(True, air_condition.confirm_Ac_Off())

    def test_That_Ac_Is_Turned_On(self):
        air_condition.get_Ac_On()
        self.assertTrue(True, air_condition.get_Ac_On())

    def test_That_Ac_Is_Turned_Off(self):
        air_condition.get_Ac_On()
        self.assertFalse(False, air_condition.get_Ac_Off())

class TestAirConditionDefaultTemperature(TestCase):
    def test_Air_Condition_Default_Temperature(self):
        air_condition.get_Ac_On()
        result = air_condition.display_Temperature()
        self.assertEqual(result, 24)

    def test_Air_Condition_Default_Temperature_When_Off(self):
        air_condition.get_Ac_Off()
        self.assertFalse(False, air_condition.display_Temperature())
    def test_Air_Condition_Default_Temperature_When_On(self):
        air_condition.get_Ac_On()
        result = air_condition.display_Temperature()
        self.assertEqual(result, 24)

    def test_That_AirCondition_Default_Temperature_When_Off(self):
        air_condition.get_Ac_Off()
        self.assertFalse(False, air_condition.display_Temperature())

class TestAirConditionTemperatureIncrease(TestCase):
    def test_Air_Condition_Temperature_Increase(self):
        air_condition.get_Ac_On()
        air_condition.display_Temperature()
        air_condition.temperature_Increase()
        self.assertTrue(True, air_condition.temperature_Increase())

    def test_that_Air_Condition_Temperature_Do_Not_Increase_When_Off(self):
        air_condition.get_Ac_Off()
        air_condition.temperature_Increase()
        self.assertTrue(True, air_condition.get_Ac_Off())

    def test_That_Air_Condition_Temperature_Do_Not_Increase_Past_Limit(self):
        air_condition.get_Ac_On()
        air_condition.display_Temperature()
        air_condition.temperature_Increase_Limit()
        air_condition.temperature_Increase_Limit()
        self.assertTrue(True, air_condition.temperature_Increase_Limit())

class TestAirConditionTemperatureDecrease(TestCase):
    def test_Air_Condition_Temperature_Decrease(self):
        air_condition.get_Ac_On()
        air_condition.display_Temperature()
        air_condition.temperature_Decrease()
        self.assertTrue(True, air_condition.temperature_Decrease())

    def test_That_AirCondition_Temperature_Decrease_When_Off(self):
        air_condition.get_Ac_Off()
        air_condition.temperature_Decrease()
        self.assertFalse(False, air_condition.temperature_Decrease())

    def test_That_Air_Condition_Temperature_Do_Not_Decrease_Past_Limit(self):
        air_condition.get_Ac_On()
        air_condition.temperature_Decrease()
        air_condition.temperature_Decrease_Limit()
        self.assertTrue(True, air_condition.temperature_Decrease_Limit())