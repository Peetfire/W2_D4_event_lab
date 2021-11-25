class Performer:

    def __init__(self, name):
        self.name = name
        self.earnings = 0

    def add_money(self, amount):
        self.earnings += amount