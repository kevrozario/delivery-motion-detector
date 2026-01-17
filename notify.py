import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()

def notify():
    message = Mail(
        from_email=os.getenv("from_email"),
        to_emails=os.getenv("to_emails"),
        subject='Delivery Arrived!',
        html_content='<strong>Check your front door</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
        
notify()