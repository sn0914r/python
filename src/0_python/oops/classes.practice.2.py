"""
E-commerce Cart System
"""


class Cart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price):
        if item in self.items:
            self.items[item]["qty"] += 1
            return True
        self.items[item] = {"price": price, "qty": 1}
        return True

    def remove_item(self, item):
        if item not in self.items:
            return False

        del self.items[item]
        return True

    def get_total(self, discount=None):
        total = sum([v["price"] * v["qty"] for v in self.items.values()])
        if discount is not None:
            return self.apply_discount(discount, total)
        return total

    def increase_qty(self, item):
        if item not in self.items:
            return False
        self.items[item]["qty"] += 1
        return True

    def decrease_qty(self, item):
        if item not in self.items:
            return False
        if self.items[item]["qty"] == 1:
            del self.items[item]
            return True
        self.items[item]["qty"] -= 1
        return True

    def display_cart(self):
        print(self.items)
        return None

    def get_total_items(self):
        return sum([v["qty"] for v in self.items.values()])

    def apply_discount(self, discount_percentage, total):
        return total - (discount_percentage / 100) * total


user1_cart = Cart()

user1_cart.add_item("apple", 100)
user1_cart.add_item("apple", 100)
user1_cart.add_item("banana", 200)

user1_cart.increase_qty("apple")

print(user1_cart.get_total())

# user1_cart.remove_item("apple")
# user1_cart.decrease_qty("banana")
# user1_cart.decrease_qty("bananas")

print(user1_cart.get_total_items())
print(user1_cart.get_total(10))
