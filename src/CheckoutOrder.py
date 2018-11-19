class CheckoutOrder:
    def __init__(self):
        self.__value = 0.0
        self.__items = {}
        return

    def add_item(self, item, value):
        flag = False

        if item not in self.__items:
            self.__items[item] = value
            flag = True

        return flag


    def scan_item(self, item):
        self.__value = self.__value + (self.__items[item] - 0.5)
        return self.__value


    def scan_item_by_weight(self, item, weight):
        self.__value = self.__value + 1.00 * weight
        return self.__value
