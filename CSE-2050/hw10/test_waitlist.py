import unittest
from waitlist import Waitlist

class Test_Waitlist(unittest.TestCase):
    def test_add_customer(self):
        ''' tests adding customers to the waitlist '''
        waitlist = Waitlist()
        
        # tests adding a customer with a valid time
        waitlist.add_customer("Alice", "12:00")
        assert len(waitlist._entries) == 1
        assert waitlist._entries[0].name == "Alice"

        # tests adding multiple customers and check if they are sorted correctly by reservation time
        waitlist.add_customer("Charlie", "11:00")
        waitlist.add_customer("David", "10:30")
        waitlist.add_customer("Eve", "11:30")
        waitlist.add_customer("Frank", "10:45")
        assert len(waitlist._entries) == 5
        assert waitlist._entries[0].name == "David"
        assert waitlist._entries[1].name == "Frank"
        assert waitlist._entries[2].name == "Charlie"
        assert waitlist._entries[3].name == "Eve"
        assert waitlist._entries[4].name == "Alice"

        # tests adding a customer with the wrong format for time
        waitlist.add_customer("Karina", "1")
        assert len(waitlist._entries) == 5 # (length should not change because Karina was not added to waitlist)

   
    def test_peek(self):
        ''' tests that peek returns the customer with highest priority '''
        waitlist = Waitlist()

        # tests the waitlist is empty
        assert waitlist.peek() == None

        waitlist.add_customer("Alice", "12:00")
        waitlist.add_customer("Charlie", "11:00")
        waitlist.add_customer("David", "10:30") # priority
        waitlist.add_customer("Eve", "11:30")
        waitlist.add_customer("Frank", "10:45")
        
        # tests that David, who is the earliest, is the one returned with the peek
        assert waitlist.peek()[0] == 'David'

        # asserts that customer will be sorted correctly and peeked correctly
        waitlist.add_customer("Karina", "9:45")
        assert waitlist.peek()[0] == 'Karina'

   
    def test_seat_customer(self):
        ''' tests that this function removes customer with highest priority '''
        waitlist = Waitlist()

        # tests the waitlist is empty so no customers to seat
        assert waitlist.seat_customer() == None

        waitlist.add_customer("Alice", "12:00") # 5
        waitlist.add_customer("Charlie", "11:00") # 3
        waitlist.add_customer("David", "10:30") # 1
        waitlist.add_customer("Eve", "11:30") # 4
        waitlist.add_customer("Frank", "10:45") # 2
        
        # tests that David, who is the earliest, is seated and removed
        assert waitlist.seat_customer()[0] == 'David'
        assert len(waitlist._entries) == 4

        # tests that Frank, who is second earliest, is seated and removed
        assert waitlist.seat_customer()[0] == 'Frank'
        assert len(waitlist._entries) == 3

        # tests that Charlie, who is third earliest, is seated and removed
        assert waitlist.seat_customer()[0] == 'Charlie'
        assert len(waitlist._entries) == 2

        # tests that Eve, who is fourth earliest, is seated and removed
        assert waitlist.seat_customer()[0] == 'Eve'
        assert len(waitlist._entries) == 1

        # tests that Alice, who is fourth earliest, is seated and removed
        assert waitlist.seat_customer()[0] == 'Alice'
        assert len(waitlist._entries) == 0

        # tests the waitlist is empty (again) so no customers to seat
        assert waitlist.seat_customer() == None

      
    def test_print_reservation_list(self):
        ''' tests that this function removes customer with highest priority '''
        waitlist = Waitlist()

        # the waitlist is empty so should be empty
        assert waitlist.print_reservation_list() == 'The waitlist is empty.'

        waitlist.add_customer("Alice", "12:00")
        waitlist.add_customer("Charlie", "11:00")
        waitlist.add_customer("David", "10:30")
        
        # tests that it prints what it should print
        assert waitlist.print_reservation_list() == 'Waitlist:\nDavid (10:30)\nCharlie (11:00)\nAlice (12:00)'
        

    def test_change_reservation_time(self):
        ''' tests that it changes reservation time of a specific customer '''
        waitlist = Waitlist()

        waitlist.add_customer("Alice", "12:00")
        waitlist.add_customer("Charlie", "11:00")
        waitlist.add_customer("David", "10:30")
        waitlist.add_customer("Eve", "11:30")
        waitlist.add_customer("Frank", "10:45")

        # changed time so Alice is now the first in the priority, so she should be first
        assert waitlist.change_reservation_time('Alice','9:00')
        assert waitlist.peek()[0] == 'Alice'

        # gave Frank a wrong time so makes sure that it doesn't actually change the reservation time
        assert not waitlist.change_reservation_time('Frank','900')

        # Karina does not exist so makes sure that it doesn't actually change the reservation time
        assert not waitlist.change_reservation_time('Karina','9:00')


unittest.main()