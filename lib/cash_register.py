class CashRegister:
    def __init__(self, discount=0):
        self.total = 0.0
        self.items = []
        self.discount = discount  # renamed to match test expectation
        self.last_transaction_amount = 0.0
        self.last_transaction_quantity = 0
        self.last_transaction_title = None

    def add_item(self, title, price, quantity=1):
        total_price = price * quantity
        self.total += total_price

        for _ in range(quantity):
            self.items.append(title)

        # Track last transaction details
        self.last_transaction_amount = total_price
        self.last_transaction_quantity = quantity
        self.last_transaction_title = title

    def apply_discount(self):
        if self.discount != 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
          print("There is no discount to apply.")


    def void_last_transaction(self):
        # Remove last transaction from total
        self.total -= self.last_transaction_amount

        # Remove last transaction items
        for _ in range(self.last_transaction_quantity):
            if self.last_transaction_title in self.items:
                self.items.remove(self.last_transaction_title)
