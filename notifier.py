from abc import ABC, abstractmethod

class Notifier:
    def __init__(self):
        pass
    @abstractmethod
    def send(self, message):
        pass
    
class EmailNotifier(Notifier):
    def send(self, message):
        print (f'send {message} to email')
    
class SMSNotifier(Notifier):
    def send(self, message):
        print (f'send {message} to SMS')
    
class WhatsappNotifier(Notifier):
    def send(self, message):
        print (f'send {message} to Whatsapp')

sms = SMSNotifier()
email = EmailNotifier()
whatsapp = WhatsappNotifier()
notifiers = [sms, email, whatsapp]
for notifier in notifiers:
    notifier.send('Hello!!')
    
