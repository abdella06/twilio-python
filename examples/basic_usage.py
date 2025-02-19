import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
from dotenv import load_dotenv
from twilio.rest import Client

# Load environment variables
load_dotenv()

# Twilio Credentials (from .env file)
ACCOUNT_SID = os.getenv("AC257df73df37631e0284e0fc675065502")
AUTH_TOKEN = os.getenv("8cbcbd6b5c5d1e63d9d305c7aebfc43f")
TWILIO_WHATSAPP_NUMBER = os.getenv("+14155238886")

client = Client(ACCOUNT_SID, AUTH_TOKEN)

app = Flask(__name__)

# Function to send WhatsApp messages
def send_whatsapp_message(to, message):
    client.messages.create(
        from_=TWILIO_WHATSAPP_NUMBER,
        to=to,
        body=message
    )

@app.route("/webhook", methods=["POST"])
def whatsapp_bot():
    incoming_msg = request.form.get("Body").strip().lower()
    sender = request.form.get("From")
    response = MessagingResponse()
    msg = response.message()

    # Define responses
    if "hello" in incoming_msg:
        msg.body("Hi! How can I help you?")
    elif "how are you" in incoming_msg:
        msg.body("I'm just a bot, but I'm good! What about you?")
    elif "how do you feel today" in incoming_msg:
        msg.body("I'm always ready to assist you! 😊")
    elif "give me your instagram" in incoming_msg:
        msg.body("You can follow me on Instagram: @your_instagram_handle")
    else:
        msg.body("I didn't understand that. Try asking about the weather, greetings, or my Instagram.")

    return str(response)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
