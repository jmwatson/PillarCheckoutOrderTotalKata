class CheckoutOrder:
    def __init__(self):
        self.__items = {}
        self.__markdowns = {}
        self.__specials = {}
        self.__order = []
        self.__total = 0.0

    def add_item(self, item, value):
        return self.add_to_data_store(self.__items, item, value)

    def add_markdown(self, item, value):
        return self.add_to_data_store(self.__markdowns, item, value)

    def add_bogo_special(self, item, count, special_count, percent_off):
        if 'bogo' not in self.__specials:
            self.add_to_data_store(self.__specials, 'bogo', {})

        entry = {
                'count': count,
                'special_count': special_count,
                'percent_off': percent_off,
            }
        return self.add_to_data_store(self.__specials['bogo'], item, entry)

    def add_bundle_special(self, item, count, price):
        if 'bundle' not in self.__specials:
            self.add_to_data_store(self.__specials, 'bundle', {})

        entry = {
            'count': count,
            'price': price
        }
        return self.add_to_data_store(self.__specials['bundle'], item, entry)

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

    def get_bogo_value(self, item, name, value, count):
        bogos = self.__specials['bogo']
        min_count = bogos[name]['count']
        max_count = min_count + bogos[name]['special_count']

        if min_count < count[name] <= max_count:
            # 100.0 is to force python to run the percentage calculation as a float rather than an integer.
            value = item['value'] - (item['value'] * bogos[name]['percent_off'] / 100.0)

            if count[name] == max_count:
                count[name] = 0

        return value

    def handle_bundle_specials(self, name, value, count):
        bundles = self.__specials['bundle']

        if bundles[name]['count'] == count[name]:
            self.__total -= value * (count[name] - 1)
            value = bundles[name]['price']
            count[name] = 0

        return value

    def get_order(self):
        return self.__order

    def get_order_total(self):
        self.__total = 0.00
        count = {}

        for item in self.__order:
            name = item['name']
            value = item['value']
            count[name] = 1 if name not in count else count[name] + 1

            if 'bogo' in self.__specials and name in self.__specials['bogo']:
                value = self.get_bogo_value(item, name, value, count)
            elif 'bundle' in self.__specials and name in self.__specials['bundle']:
                value = self.handle_bundle_specials(name, value, count)

            self.__total += value;

        return self.__total
