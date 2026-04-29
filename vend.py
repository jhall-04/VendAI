class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class VendingMachine:
    def __init__(self):
        self.items = {}
        self.balance = 0

    def add_item(self, item):
        self.items[item.name] = self.items.get(item.name, 0) + 1

    def insert_money(self, amount):
        self.balance += amount

    def select_item(self, item_name):
        if item_name not in self.items or self.items[item_name] == 0:
            return "Item not available"
        
        item_price = self.get_item_price(item_name)
        self.insert_money(item_price)  # Assuming the user inserts the exact amount for simplicity
        
        self.balance -= item_price
        self.items[item_name] -= 1
        return f"Dispensed {item_name}"
    
    def display_items(self):
        return {item: count for item, count in self.items.items()}

    def get_balance(self):
        return self.balance