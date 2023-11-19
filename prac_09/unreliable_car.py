"""
CP1404 - Unreliable Car
"""
from random import randint
from prac_09.car import Car


class UnreliableCar(Car):
    """Represent SilverTaxi Service."""

    def __init__(self, name, fuel, realibility):
        """Initialise a Unreliable car."""
        super().__init__(name, fuel)
        self.reliability = realibility

    def drive(self, distance):
        random_number = randint(1, 100)
        if random_number >= self.reliability:
            distance = 0
            # Either way, we want to call the parent class's drive method (maybe driving 0)
        distance_driven = super().drive(distance)
        return distance_driven
