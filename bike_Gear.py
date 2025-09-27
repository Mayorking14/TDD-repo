class Bike:
    def __init__(self):
        self.is_power = False
        self.gear = 0
        self.speed = 0


    def power(self):
        if not self.is_power:
            self.is_power = True

    def set_speed(self, speed_level):
        if self.is_power:
            self.speed = speed_level

    def get_is_power(self):
        return self.is_power

    def get_gear(self):
        return self.gear

    def accelerate(self):
        if self.is_power:
            self.speed += self.gear
        else:
            return "The bike is off"

    def decelerate(self):
        if self.is_power:
            if self.speed > 0:
                self.speed -= self.gear
            else:
                return "The bike has stopped"
        else:
            return "The bike is off"


    def get_speed(self):
        return self.speed


    def set_gear(self):
         if self.is_power:
             if 0 <= self.speed <= 20:
                self.gear = 1
             elif 21 <= self.speed <= 30:
                self.gear = 2
             elif 31 <= self.speed <= 40:
                self.gear = 3
             else:
                self.gear = 4

