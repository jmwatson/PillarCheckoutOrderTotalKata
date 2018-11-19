class CheckoutOrder:
    def __init__(self):
        self.__value = 0.00
        self.__items = {}
        self.__markdowns = {
            'markdown_item': 0.50,
            'markdown_weighted_item': 0.50,
        }

    def add_item(self, item, value):
        flag = False

        if item not in self.__items:
            self.__items[item] = value
            flag = True

        return flag

    def scan_item(self, item):
        self.__value = self.__value + self.get_item_value(item)
        return self.__value

    def scan_item_by_weight(self, item, weight):
        self.__value = self.__value + ((self.__items[item] - self.get_markdown(item)) * weight)
        return self.__value

    def get_markdown(self, item):
        return self.__markdowns[item] if item in self.__markdowns else 0

    def get_item_value(self, item):
        return self.__items[item] - self.get_markdown(item)
