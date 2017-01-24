from email import message_from_string
from email.message import Message
from logging import getLogger

from bs4 import BeautifulSoup

logger = getLogger('parse_logger')


class HosgeldiMessage:
    def __init__(self, string):
        self.message = message_from_string(string)

    def get_link(self):
        if self.message.get_content_maintype() == 'text':
            soup = BeautifulSoup(self.message.get_payload(), 'html.parser')
            for strong in soup.find_all('strong'):
                if strong.string == 'Учить слова на французском':
                    return strong.parent.get('href')
