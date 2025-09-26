class InsufficientStockError(Exception):
    """Raised when trying to sell more items than available in inventory."""
    pass
