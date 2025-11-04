class Order:
    def __init__(self, items, total_price):
        self.items = items
        self.total_price = total_price

    def print_invoice(self):
        print (f'{self.items}: {self.total_price}')

class InvoicePrinter:
    def __init__(self):
        pass
    @staticmethod
    def print_invoice(order: Order):
        print (f'{order.items}: {order.total_price}')