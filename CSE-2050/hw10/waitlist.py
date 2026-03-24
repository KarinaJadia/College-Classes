import random
class Time:
    """A class that represents time in the format HH:MM"""
    def __init__(self, hour, minute):
        self.hour = int(hour)
        self.minute = int(minute)

    def __lt__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self < other, and False otherwise"""
        if self.hour < other.hour:
            return True
        elif self.hour == other.hour and self.minute < other.minute:
            return True
        else:
            return False
    
    def __eq__(self, other):
        """Compare two times based on their hour and minute"""
        """ return True if self == other, and False otherwise"""
        if self.hour ==  other.hour and self.minute == other.minute:
            return True
        else:
            return False

    def __repr__(self):
        """Return the string representation of the time"""
        return f"{self.hour:02d}:{self.minute:02d}"

class Entry:
    """A class that represents a customer in the waitlist"""
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __lt__(self, other):
        """Compare two customers based on their time, if equal then compare based on the customer name"""
        if self.time == other.time:
            return self.name < other.name
        return self.time < other.time

    def get_time(self):
        """ returns the entry's reservation time """
        # made this to deal with sorting customers in add_customer
        return self.time    

class Waitlist:
    def __init__(self):
        self._entries = []

    def add_customer(self, name, priority):
        """ adds a customer to the waitlist if they input their time correctly and returns True if they did and False if not """
        try:
            # take the two numbers from the customer's reservation time 
            time = Time(*priority.split(":"))
            # creates a new Entry object for the customer
            entry = Entry(name, time)
            # adds the entry to the waitlist
            self._entries.append(entry)
            # sorts the waitlist by reservation time
            self._entries.sort(key=Entry.get_time)
            print(f"Added {name} to the waitlist with reservation time {priority}")
            return True
        except:
            # if the customer did not input their time correctly, throw an error
            print("Invalid time format. Please enter time in the format HH:MM")
            return False


    def peek(self):
        """ returns the customer with the highest priority """
        # checks if user isn't in waitlist
        if not self._entries:
            print("The waitlist is empty.")
            return None
        # takes the first element in waitlist
        entry = self._entries[0]
        print(f"The first customer in the waitlist is {entry.name} with reservation time {entry.time}")
        # the tuple i must return
        tuple = (entry.name, entry.time)
        return tuple


    def seat_customer(self):
        """ seats the next customer and returns them """
        # if the list is empty then there is no one to seat
        if not self._entries:
            print("The waitlist is empty. No customer to seat.")
            return None
        entry = self._entries.pop(0)
        print(f"Seated {entry.name} with reservation time {entry.time}")
        # the tuple i must return
        tuple = (entry.name, entry.time)
        return tuple


    def print_reservation_list(self):
        """ prints all customers in order of their priority (reservation time) """
        if not self._entries:
            return "The waitlist is empty."
        else:
            # makes a large string of all the waitlist members and returns it
            entries_str = "\n".join(f"{entry.name} ({entry.time})" for entry in self._entries)
            return f"Waitlist:\n{entries_str}"


    def change_reservation_time(self, name, new_priority):
        """ changes the reservation time (priority) for the customer with the given name but returns false if they input name or time wrong """
        try:
            time = Time(*new_priority.split(":"))
            for entry in self._entries:
                if entry.name == name:
                    old_time = entry.time
                    entry.time = time
                    self._entries.sort(key=Entry.get_time)
                    print(f"Changed reservation time for {name} from {old_time} to {time}")
                    return True
            print(f"{name} not found in the waitlist.")
            return False
        except:
            print("Invalid time format. Please enter time in the format HH:MM")
            return False
    

    def __repr__(self):
        """ returns a string representation of the waitlist, helps with print_reservation_list (for some reason that doesn't work without this) """
        if not self._entries:
            return "The waitlist is empty."
        else:
            # makes a large string of all the waitlist members and returns it
            entries_str = "\n".join(f"{entry.name} ({entry.time})" for entry in self._entries)
            return f"Waitlist:\n{entries_str}"
        

    def contains(self, name, priority):
        return (name, priority) in self._entries