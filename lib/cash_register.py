class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        transaction_amount = price * quantity
        self.total += transaction_amount
        self.items.extend([title] * quantity)
        self.last_transaction = transaction_amount

    def apply_discount(self):
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discounted_total = self.total * (1 - self.discount / 100)
            self.total = int(discounted_total)  # Convert to integer
            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        if self.last_transaction:
            self.total -= self.last_transaction
            if self.items:
                self.items.pop()
            self.last_transaction = 0