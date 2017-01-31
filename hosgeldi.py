#! /usr/bin/python3

import argparse

from hmessage import HosgeldiMessage
from mail import Mailbox
from settings.base import languages, newsletter_folder
from settings.local import host, username, password, csv_path


class Main:
    def __init__(self):
        self._language_from_args()
        self.mailbox = Mailbox(host, username, password)

    def _language_from_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("language", choices=languages.keys(), help='specify the language you are learning')
        args = parser.parse_args()
        self.language = args.language

    def process_message(self, uid):
        message = HosgeldiMessage(self.mailbox.get_by_uid(uid), self.language)
        message.words_to_csv('{}hosgeldi_{}.csv'.format(csv_path, self.language))

    def run(self):
        self.mailbox.go_to_folder(newsletter_folder)

        uids = self.mailbox.get_uids()

        for uid in uids:
            self.process_message(uid)


Main().run()
