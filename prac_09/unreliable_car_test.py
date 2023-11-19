"""
CP1404/CP5632 Practical
Unreliable car test
"""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Taxi testing"""
    # Cars with different reliabilities
    good_car = UnreliableCar("Mostly Good", 100, 90)
    bad_car = UnreliableCar("Shady", 100, 9)
    for i in range(1, 12):
        print(f"Attempt to drive{i}km")
        print(f"{good_car.name:12} drove {good_car.drive(i):2}km")
        print(f"{bad_car.name:12} drove {bad_car.drive(i):2}km")
    # State of the car
    print(good_car)
    print(bad_car)


main()
