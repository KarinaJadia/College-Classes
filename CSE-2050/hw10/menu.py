from waitlist import Waitlist

class Menu:
    """A class representing the menu for the restaurant reservation program"""

    def __init__(self):
        """Initialize the menu with the waitlist object"""
        self.waitlist = Waitlist()

    def run(self):
        """Print the main menu"""
        print("Welcome to the Restaurant Reservation System!")
        print("==============================================")
        print("Please select an option:")
        print("1. Add a customer to the waitlist")
        print("2. Seat the next customer")
        print("3. Change the time of a customer's reservation")
        print("4. Peek at the next customer")
        print("5. Print the reservation list")
        print("6. Quit")
        print("")
        
        while True:
            choice = input("Enter your choice (1-6): ")
            print("*************************************************")
            
            if choice == "1":
                name = input("Enter the customer's name: ")
                time = input("Enter the reservation time (HH:MM): ")
                self.waitlist.add_customer(name, time)
                
            elif choice == "2":
                next_customer = self.waitlist.seat_customer()
                if next_customer:
                    print(f"Seating {next_customer.name}.")
                else:
                    print("No customers in waitlist.")
                
            elif choice == "3":
                name = input("Enter the customer's name: ")
                time = input("Enter the new reservation time (HH:MM): ")
                if self.waitlist.change_reservation_time(time,name):
                    print("Reservation time updated.")
                else:
                    print(self.waitlist.change_reservation_time(time,name))
                
            elif choice == "4":
                next_customer = self.waitlist.peek()
                if next_customer:
                    print(f"The next customer is {next_customer.name}.")
                else:
                    print("No customers in waitlist.")
                
            elif choice == "5":
                print(self.waitlist)
                
            elif choice == "6":
                print("Thank you for using the Restaurant Reservation System!")
                break
                
            else:
                print("Invalid choice. Try again.")

if __name__ == '__main__':
    s = Menu()
    s.run()
