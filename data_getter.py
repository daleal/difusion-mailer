"""
This module contains the classes and methods necessary to get every piece
of data needed to generate a mail message.
"""


import os
import csv
import mimetypes
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.application import MIMEApplication
from parameters import DATABASE_LOCATION, ATTACHMENTS_FOLDER


class DataGetter:

    """Serves as a collector for every piece of data."""

    def __init__(self, path):
        self.data_path = os.path.normpath(path)

    def __get_path(self, adyacent_path):
        """Creates a normpath given an adyacent path."""
        return os.path.normpath(self.data_path + '/' + adyacent_path)

    def __get_file_paths(self, folder_name):
        """
        Gets a dictionary with the name of every file as keys and the path
        of every file as values.
        """
        folder = self.__get_path(folder_name)
        if not os.path.exists(folder):
            return []
        return [os.path.join(folder, x) for x in os.listdir(folder)]

    @staticmethod
    def __get_file_types(file_path):
        """Returns the main type and the sub type of a file."""
        content_type, encoding = mimetypes.guess_type(file_path)
        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'
        return content_type.split('/', 1)

    def __generate_file(self, file_path):
        """Generates the file."""
        main_type, sub_type = self.__get_file_types(file_path)
        if main_type == 'text':
            fp = open(file_path, 'rb')
            msg = MIMEText(fp.read(), _subtype=sub_type)
            fp.close()
        elif main_type == 'application':
            fp = open(file_path, 'rb')
            msg = MIMEApplication(fp.read(), _subtype=sub_type)
            fp.close()
        elif main_type == 'image':
            fp = open(file_path, 'rb')
            msg = MIMEImage(fp.read(), _subtype=sub_type)
            fp.close()
        elif main_type == 'audio':
            fp = open(file_path, 'rb')
            msg = MIMEAudio(fp.read(), _subtype=sub_type)
            fp.close()
        else:
            fp = open(file_path, 'rb')
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(fp.read())
            fp.close()
        filename = os.path.basename(file_path)
        msg.add_header('Content-Disposition', 'attachment', filename=filename)
        return msg

    def get_target_data(self, database_filename):
        """Loads the database."""
        path = self.__get_path(database_filename)
        with open(path, 'r', encoding='utf-8-sig') as database:
            dat = csv.DictReader(database, delimiter=';')
            data = [x for x in map(dict, dat)]
        return data

    def get_template(self, template_filename):
        """Loads the mail template from file."""
        path = self.__get_path(template_filename)
        with open(path, 'r', encoding='utf-8') as raw_template:
            template = raw_template.read()
        return template.strip()

    def get_attachments(self, folder_name):
        """Loads the mail attachments."""
        paths = self.__get_file_paths(folder_name)
        return [self.__generate_file(x) for x in paths]


if __name__ == '__main__':
    DATA_GETTER = DataGetter(DATABASE_LOCATION)
    print(DATA_GETTER.get_attachments(ATTACHMENTS_FOLDER))
