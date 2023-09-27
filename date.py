from twilio.rest import Client
import datetime
# Twilio credentials
TWILIO_ACCOUNT_SID = 'AC19e960acf50b8e2670798c71c5ab595c'
TWILIO_AUTH_TOKEN = '940321ab39c30f334f8c95b68117c926'
YOUR_PHONE_NUMBER = '+918605320413'  # Your phone number where you want to receive notifications

# Dictionary to store dates and messages
important_dates = {
    '2023-09-20': "Ganapati Get",
    '2023-10-02': "Christmas",
    '2024-01-01': "New Year's Day",
}

# Function to send a text message
def send_sms(message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    
    try:
        message = client.messages.create(
            body=message,
            from_='+16364868046',  # Your Twilio phone number
            to='+918605320413'  # Your phone number
        )
        print(f"Message sent: {message.sid}")
    except Exception as e:
        print(f"Error sending message: {e}")

# Function to check for important dates and send messages
def check_dates():
    today = datetime.date.today()
    for date_str, message in important_dates.items():
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        if date == today:
            send_sms(f"Don't forget: {message} today!")

if __name__ == "__main__":
    check_dates()
