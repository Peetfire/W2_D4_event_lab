class Event:
    def __init__(self,name,ticket_price,customers,performers):
        self.name = name
        self.ticket_price = ticket_price
        self.revenue = 0
        self.customers = customers
        self.performers = performers
        
        
    def add_money(self,amount):
        self.revenue += amount

    def reduce_money(self, amount):
        self.revenue -= amount

    def add_customer(self,customer):
        if not customer in self.customers:
            self.customers.append(customer)
        
    