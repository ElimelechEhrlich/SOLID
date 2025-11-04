from abc import ABC, abstractmethod

class Payment:
    def __init__(self):
        pass
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCardPayment(Payment):
    def pay(self, amount):
        print (f'{amount} $ payment via credit card')

class PayPalPayment(Payment):
    def pay(self, amount):
        print (f'{amount} $ payment via paypal')
    
class CryptoPayment(Payment):
    def pay(self, amount):
        print (f'{amount} $ payment via crypto')
    

crypto_payment = CryptoPayment()
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()


crypto_payment.pay(1200)
credit_card_payment.pay(800)
paypal_payment.pay(2000)


