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
        self.checkout_order.add_item('bundle_item', 2.00)
        self.checkout_order.add_markdown('markdown_item', 0.50)
        self.checkout_order.add_markdown('markdown_weighted_item', 0.50)
        self.checkout_order.add_bogo_special('bogo_item', 1, 1, 100, 3)
        self.checkout_order.add_bogo_special('bogo_item_2', 3, 2, 50)
        self.checkout_order.add_bundle_special('bundle_item', 2, 3)

    def tearDown(self):
        self.checkout_order = None

    def test_add_item(self):
        self.assertTrue(self.checkout_order.add_item('item3', 1))

    def test_add_markdown(self):
        self.assertTrue(self.checkout_order.add_markdown('item3', 0.50))

    def test_add_special(self):
        self.assertTrue(self.checkout_order.add_bogo_special('item3', 1, 1, 100, 3))
        self.assertTrue(self.checkout_order.add_bundle_special('item4', 2, 3))
        self.assertTrue(self.checkout_order.add_bogo_special('item5', 1, 1, 100))
        self.assertTrue(self.checkout_order.add_equality_special('item6', 'item7', 50))

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
        self.assertEqual(3.00, self.checkout_order.scan_item('bogo_item_2'))
        self.assertEqual(4.00, self.checkout_order.scan_item('bogo_item_2'))
        self.assertEqual(5.00, self.checkout_order.scan_item('bogo_item_2'))
        self.assertEqual(5.50, self.checkout_order.scan_item('bogo_item_2'))
        self.assertEqual(6.00, self.checkout_order.scan_item('bogo_item_2'))
        self.assertEqual(7.10, self.checkout_order.scan_item_by_weight('bogo_item', 1.1))
        self.assertEqual(7.10, self.checkout_order.scan_item_by_weight('bogo_item', 1.1))
        self.assertEqual(8.10, self.checkout_order.scan_item('bogo_item'))
        self.assertEqual(9.10, self.checkout_order.scan_item('bogo_item'))

    def test_scan_item_with_bundle_special(self):
        self.assertEqual(2.00, self.checkout_order.scan_item('bundle_item'))
        self.assertEqual(3.00, self.checkout_order.scan_item('bundle_item'))
        self.assertEqual(5.00, self.checkout_order.scan_item('bundle_item'))
        self.assertEqual(6.00, self.checkout_order.scan_item('bundle_item'))
        self.assertEqual(8.20, self.checkout_order.scan_item_by_weight('bundle_item', 1.1))
        self.assertEqual(9.00, self.checkout_order.scan_item_by_weight('bundle_item', 1.1))

    def test_scan_item_remove(self):
        self.checkout_order.add_item('bogo_weighted_item', 1.00)
        self.checkout_order.add_item('bundle_weighted_item', 2.00)
        self.checkout_order.add_bogo_special('bogo_weighted_item', 1, 1, 100, 3)
        self.checkout_order.add_bundle_special('bundle_weighted_item', 2, 3)

        self.assertEqual(1.00, self.checkout_order.scan_item('item'))
        self.assertEqual(2.00, self.checkout_order.scan_item('item'))

        # Remove last item
        self.assertEqual(1.00, self.checkout_order.scan_item_remove())

        self.assertEqual(2.00, self.checkout_order.scan_item('item'))
        self.assertEqual(3.50, self.checkout_order.scan_item('second_item'))
        self.assertEqual(5.00, self.checkout_order.scan_item('second_item'))

        # Remove the specific item via index
        self.assertEqual(3.50, self.checkout_order.scan_item_remove(2))
        self.assertEqual(2.50, self.checkout_order.scan_item_remove(1))

        self.assertEqual(3.50, self.checkout_order.scan_item('item'))
        self.assertEqual(5.00, self.checkout_order.scan_item('second_item'))
        self.assertEqual(6.00, self.checkout_order.scan_item('bogo_item'))
        self.assertEqual(6.00, self.checkout_order.scan_item('bogo_item'))
        self.assertEqual(7.00, self.checkout_order.scan_item('bogo_item'))
        self.assertEqual(7.00, self.checkout_order.scan_item('bogo_item'))
        self.assertEqual(8.00, self.checkout_order.scan_item('bogo_item_2'))
        self.assertEqual(9.00, self.checkout_order.scan_item('bogo_item_2'))
        self.assertEqual(10.00, self.checkout_order.scan_item('bogo_item_2'))
        self.assertEqual(10.50, self.checkout_order.scan_item('bogo_item_2'))
        self.assertEqual(11.00, self.checkout_order.scan_item('bogo_item_2'))
        self.assertEqual(12.10, self.checkout_order.scan_item_by_weight('bogo_weighted_item', 1.1))
        self.assertEqual(12.10, self.checkout_order.scan_item_by_weight('bogo_weighted_item', 1.1))
        self.assertEqual(13.10, self.checkout_order.scan_item('bogo_item'))
        self.assertEqual(13.10, self.checkout_order.scan_item('bogo_item'))
        self.assertEqual(15.10, self.checkout_order.scan_item('bundle_item'))
        self.assertEqual(16.10, self.checkout_order.scan_item('bundle_item'))
        self.assertEqual(18.10, self.checkout_order.scan_item('bundle_item'))
        self.assertEqual(19.10, self.checkout_order.scan_item('bundle_item'))
        self.assertEqual(21.30, self.checkout_order.scan_item_by_weight('bundle_weighted_item', 1.1))
        self.assertEqual(22.10, self.checkout_order.scan_item_by_weight('bundle_weighted_item', 1.1))

        # Remove items from a special
        # Remove first item from bundle specials by weight
        self.assertEqual(21.30, self.checkout_order.scan_item_remove(21))
        # Remove random bundle item not by weight
        self.assertEqual(20.30, self.checkout_order.scan_item_remove(19))
        # Remove a bogo item 2 entry
        self.assertEqual(19.80, self.checkout_order.scan_item_remove(9))
        # Remove a bogo item entry
        self.assertEqual(19.80, self.checkout_order.scan_item_remove(6))

    def test_scan_item_with_equality_special(self):
        self.checkout_order.add_item('purchased_item', 2)
        self.checkout_order.add_item('discounted_item', 2)
        self.checkout_order.add_equality_special('purchased_item', 'discounted_item', 50)
        self.assertEqual(3.00, self.checkout_order.scan_item_by_weight('purchased_item', 1.5))
        self.assertEqual(4.00, self.checkout_order.scan_item_by_weight('discounted_item', 1))


if __name__ == 'main':
    unittest.main()
