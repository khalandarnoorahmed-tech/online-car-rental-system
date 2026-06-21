from car_rental import CarRental, Customer


def main():

    shop = CarRental(50)
    customer = Customer()

    while True:

        print("\n===== ONLINE CAR RENTAL SYSTEM =====")
        print("1. Display Available Cars")
        print("2. Rent Car Hourly")
        print("3. Rent Car Daily")
        print("4. Rent Car Weekly")
        print("5. Return Car")
        print("6. Exit")

        try:
            choice = int(input("\nEnter choice (1-6): "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            shop.display_available_cars()

        elif choice == 2:
            customer.cars = customer.request_car()

            customer.rental_time = shop.rent_hourly(customer.cars)

            if customer.rental_time:
                customer.rental_basis = 1

        elif choice == 3:
            customer.cars = customer.request_car()

            customer.rental_time = shop.rent_daily(customer.cars)

            if customer.rental_time:
                customer.rental_basis = 2

        elif choice == 4:
            customer.cars = customer.request_car()

            customer.rental_time = shop.rent_weekly(customer.cars)

            if customer.rental_time:
                customer.rental_basis = 3

        elif choice == 5:

            if customer.cars == 0:
                print("\nNo active rental found.")
            else:
                bill = shop.return_car(customer.return_car())

                print(f"Final Bill Amount: ₹{bill}")

                # Reset customer data after successful return
                customer.cars = 0
                customer.rental_basis = 0
                customer.rental_time = 0

        elif choice == 6:
            print("\nThank you for using the Car Rental System.")
            break

        else:
            print("Invalid choice. Please select between 1 and 6.")


if __name__ == "__main__":
    main()
