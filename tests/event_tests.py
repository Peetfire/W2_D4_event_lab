import unittest
from src.event import Event
from src.performer import Performer
from src.customer import Customer

class TestEvent(unittest.TestCase):

    def setUp(self):
        self.customer1 = Customer("Meera", 100.50, "Adele")
        self.customer2 = Customer("Peter", 10.00, "David Bowie")
        self.customer3 = Customer("Torin", 200, "Blippi")
        self.customers = []
        self.performer1 = Performer("Jimmy Crankey")
        self.performer2 = Performer('Adele')
        self.performers = [self.performer1, self.performer2]
        self.event = Event("Glastonbury", 100, self.customers, self.performers)

    def test_event_has_name(self):
        self.assertEqual('Glastonbury', self.event.name)
        
    def test_event_has_price(self):
        self.assertEqual(100, self.event.ticket_price)

    def test_event_has_customers_list(self):
        self.assertEqual(0, len(self.customers))

    def test_event_has_performers(self):
        self.assertEqual(2, len(self.performers))
    
    def test_can_add_money(self):
        self.event.add_money(10.50)
        self.assertEqual(10.50, self.event.revenue)
    
    def test_can_reduce_money(self):
        self.event.add_money(100)
        self.event.reduce_money(20)
        self.assertEqual(80, self.event.revenue)
    
    def test_can_add_customer_to_list(self):
        customer = self.customer1
        self.event.add_customer(customer)
        self.assertEqual(1, len(self.customers))

    
    def test_can_add_performer(self):
        performer = Performer("Jimmy Cliff")
        self.event.add_performer(performer)
        self.assertEqual(3, len(self.performers))