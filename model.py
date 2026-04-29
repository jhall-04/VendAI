from typing import List

from langchain.messages import AIMessage, SystemMessage
from langchain.tools import tool
from langchain_ollama import ChatOllama

from vend import VendingMachine, Item

vending_machine = VendingMachine(balance=100)

items = [
    Item(name="Coke", price=1.50),
    Item(name="Pepsi", price=1.50),
    Item(name="Water", price=1.00)]


@tool
def restock(item_name: str, purchase_price: float, selling_price: float, quantity: int) -> str:
    """ Restock an item in the vending machine. If the balance is insufficient to restock the full quantity, restock as many as possible with the available balance and return a message indicating how many items were restocked.
    
    Args:
        item_name (str): The name of the item to restock.
        purchase_price (float): The price at which the item is purchased for restocking.
        selling_price (float): The price at which the item will be sold in the vending machine.
        quantity (int): The quantity of the item to restock.
    Returns:
        str: A message indicating the result of the restocking operation.
    """
    item = Item(name=item_name, price=purchase_price)
    balance = vending_machine.check_balance()
    total_cost = purchase_price * quantity
    if balance < total_cost:
        for _ in range(balance // purchase_price):
            vending_machine.add_item(item)
        added = balance // purchase_price
        if added > 0:
            vending_machine.set_sale_price(item_name, selling_price)
        return f"Not enough balance to restock {item_name}. Required: ${total_cost}, Available: ${balance}. Restocked {added} items."
    for _ in range(quantity):
        vending_machine.add_item(item)
    if quantity > 0:
        vending_machine.set_sale_price(item_name, selling_price)
    return f"Restocked {item_name} at ${purchase_price} (Quantity: {quantity})"

@tool
def check_stock() -> str:
    """
    Check the current stock of the vending machine.

    Returns:
        str: A string representation of the current stock and sale prices.
    """
    return vending_machine.display_stock()
    
for item in items:
    restock(item.name, item.price, item.price * 1.5, 4)
    

llm = ChatOllama(
    model="gemma3:4b"
).bind_tools([restock, check_stock])