class CheckoutOrder:
    def __init__(self):
        self.__items = {}
        self.__markdowns = {
            'markdown_item': 0.50,
            'markdown_weighted_item': 0.50,
        }
        self.__order = []

    def add_item(self, item, value):
        flag = False

        if item not in self.__items:
            self.__items[item] = value
            flag = True

        return flag

    def add_markdown(self, item, value):
        flag = False

        if item not in self.__markdowns:
            self.__markdowns[item] = value
            flag = True

        return flag

    def scan_item(self, item):
        self.__order.append({'name': item, 'value': self.get_item_value(item)})
        return self.get_order_total()

    def scan_item_by_weight(self, item, weight):
        self.__order.append({'name': item, 'value': self.get_item_value(item, weight)})
        return self.get_order_total()

    def get_markdown(self, item):
        return self.__markdowns[item] if item in self.__markdowns else 0

    def get_item_value(self, item, weight=1):
        return (self.__items[item] - self.get_markdown(item)) * weight

    def get_order(self):
        return self.__order

    def get_order_total(self):
        total = 0.00

        for item in self.__order:
            total = total + item['value']

        return total
