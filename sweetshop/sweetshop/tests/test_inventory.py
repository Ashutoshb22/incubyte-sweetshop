import pytest
from sweetshop.inventory import Inventory
from sweetshop.exceptions import InsufficientStockError

def test_add_and_get_stock():
    inv = Inventory()
    inv.add_sweet("Lollipop", 5.0, 10)
    assert inv.get_stock("Lollipop") == 10
    assert inv.get_price("Lollipop") == 5.0

def test_sell_reduces_stock_and_returns_price():
    inv = Inventory()
    inv.add_sweet("Choco", 10.0, 5)
    price = inv.sell("Choco", 2)
    assert price == 20.0
    assert inv.get_stock("Choco") == 3

def test_insufficient_stock_raises():
    inv = Inventory()
    inv.add_sweet("Candy", 1.5, 2)
    with pytest.raises(InsufficientStockError):
        inv.sell("Candy", 3)

def test_total_value():
    inv = Inventory()
    inv.add_sweet("A", 2.0, 3)
    inv.add_sweet("B", 4.5, 2)
    assert inv.total_value() == round(2.0*3 + 4.5*2, 2)
