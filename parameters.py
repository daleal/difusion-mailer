"""
This module contains the necessary parameters to make the mailer work.
"""


import json


MAIL_COLUMN_NAME = 'mail'
DATABASE_LOCATION = ''
TARGET_DATABASE = 'mail_list.csv'
TEMPLATE_FILE = 'template.txt'
ATTACHMENTS_FOLDER = 'attachments'
DELIMITER = ';'
SKIPINITIALSPACE = False

# Para usar el mailer, rellenar con el mail a usar
MAIL_SENDER = ''

# Para usar el mailer, comentar las siguientes lineas
with open('mail.json', 'r') as metadata:
    MAIL_SENDER = json.load(metadata)['mail']
