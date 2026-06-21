from datetime import datetime


class CarRental:
    def __init__(self, stock=100):
        self.stock = stock

    def display_available_cars(self):
        print(f"\nAvailable Cars: {self.stock}")

    def rent_hourly(self, num_cars):
        if num_cars <= 0:
            print("Number of cars should be positive.")
            return None

        if num_cars > self.stock:
            print(f"Only {self.stock} cars available.")
            return None

        self.stock -= num_cars
        print(f"{num_cars} car(s) rented on hourly basis.")
        return datetime.now()

    def rent_daily(self, num_cars):
        if num_cars <= 0:
            print("Number of cars should be positive.")
            return None

        if num_cars > self.stock:
            print(f"Only {self.stock} cars available.")
            return None

        self.stock -= num_cars
        print(f"{num_cars} car(s) rented on daily basis.")
        return datetime.now()

    def rent_weekly(self, num_cars):
        if num_cars <= 0:
            print("Number of cars should be positive.")
            return None

        if num_cars > self.stock:
            print(f"Only {self.stock} cars available.")
            return None

        self.stock -= num_cars
        print(f"{num_cars} car(s) rented on weekly basis.")
        return datetime.now()

    def return_car(self, request):
        rental_time, rental_basis, num_cars = request

        if rental_time and rental_basis and num_cars:
            self.stock += num_cars

            rental_period = datetime.now() - rental_time

            bill = 0

            if rental_basis == 1:
                hours = max(1, round(rental_period.seconds / 3600))
                bill = hours * 50 * num_cars
            elif rental_basis == 2:
                days = max(1, rental_period.days)
                bill = days * 500 * num_cars

            elif rental_basis == 3:
                weeks = max(1, round(rental_period.days / 7))
                bill = weeks * 3000 * num_cars

            print(f"\nRental Bill: ₹{bill}")
            return bill

        else:
            print("Invalid return request.")
            return None


class Customer:
    def __init__(self):
        self.cars = 0
        self.rental_basis = 0
        self.rental_time = 0

    def request_car(self):
        cars = int(input("Enter number of cars: "))
        return cars

    def return_car(self):
        if self.rental_time and self.rental_basis and self.cars:
            return self.rental_time, self.rental_basis, self.cars
        else:
            return 0, 0, 0
