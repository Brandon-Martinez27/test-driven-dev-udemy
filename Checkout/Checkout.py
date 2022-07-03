
class Checkout:
    class Discount:
        def __init__(self, numItems, price):
            self.numItems = numItems
            self.price = price

    def __init__(self):
        self.prices = {}
        self.discounts = {}
        self.items = {}

    def addDiscount(self, item, numItems, price):
        discount = self.Discount(numItems, price)
        self.discounts[item] = discount

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addItem(self, item):
        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, cnt in self.items.items():
            if item in self.discounts:
                discount = self.discounts[item]
                if cnt >= discount.numItems:
                    numDiscounts = cnt/discount.numItems
                    total += numDiscounts * discount.price
                    remaining = cnt % discount.numItems
                    total += remaining * self.prices[item]
                else:
                    total += self.prices[item] * cnt
            else:
                total += self.prices[item] * cnt
        return total



