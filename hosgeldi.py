import argparse

from hmessage import HosgeldiMessage
from mail import Mailbox
from settings.base import languages, newsletter_folder
from settings.local import host, username, password, csv_path

parser = argparse.ArgumentParser()
parser.add_argument("language", choices=languages.keys(), help='specify the language you are learning')
args = parser.parse_args()

mailbox = Mailbox(host, username, password)
mailbox.go_to_folder(newsletter_folder)

uids = mailbox.get_uids()
for uid in uids:
    message = HosgeldiMessage(mailbox.get_by_uid(uid), args.language)
    message.words_to_csv('{}hosgeldi_{}.csv'.format(csv_path, args.language))
