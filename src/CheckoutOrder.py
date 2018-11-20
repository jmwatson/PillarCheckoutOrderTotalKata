class CheckoutOrder:
    def __init__(self):
        self.__items = {}
        self.__markdowns = {}
        self.__specials = {}
        self.__order = []

    def add_item(self, item, value):
        return self.add_to_data_store(self.__items, item, value)

    def add_markdown(self, item, value):
        return self.add_to_data_store(self.__markdowns, item, value)

    def add_bogo_special(self, item, count, special_count, percent_off):
        entry = {
                'count': count,
                'special_count': special_count,
                'percent_off': percent_off,
            }
        return self.add_to_data_store(self.__specials, item, entry)

    @staticmethod
    def add_to_data_store(dictionary, key, value):
        flag = False

        if key not in dictionary:
            dictionary[key] = value
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

    def get_special_value(self, item, count):
        name = item['name']
        count[name] = 1 if name not in count else count[name] + 1

        if name in self.__specials:
            min_count = self.__specials[name]['count']
            max_count = min_count + self.__specials[name]['special_count']

            if min_count < count[name] <= max_count:
                # 100.0 is to force python to run the percentage calculation as a float rather than an integer.
                value = item['value'] - (item['value'] * self.__specials[name]['percent_off'] / 100.0)

                if count[name] == max_count:
                    count[name] = 0
            else:
                value = item['value']
        else:
            value = item['value']

        return value

    def get_order(self):
        return self.__order

    def get_order_total(self):
        total = 0.00
        count = {}

        for item in self.__order:
            total += self.get_special_value(item, count)

        return total
