class CheckoutOrder:
    def __init__(self):
        self.__value = 0.0
        self.__items = {}
        self.__markdowns = {
            'markdown_item': 0.5,
            'markdown_weighted_item': 0.5,
        }
        return

    def add_item(self, item, value):
        flag = False

        if item not in self.__items:
            self.__items[item] = value
            flag = True

        return flag


    def scan_item(self, item):
        markdown = self.__markdowns[item] if item in self.__markdowns else 0
        self.__value = self.__value + (self.__items[item] - markdown)
        return self.__value


    def scan_item_by_weight(self, item, weight):
        markdown = self.__markdowns[item] if item in self.__markdowns else 0
        self.__value = self.__value + ((1.00 - markdown) * weight)
        return self.__value
