import unittest
from src.CheckoutOrder import CheckoutOrder


class CheckoutOrderTests(unittest.TestCase):
    def setUp(self):
        self.checkout_order = CheckoutOrder()
        self.checkout_order.add_item('item', 1.00)
        self.checkout_order.add_item('second_item', 1.50)
        self.checkout_order.add_item('markdown_item', 1.00)
        self.checkout_order.add_item('markdown_weighted_item', 1.00)
        self.checkout_order.add_item('weight_item', 1.00)
        self.checkout_order.add_item('second_weight_item', 1.50)
        self.checkout_order.add_item('bogo_item', 1.00)
        self.checkout_order.add_item('bogo_item_2', 1.00)
        self.checkout_order.add_markdown('markdown_item', 0.50)
        self.checkout_order.add_markdown('markdown_weighted_item', 0.50)
        self.checkout_order.add_bogo_special('bogo_item', 1, 1, 100)
        self.checkout_order.add_bogo_special('bogo_item_2', 3, 2, 50)

    def tearDown(self):
        self.checkout_order = None

    def test_add_item(self):
        self.assertTrue(self.checkout_order.add_item('item3', 1))

    def test_add_markdown(self):
        self.assertTrue(self.checkout_order.add_markdown('item3', 0.50))

    def test_add_special(self):
        self.assertTrue(self.checkout_order.add_bogo_special('item3', 1, 1, 100))

    def test_scan_item(self):
        self.assertEqual(1.00, self.checkout_order.scan_item('item'))
        self.assertEqual(2.00, self.checkout_order.scan_item('item'))
        self.assertEqual(3.50, self.checkout_order.scan_item('second_item'))
        self.assertEqual(5.00, self.checkout_order.scan_item('second_item'))

    def test_scan_item_by_weight(self):
        self.assertEqual(1.00, self.checkout_order.scan_item_by_weight('weight_item', 1))
        self.assertEqual(2.10, self.checkout_order.scan_item_by_weight('weight_item', 1.1))
        self.assertEqual(3.60, self.checkout_order.scan_item_by_weight('second_weight_item', 1))
        self.assertEqual(5.25, self.checkout_order.scan_item_by_weight('second_weight_item', 1.1))

    def test_scan_item_with_markdown(self):
        self.assertEqual(0.50, self.checkout_order.scan_item('markdown_item'))
        self.assertEqual(1.00, self.checkout_order.scan_item_by_weight('markdown_weighted_item', 1))
        self.assertEqual(1.50, self.checkout_order.scan_item('markdown_item'))
        self.assertEqual(2.25, self.checkout_order.scan_item_by_weight('markdown_weighted_item', 1.5))

    def test_get_item_value(self):
        self.assertEqual(1.00, self.checkout_order.get_item_value('item'))
        self.assertEqual(1.50, self.checkout_order.get_item_value('second_item'))
        self.assertEqual(0.50, self.checkout_order.get_item_value('markdown_item'))

    def test_get_order(self):
        item_one = {
            'name': 'item',
            'value': 1.00,
        }
        item_two = {
            'name': 'second_item',
            'value': 1.50,
        }
        item_three = {
            'name': 'weight_item',
            'value': 1.00
        }

        self.checkout_order.scan_item('item')
        self.assertEqual([item_one], self.checkout_order.get_order())
        self.checkout_order.scan_item('second_item')
        self.assertEqual([item_one, item_two], self.checkout_order.get_order())
        self.checkout_order.scan_item('item')
        self.assertEqual([item_one, item_two, item_one], self.checkout_order.get_order())
        self.checkout_order.scan_item_by_weight('weight_item', 1)
        self.assertEqual([item_one, item_two, item_one, item_three], self.checkout_order.get_order())

    def test_get_order_total(self):
        self.assertEqual(0.00, self.checkout_order.get_order_total())

    def test_scan_item_with_bogo_style_special(self):
        self.assertEqual(1.00, self.checkout_order.scan_item('bogo_item'))
        self.assertEqual(1.00, self.checkout_order.scan_item('bogo_item'))
        self.assertEqual(2.00, self.checkout_order.scan_item('bogo_item'))
        self.assertEqual(2.00, self.checkout_order.scan_item('bogo_item'))
        self.assertEqual(3.00, self.checkout_order.scan_item('bogo_item2'))
        self.assertEqual(4.00, self.checkout_order.scan_item('bogo_item2'))
        self.assertEqual(5.00, self.checkout_order.scan_item('bogo_item2'))
        self.assertEqual(5.00, self.checkout_order.scan_item('bogo_item2'))
        self.assertEqual(5.00, self.checkout_order.scan_item('bogo_item2'))


if __name__ == 'main':
    unittest.main()
