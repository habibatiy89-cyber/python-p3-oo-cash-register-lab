class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        self.last_transaction = price * quantity
        self.total += self.last_transaction
        for _ in range(quantity):
            self.items.append(title)

    def apply_discount(self):
        """Applies discount and prints a message instead of returning"""
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        """Removes last transaction from total and items"""
        if self.last_transaction > 0:
            # Remove items from last transaction
            items_to_remove = int(self.last_transaction / (self.last_transaction / len(self.items) if self.items else 1))
            for _ in range(items_to_remove):
                if self.items:
                    self.items.pop()
            self.total -= self.last_transaction
            if self.total < 0:
                self.total = 0
            self.last_transaction = 0
