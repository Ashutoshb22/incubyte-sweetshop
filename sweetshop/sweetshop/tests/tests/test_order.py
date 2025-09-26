import pytest
from sweetshop.inventory import Inventory
from sweetshop.order import Order
from sweetshop.exceptions import InsufficientStockError

def test_order_total_and_checkout_with_discount():
    inv = Inventory()
    inv.add_sweet("PremiumCake", 60.0, 2)
    order = Order(inv)
    order.add_item("PremiumCake", 2)  # subtotal 120 -> discount applies
    assert order.subtotal() == 120.0
    assert order.total() == round(120.0 * 0.9, 2)
    total = order.checkout()
    assert total == round(120.0 * 0.9, 2)
    assert inv.get_stock("PremiumCake") == 0

def test_add_item_insufficient_raises():
    inv = Inventory()
    inv.add_sweet("Bar", 5.0, 1)
    order = Order(inv)
    with pytest.raises(InsufficientStockError):
        order.add_item("Bar", 2)
