# Incubyte — Sweet Shop Management 

This project is a Python implementation of a Sweet Shop Management System**, built using **Test-Driven Development (TDD) principles.

## Features
- Inventory management (add sweets, update prices, track stock, total value)
- Order management (add items, checkout, apply discounts)
- Discount: 10% off if order subtotal ≥ 100
- Exception handling for insufficient stock
- Test suite using **pytest**

## Installation & Run Tests
```bash
git clone https://github.com/<your-username>/incubyte-sweetshop.git
cd incubyte-sweetshop
python3 -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
pytest -q
