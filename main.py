"""
This module builds and executes the mailer system.
"""


import sys
import csv
import requests
from mailer import Mailer
from parameters import MAIL_SENDER


mailer = Mailer()


def get_target_data():
    """Loads the database."""
    with open('mail_list.csv', 'r', encoding='utf-8-sig') as database:
        dat = csv.DictReader(database, skipinitialspace=True)
        data = [x for x in map(dict, dat)]
    return data


def get_mail_title():
    """Gets the title for the mail."""
    trailing = sys.argv[1:]
    return 'Sample Diffusion' if not trailing else " ".join(trailing)


def get_template():
    """Loads the mail template from txt file."""
    with open('template.txt', 'r', encoding='utf-8') as raw_template:
        template = raw_template.read()
    return template.strip()


def send_report(template, subject, **kwargs):
    """
    Generates the message with the necessary information and sends the mail.
    """
    text = template.format(name=kwargs['name'],
                           last_name=kwargs['last_name'],
                           enterprise=kwargs['enterprise'])
    message = mailer.create_text_message(
        MAIL_SENDER, kwargs['mail'], subject, text)
    try:
        mailer.send_message(MAIL_SENDER, message)
    except requests.exceptions.ConnectionError:
        return {'worked': False}
    return {'worked': True}


if __name__ == '__main__':
    SUBJECT = get_mail_title()
    TEMPLATE = get_template()
    DATABASE = get_target_data()
    for TARGET in DATABASE:
        STATUS = send_report(TEMPLATE, SUBJECT, **TARGET)
        if STATUS['worked']:
            print('Message sent to {} successfully!\n'.format(TARGET['mail']))
        else:
            print('Unable to send message to {}\n'.format(TARGET['mail']))
