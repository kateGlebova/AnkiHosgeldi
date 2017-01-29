import csv
from email import message_from_string
from logging import getLogger

import requests
from bs4 import BeautifulSoup, element
from requests import RequestException

from settings.base import languages

logger = getLogger('logger')


class HosgeldiMessage:
    _page = None

    def __init__(self, string, language):
        self.language = language
        self._message = message_from_string(string)
        self._page = self.get_page()
        self._words = dict()

    def get_link(self):
        if self._message.get_content_maintype() == 'text':
            soup = BeautifulSoup(self._message.get_payload(), 'html.parser')
            for strong in soup.find_all('strong'):
                if strong.string == languages.get(self.language):
                    return strong.parent.get('href')

    def get_page(self):
        if self._page:
            return self._page
        try:
            return BeautifulSoup(requests.get(self.get_link()).content, 'html.parser')
        except RequestException:
            logger.exception('Invalid link.')

    def get_words(self):
        if not self._words:
            self._parse_words()
        return self._words

    def words_to_csv(self, file):
        if self.get_words():
            with open(file, 'a') as f:
                writer = csv.writer(f)
                for word, translation in self._words.items():
                    writer.writerow([word, translation])

    def _parse_words(self):
        if self._page:
            for li in self._page.find(id='myGallery'):
                if isinstance(li, element.Tag):
                    word = [p.get_text() for p in list(li.children)[3].find_all('p')]
                    self._words[word[0]] = word[1]
