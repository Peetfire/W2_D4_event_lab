import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer = Customer("Meera", 100.50, "Adele")

    def test_has_name(self):
        self.assertEqual("Meera", self.customer.name)

    def test_for_favourite_performer(self):
        self.assertEqual('Adele',self.customer.favourite)

    def test_has_a_wallet(self):
        self.assertEqual(100.50,self.customer.wallet)
    
    def test_can_reduce_money_from_wallet(self):
        self.customer.reduce_money(10.50)
        self.assertEqual(90, self.customer.wallet)
    
    def test_can_get_favourite_perfomer(self):
        self.assertEqual('Adele', self.customer.get_favourite())