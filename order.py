class Order:
    def __init__(self, items:list[str], total_price:float):
        self.items = items
        self.total_price = total_price

class InvoicePrinter:
    def __init__(self):
        pass
    @staticmethod
    def print_invoice(order: Order):
        Item_number = 1
        for item in order.items:
            print (f'{Item_number}: {item}')
            Item_number += 1
        print (f'Total price: {order.total_price}')

a = Order(['milk', 'bread', 'shampoo'], 30)
b = InvoicePrinter().print_invoice(a)
b.print_invoice(a)
