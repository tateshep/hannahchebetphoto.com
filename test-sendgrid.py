import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
# print(SENDGRID_API_KEY)
message = Mail(
    from_email='hannahchebetphoto@gmail.com',
    to_emails='tateshep@gmail.com',
    subject='sending another mail with SendGrid',
    html_content='<strong>Hello Tate. Hope this works, from hannachebetphoto@gmail.com</strong>'
)
try:

    sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)
