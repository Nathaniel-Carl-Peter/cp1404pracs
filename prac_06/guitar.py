"""
CP1404 - Prac 06 -Guitars
"""
CURRENT_YEAR = 2013
VINTAGE_AGE = 50


class Guitar:
    """Represent a Car object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise Guitar."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Display results which represent Car object"""
        return f"{self.name}, {self.year}, ${self.cost:.2f}"

    def get_age(self):
        """Get the age of guitar based on 2017"""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Drive the car a given distance.

        Drive given distance if car has enough fuel
        or drive until fuel runs out return the distance actually driven.
        """
        return self.get_age() >= VINTAGE_AGE
