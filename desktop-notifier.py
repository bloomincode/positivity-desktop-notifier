from notifypy import Notify
from random import randint
import time 
import requests

quoteData = None

try:
    quoteData = requests.get("https://type.fit/api/quotes")
except:
    print("400 Error")

if (quoteData != None):
    data = quoteData.json()
    # Max quotes returned is 300 - choose a random quote
    index = randint(1,300) 
    
    # Format of returned quotes is a 4-digit number prefixed with zeros
    if index < 10:
        index = "000" + str(index)
    elif index < 100:
        index = "00" + str(index)
    else:
        index = "0" + str(index)
   
    random_quote = data[int(index)]

    # Execute notification every hour 
    while True:
        notification = Notify()
        notification.title = "Daily Positivity"
        notification.message = random_quote['text']
        notification.audio = "./desktop-notifier/mixkit-positive-notification-951.wav"
        notification.send()

        #notification repeats every 1 hour
        time.sleep(60*60*1)