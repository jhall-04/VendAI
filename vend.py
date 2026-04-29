from dataclasses import dataclass

@dataclass(frozen=True)
class Item:
    name: str
    price: float
    def __repr__(self):
        return f"Item(name='{self.name}', price={self.price})"

class VendingMachine:
    """
    A simple vending machine that can hold items, restock them, and allow purchases.
    The machine keeps track of the money it has collected from purchases.
    """
    def __init__(self, balance=0):
        self.items = {}
        self.sale_prices = {}
        self.balance = balance

    def add_item(self, item: Item):
        if self.balance >= item.price:
            self.items[item.name] = self.items.get(item.name, 0) + 1
            self.balance -= item.price
        else:
            raise ValueError(f"Not enough balance to add {item.name}. Required: ${item.price}, Available: ${self.balance}")
    
    def set_sale_price(self, item_name: str, price: float):
        if item_name in self.items:
            self.sale_prices[item_name] = price
        else:
            raise ValueError(f"Cannot set sale price for {item_name} as it does not exist in the vending machine.")
        
    def sell_item(self, item_name: str):
        if item_name in self.items and self.items[item_name] > 0:
            self.items[item_name] -= 1
            self.balance += self.get_item_price(item_name)
            return f"Purchased {item_name} for ${self.get_item_price(item_name)}"
        else:
            raise ValueError(f"{item_name} is out of stock or does not exist.")
        
    def check_balance(self):
        return self.balance
    
    def display_stock(self):
        inventory = "Current Stock:\n"
        for item in self.items:
            inventory += f"{item}: {self.items[item]} in stock, Sale Price: ${self.sale_prices.get(item, 'Not set')}\n"
        return inventory.strip()