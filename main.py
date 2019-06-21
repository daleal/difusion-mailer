"""
This module builds and executes the mailer system.
"""


import os
import sys
import csv
import requests
from mailer import Mailer
from data_getter import DataGetter
from parameters import (MAIL_SENDER, DATABASE_LOCATION, TARGET_DATABASE,
                        TEMPLATE_FILE, ATTACHMENTS_FOLDER, MAIL_COLUMN_NAME)


mailer = Mailer()
getter = DataGetter(DATABASE_LOCATION)


def get_mail_title():
    """Gets the title for the mail."""
    trailing = sys.argv[1:]
    return 'Sample Diffusion' if not trailing else " ".join(trailing)


def generate_message(template, subject, attachments, **kwargs):
    """Generates the adequate message depending on attachments."""
    text = template.format(**kwargs)
    if not attachments:
        return mailer.create_text_message(
            MAIL_SENDER, kwargs[MAIL_COLUMN_NAME], subject, text)
    return mailer.create_attachments_message(
        MAIL_SENDER, kwargs[MAIL_COLUMN_NAME], subject, text + '\n\n',
        attachments)


def send_message(message):
    """Sends the mail."""
    try:
        mailer.send_message(MAIL_SENDER, message)
    except requests.exceptions.ConnectionError:
        return {'worked': False}
    return {'worked': True}


if __name__ == '__main__':
    SUBJECT = get_mail_title()
    TEMPLATE = getter.get_template(TEMPLATE_FILE)
    DATABASE = getter.get_target_data(TARGET_DATABASE)
    ATTACHMENTS = getter.get_attachments(ATTACHMENTS_FOLDER)
    for TARGET in DATABASE:
        MESSAGE = generate_message(TEMPLATE, SUBJECT, ATTACHMENTS, **TARGET)
        STATUS = send_message(MESSAGE)
        if STATUS['worked']:
            print('Message sent to {} successfully!\n'.format(
                TARGET[MAIL_COLUMN_NAME]))
        else:
            print('Unable to send message to {}\n'.format(
                TARGET[MAIL_COLUMN_NAME]))
