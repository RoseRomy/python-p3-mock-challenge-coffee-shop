class Coffee:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self._orders = []

    def orders(self):
        return self._orders

    def add_order(self, order):
        if order not in self._orders:
            self._orders.append(order)

    def average_price(self):
        if not self._orders:
            return 0  # Return 0 if there are no orders

        total_price = sum(order.coffee.price *
                          order.quantity for order in self._orders)
        total_quantity = sum(order.quantity for order in self._orders)

        if total_quantity == 0:
            return 0

        return total_price / total_quantity


class Customer:
    def __init__(self, name):
        self.name = name

    def orders(self):
        pass

    def coffees(self):
        pass

    def create_order(self, coffee, price):
        pass


class Order:
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
