from typing import Dict
from .models import Sweet
from .exceptions import InsufficientStockError

class Inventory:
    def __init__(self):
        # internal store: name -> {"sweet": Sweet, "qty": int}
        self._items: Dict[str, dict] = {}

    def add_sweet(self, name: str, price: float, qty: int = 0):
        if qty < 0:
            raise ValueError("qty must be >= 0")
        if price < 0:
            raise ValueError("price must be >= 0")
        if name in self._items:
            # update price and stock
            self._items[name]["sweet"].price = price
            self._items[name]["qty"] += qty
        else:
            self._items[name] = {"sweet": Sweet(name, price), "qty": qty}

    def get_stock(self, name: str) -> int:
        return self._items.get(name, {"qty": 0})["qty"]

    def get_price(self, name: str) -> float:
        item = self._items.get(name)
        if not item:
            raise KeyError(f"{name} not found in inventory")
        return item["sweet"].price

    def sell(self, name: str, qty: int = 1) -> float:
        if qty <= 0:
            raise ValueError("qty must be > 0")
        if name not in self._items or self._items[name]["qty"] < qty:
            raise InsufficientStockError(f"Not enough stock for {name}")
        self._items[name]["qty"] -= qty
        total_price = self._items[name]["sweet"].price * qty
        return round(total_price, 2)

    def total_value(self) -> float:
        total = 0.0
        for v in self._items.values():
            total += v["sweet"].price * v["qty"]
        return round(total, 2)

    def list_items(self) -> dict:
        return {
            name: {"price": v["sweet"].price, "qty": v["qty"]}
            for name, v in self._items.items()
        }
