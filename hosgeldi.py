from email import message_from_string
from logging import getLogger

import requests
from bs4 import BeautifulSoup, element
from requests import RequestException

logger = getLogger('logger')


class HosgeldiMessage:
    def __init__(self, string):
        self.message = message_from_string(string)

    def get_link(self):
        '''

        :return: str | link to the page with 10 words in case of success
                 None otherwise
        '''
        if self.message.get_content_maintype() == 'text':
            soup = BeautifulSoup(self.message.get_payload(), 'html.parser')
            for strong in soup.find_all('strong'):

                if strong.string == 'Учить слова на французском':
                    return strong.parent.get('href')


class HosgeldiParser:
    _page = None
    _words = dict()

    def __init__(self, link):
        try:
            self._page = BeautifulSoup(requests.get(link).content, 'html.parser')
        except RequestException:
            logger.exception('Invalid link.')

    def get_words(self):
        if not self._words:
            self._parse_words()
        return self._words

    def _parse_words(self):
        if self._page:
            for li in self._page.find(id='myGallery'):
                if isinstance(li, element.Tag):
                    word = [p.get_text() for p in list(li.children)[3].find_all('p')]
                    self._words[word[0]] = word[1]
