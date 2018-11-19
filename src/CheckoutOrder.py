class CheckoutOrder:
    def __init__(self):
        self.__value = 0.0
        return

    def add_item(self, item, value):
        return True


    def scan_item(self, item):
        self.__value = self.__value + 1.00
        return self.__value
