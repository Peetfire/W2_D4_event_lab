class Customer:

    def __init__(self, name, wallet, favourite):
        self.name = name
        self.wallet = wallet
        self.favourite = favourite

    def reduce_money(self, amount):
        self.wallet -= amount
    
    def get_favourite(self):
        return self.favourite

    