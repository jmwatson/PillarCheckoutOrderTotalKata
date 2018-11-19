import unittest
from src.CheckoutOrder import CheckoutOrder


class CheckoutOrderTests(unittest.TestCase):
    def setUp(self):
        self.checkout_order = CheckoutOrder()


    def tearDown(self):
        self.checkout_order = None


    def test_add_item(self):
        self.assertTrue(self.checkout_order.add_item('item', 1))


    def test_scan_item(self):
        self.assertEqual(1.00, self.checkout_order.scan_item('item'))
        self.assertEqual(2.00, self.checkout_order.scan_item('item'))
        self.assertEqual(3.50, self.checkout_order.scan_item('second_item'))
        self.assertEqual(5.00, self.checkout_order.scan_item('second_item'))


if __name__ == 'main':
    unittest.main()
