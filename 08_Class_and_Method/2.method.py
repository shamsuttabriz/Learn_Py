class Phone:
    brand = 'xiaomi'
    features = ['20px front camera', '3200mAp battery']

    def call(self):
        print('ring ring ring')
    
    def sms(self, text, num):
        sms = f"Sending sms: {text} to: {num}"
        return sms

myPhone = Phone()
myPhone.call()
sms = myPhone.sms("I missed to miss you!", "01986884508")
print(sms)