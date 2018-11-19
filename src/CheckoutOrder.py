class CheckoutOrder:
    def __init__(self):
        self.__value = 0.0
        self.__items = {}
        return

    def add_item(self, item, value):
        flag = False

        if item not in self.__items:
            flag = True

        return flag


    def scan_item(self, item):
        self.__value = self.__value + self.__items[item]
        return self.__value
