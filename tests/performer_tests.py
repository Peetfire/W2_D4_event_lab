import unittest
from src.performer import Performer

class TestPerformer(unittest.TestCase):

    def setUp(self):
        self.performer = Performer("Jimmy Crankey")

    def test_has_name(self):
        self.assertEqual("Jimmy Crankey", self.performer.name)

    def test_can_add_money(self):
        self.performer.add_money(100)
        self.assertEqual(100, self.performer.earnings)