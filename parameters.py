"""
This module contains the necessary parameters to make the mailer work.
"""


import json


# Para usar el mailer, rellenar con el mail a usar
MAIL_SENDER = ''

# Para usar el mailer, comentar las siguientes lineas
with open('mail.json', 'r') as metadata:
    MAIL_SENDER = json.load(metadata)['mail']
