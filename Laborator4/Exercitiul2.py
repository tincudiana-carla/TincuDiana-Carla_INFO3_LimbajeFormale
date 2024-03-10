class ParkingAutomaton:
    def __init__(self, total_spaces):
        self.total_spaces = total_spaces
        self.available_spaces = total_spaces

    def park_car(self):
        if self.available_spaces > 0:
            self.available_spaces -= 1
            print("Car parked successfully.")
        else:
            print("Parking is full. Cannot park car.")

    def leave_car(self):
        if self.available_spaces < self.total_spaces:
            self.available_spaces += 1
            print("Car left parking successfully.")
        else:
            print("Parking is already empty. No cars to leave.")

    def get_parking_status(self):
        print(f"Total spaces: {self.total_spaces}")
        print(f"Available spaces: {self.available_spaces}")

    def process_request(self, request):
        if request == "park":
            self.park_car()
        elif request == "leave":
            self.leave_car()
        elif request == "status":
            self.get_parking_status()
        else:
            print("Invalid request. Please use 'park', 'leave', or 'status'.")


def main():
    total_spaces = 5
    parking = ParkingAutomaton(total_spaces)

    while True:
        print("\nOptions: park, leave, status, exit")
        option = input("Enter your choice: ")

        if option == "exit":
            print("Exiting...")
            break

        parking.process_request(option)


if __name__ == "__main__":
    main()
