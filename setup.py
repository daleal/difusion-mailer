"""
This module contains the classes and methods necessary to setup the mailer.
"""

import sys
import subprocess
from mailer import Mailer
from parameters import MAIL_SENDER

try:
    # Install dependencies
    with open('requirements.txt', 'r') as requirements:
        libraries = [x.strip() for x in requirements.readlines()]
    for library in libraries:
        subprocess.check_call(
            [sys.executable, '-m', 'pip', 'install', '--user', library])
    # Send testing email
    SENDER = Mailer()
    print('Sender has been created')
    MESSAGE = SENDER.create_text_message(MAIL_SENDER, MAIL_SENDER,
                                         'Testing', 'Everything set up')
    print('Message created')
    SENDER.send_message(MAIL_SENDER, MESSAGE)
    print('Message sent.')
except SystemExit as error:
    print(error)
