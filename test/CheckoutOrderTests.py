import unittest
from src.CheckoutOrder import CheckoutOrder


class CheckoutOrderTests(unittest.TestCase):
    def test_add_item(self):
        checkout_order = CheckoutOrder()
        self.assertTrue(checkout_order.add_item('item', 1))


    def test_scan_item(self):
        checkout_order = CheckoutOrder()
        self.assertTrue(checkout_order.scan_item())


if __name__ == 'main':
    unittest.main()
