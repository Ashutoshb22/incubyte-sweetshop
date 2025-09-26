from .exceptions import InsufficientStockError

class Order:
    """
    Order that references an Inventory instance.
    Items are added to the order; checkout() will decrement inventory.
    A simple discount rule: if subtotal >= 100 then 10% off final total.
    """
    def __init__(self, inventory):
        self.inventory = inventory
        self.items = {}  # name -> qty

    def add_item(self, name: str, qty: int = 1):
        if qty <= 0:
            raise ValueError("qty must be > 0")
        if self.inventory.get_stock(name) < qty:
            raise InsufficientStockError(f"Not enough stock for {name}")
        self.items[name] = self.items.get(name, 0) + qty

    def subtotal(self) -> float:
        total = 0.0
        for name, qty in self.items.items():
            price = self.inventory.get_price(name)
            total += price * qty
        return round(total, 2)

    def total(self) -> float:
        subtotal = self.subtotal()
        if subtotal >= 100:
            subtotal = subtotal * 0.9  # 10% discount
        return round(subtotal, 2)

    def checkout(self) -> float:
        """Attempt to sell all items from inventory and return final total."""
        # Double-check stock
        for name, qty in self.items.items():
            if self.inventory.get_stock(name) < qty:
                raise InsufficientStockError(f"Not enough stock for {name}")

        sold_total = 0.0
        for name, qty in self.items.items():
            sold_total += self.inventory.sell(name, qty)

        if sold_total >= 100:
            sold_total = round(sold_total * 0.9, 2)
        else:
            sold_total = round(sold_total, 2)

        # Empty cart after checkout
        self.items = {}
        return sold_total
