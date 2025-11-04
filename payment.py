class Payment:
    def __init__(self):
        pass

    def pay(self, amount):
        return f'{amount} $ payment'


class CreditCardPayment(Payment):
    def pay(self, amount):
        print (super().pay(amount) + f' via credit card')

class PayPalPayment(Payment):
    def pay(self, amount):
        print (super().pay(amount) + f' via paypal')
    
class CryptoPayment(Payment):
    def pay(self, amount):
        print (super().pay(amount) + f' via crypto')
    
payment = Payment()
crypto_payment = CryptoPayment()
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

print (payment.pay(700))
crypto_payment.pay(1200)
credit_card_payment.pay(800)
paypal_payment.pay(2000)


