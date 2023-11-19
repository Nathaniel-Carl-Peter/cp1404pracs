from prac_09.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Main taxi program"""
    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = 0
    print("Let's drive")
    choice = user_input()
    while choice != 'q':
        if choice == 'c':
            print("Taxis available: ")
            display_taxis(taxis)
            # no error-checking
            taxi_choice = int(input("Choose your taxi: "))
            try:
                current_taxi = taxis[taxi_choice]
            except IndexError:
                print("Invalid input")
        elif choice == 'd':
            if current_taxi:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                trip_cost = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                total_bill += trip_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid choice :P")
        print(f"Bill to date: ${total_bill:.2f}")
        choice = user_input()
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)
    print("Finished. ;)")


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def user_input():
    MENU = "q)uit, c)hoose taxi, d)rive"
    print(MENU)
    choice = input(">>> ").lower()
    return choice


def run_tests():
    """Run tests to show workings of Car and Taxi classes."""
    bus = Car("Datsun", 180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus._odometer)
    bus.drive(55)
    print("fuel =", bus.fuel)
    print("odo = ", bus._odometer)
    print(bus)

    # drive bus (input/loop is oblivious to fuel)
    distance = int(input("Drive how far? "))
    while distance > 0:
        distance_travelled = bus.drive(distance)
        print(f"{bus} travelled {distance_travelled}")
        distance = int(input("Drive how far? "))

    t = Taxi("Prius 1", 100)
    print(t)
    t.drive(25)
    print(t, t.get_fare())
    t.start_fare()
    t.drive(40)
    print(t, t.get_fare())

    sst = SilverServiceTaxi("Limo", 100, 2)
    print(sst, sst.get_fare())
    sst.drive(10)
    print(sst, sst.get_fare())


main()
# run_tests()
