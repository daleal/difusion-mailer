"""
This module contains the classes and methods necessary to send data through
a Google Mail as the main function of the mailer.
"""

import base64
from email.mime.text import MIMEText
from email.mime.text import MIMEMultipart
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from httplib2 import Http
from oauth2client import file, client, tools
from parameters import MAIL_SENDER


class Mailer:

    """This class allows the Gmail API to send mails."""

    # A great amount of the following code is from Google's documentation

    def __init__(self):
        scopes = 'https://www.googleapis.com/auth/gmail.send'
        store = file.Storage('credentials.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('client_secret.json', scopes)
            creds = tools.run_flow(flow, store)
        self.service = build('gmail', 'v1', http=creds.authorize(Http()))

    def send_message(self, user_id, message):
        """Sends the mail to :message: from :user_id:."""
        try:
            message = self.service.users().messages().send(
                userId=user_id, body=message).execute()
            print('Message id: {}'.format(message['id']))
            return message
        except HttpError as error:
            print('An error ocurred: {}'.format(error))

    @staticmethod
    def create_text_message(sender, sending_to, subject, body):
        """Returns a text message ready to be sent."""
        message = MIMEText(body)
        message['to'] = sending_to
        message['from'] = sender
        message['subject'] = subject
        mess = base64.urlsafe_b64encode(message.as_bytes())
        return {'raw': mess.decode('utf-8')}

    @staticmethod
    def create_attachments_message(sender, sending_to, subject, body, attach):
        """Returns a message with text and attachments."""
        message = MIMEMultipart()
        message['to'] = sending_to
        message['from'] = sender
        message['subject'] = subject
        msg = MIMEText(body)
        message.attach(msg)
        for attachment in attach:
            message.attach(attachment)
        return {'raw': base64.urlsafe_b64encode(message.as_string())}


if __name__ == '__main__':
    SENDER = Mailer()
    print('Sender has been created')
    MESSAGE = SENDER.create_text_message(MAIL_SENDER, MAIL_SENDER,
                                         'Testing', 'Everything set up')
    print('Message created')
    SENDER.send_message(MAIL_SENDER, MESSAGE)
    print('Message sent.')
