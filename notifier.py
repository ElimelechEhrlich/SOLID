from abc import ABC, abstractmethod

class Notifier:
    def __init__(self):
        pass
    @abstractmethod
    def send(self, message):
        pass
    
class EmailNotifier(Notifier):
    def send(self, message):
        print (f'send a email "{message}"')
    
class SMSNotifier(Notifier):
    def send(self, message):
        print (f'send a SMS "{message}"')
    
class PushNotifier(Notifier):
    def send(self, message):
        print (f'send a push "{message}"')

sms = SMSNotifier()
email = EmailNotifier()
push = PushNotifier()
notifiers = [sms, email, push]
for notifier in notifiers:
    notifier.send('Hello!!')
    
