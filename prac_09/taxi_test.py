"""
CP1404/CP5632 Practical
Taxi test
"""
from prac_09.taxi import Taxi


def main():
    """Taxi testing"""
    my_taxi = Taxi("Prius 1", 100)  # name, price_per_km, current_fare_distance
    my_taxi.drive(40)
    print(my_taxi)
    my_taxi.start_fare()
    my_taxi.drive(100)
    print(my_taxi)


main()

"""
Output:
Prius 1, fuel=60, odometer=40, 40km on current fare, $1.23/km
Prius 1, fuel=0, odometer=100, 60km on current fare, $1.23/km
"""