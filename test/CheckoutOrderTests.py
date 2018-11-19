import unittest
from src.CheckoutOrder import CheckoutOrder


class CheckoutOrderTests(unittest.TestCase):
    def setUp(self):
        self.checkout_order = CheckoutOrder()
        self.checkout_order.add_item('item', 1.00)
        self.checkout_order.add_item('second_item', 1.50)


    def tearDown(self):
        self.checkout_order = None


    def test_add_item(self):
        self.assertTrue(self.checkout_order.add_item('item3', 1))


    def test_scan_item(self):
        self.assertEqual(1.00, self.checkout_order.scan_item('item'))
        self.assertEqual(2.00, self.checkout_order.scan_item('item'))
        self.assertEqual(3.50, self.checkout_order.scan_item('second_item'))
        self.assertEqual(5.00, self.checkout_order.scan_item('second_item'))


    def test_scan_item_by_weight(self):
        self.assertEqual(1.00, self.checkout_order.scan_item_by_weight('weight_item', 1))
        self.assertEqual(2.10, self.checkout_order.scan_item_by_weight('weight_item', 1.1))


if __name__ == 'main':
    unittest.main()
