import os
import requests
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import random

SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

def send_email(event, context):
    rand_quote = get_quote()
    email_html = create_email_html(rand_quote)
    subs = get_subs()

    emails = [d['S'] for d in subs]

    # Convert list to tuple
    # email_tuple = tuple(emails)

    message = Mail(
        from_email='rakesh.kumar@gmail.com',
        to_emails=emails,
        subject='[Daily Words of Wisdom by Amish]',
        html_content=email_html
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
    except Exception as e:
        return {
            'statusCode': 500,
            'body': str(e)
        }

    return {
        'statusCode': 200,
        'body': 'OK'
    }

def get_subs():
    response = requests.get('https://5esuy8dfdfaa6sr2l.execute-api.us-east-1.amazonaws.com/dev/subscribers')
    subscribers = response.json()
    return [sub['email'] for sub in subscribers]

def get_quote():
    response = requests.get('https://5reuyssadsa86sr2l.execute-api.us-east-1.amazonaws.com/dev/quotes')
    quotes = response.json()['quotes']
    random_quote = random.choice(quotes)
    return random_quote

def create_email_html(rand_quote):
    return f"""
    <!DOCTYPE html">
    <html lang="en">
    <body>
      <div class="container" style="min-height: 40vh; padding: 0 0.5rem; display: flex; flex-direction: column; justify-content: center; align-items: center;"> 
        <div class="card" style="margin-left: 20px; margin-right: 20px;">
          <div style="font-size: 14px;">
            <div class='card' style="background: #f0c5c5; border-radius: 5px; padding: 1.75rem; font-size: 1.1rem; font-family: Menlo, Monaco, Lucida Console, Liberation Mono, DejaVu Sans Mono, Bitstream Vera Sans Mono, Courier New, monospace;">
              <p>{rand_quote['quote']}</p>
              <blockquote>by {rand_quote['author']}</blockquote>
            </div>
            <br>
          </div>
          <div class="footer-links" style="display: flex; justify-content: center; align-items: center;">
            <a href="/" style="text-decoration: none; margin: 8px; color: #9CA3AF;">Unsubscribe?</a>
            <a href="/" style="text-decoration: none; margin: 8px; color: #9CA3AF;">About Us</a>
          </div>
        </div>
      </div>
    </body>
    </html>
    """
