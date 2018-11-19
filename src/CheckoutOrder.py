class CheckoutOrder:
    def __init__(self):
        self.__value = 0.0
        self.__items = {
            'item': 1.00,
            'second_item': 1.50,
        }
        return

    def add_item(self, item, value):
        flag = False

        if not self.__items[item]:
            flag = True

        return flag


    def scan_item(self, item):
        self.__value = self.__value + self.__items[item]
        return self.__value
