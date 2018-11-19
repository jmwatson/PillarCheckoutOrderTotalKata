import unittest
from src.CheckoutOrder import CheckoutOrder


class CheckoutOrderTests(unittest.TestCase):
    def test_add_item(self):
        checkout_order = CheckoutOrder()
        self.assertTrue(checkout_order.add_item('item', 1))


    def test_scan_item(self):
        checkout_order = CheckoutOrder()
        self.assertEqual(1.00, checkout_order.scan_item('item'))
        self.assertEqual(2.00, checkout_order.scan_item('item'))
        self.assertEqual(3.50, checkout_order.scan_item('second_item'))
        self.assertEqual(5.00, checkout_order.scan_item('second_item'))


if __name__ == 'main':
    unittest.main()
