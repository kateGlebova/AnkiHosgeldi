#! /usr/bin/python3

import argparse
from logging import getLogger

from hmessage import HosgeldiMessage
from mail import Mailbox
from settings.base import languages, newsletter_from
from settings.local import host, username, password, csv_path

logger = getLogger('logger')


class Main:
    def __init__(self):
        self._from_args()
        self.mailbox = Mailbox(host, username, password)

    def _from_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument("language", choices=languages.keys(), help='specify the language you are learning')
        parser.add_argument("-d", help='delete processed messages', action="store_true")
        args = parser.parse_args()
        self.language = args.language
        self.delete = args.d

    def process_message(self, uid):
        logger.info('Into process_message: %s' % uid)
        message = HosgeldiMessage(self.mailbox.get_by_uid(uid), self.language)
        message.words_to_csv('{}hosgeldi_{}.csv'.format(csv_path, self.language))

    def run(self):
        uids = self.mailbox.get_uids_from(newsletter_from)

        logger.info("Have uids: %s" % uids)

        for uid in uids:
            self.process_message(uid)
            if self.delete:
                self.mailbox.delete(uid)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.mailbox.exit()

logger.info('In hosgeldi.py')
with Main() as main:
    main.run()
