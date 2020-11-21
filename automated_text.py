"""Step 1: [Text Messages] Have a Collection of preset Messages We can send 
my_messages = [" ", " "]"""

GOOD_MORNING_QUOTES = [
    "Good Morning!"
    "Howdy!"
    "What's up?"
]


from twilio.rest import Client
import schedule
import random

cellphone = 123
twilio_number = 234

def send_message(quote):
    account = ""
    token = ""
    client = Client(account, token)

    client.messages.create(to=cellphone,
                            from = twilio_number,
                            body=quote)

quote = GOOD_MORNING_QUOTES[random.randint(0, len(GOOD_MORNING_QUOTES))]
schedule.every().day.at("10:30").do(send_message, GOOD_MORNING_QUOTES[0])
