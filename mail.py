from email import message_from_string
from imaplib import IMAP4_SSL
from logging import getLogger

logger = getLogger('mail_logger')


class Mailbox:
    def __init__(self, host, username, password):
        try:
            self.mail = IMAP4_SSL(host)
            self.mail.login(username, password)
        except:
            logger.exception('An error occured while signing in.')
            exit(1)

    def go_to_folder(self, folder):
        result, data = self.mail.select(folder)
        if result == 'NO':
            self.mail.create(folder)
            self.mail.select(folder)

    def get_uids(self):
        result, data = self.mail.uid('search', None, "ALL")
        if result == 'OK':
            return data[0].split()
        return None

    def get_by_uid(self, uid):
        result, data = self.mail.uid('fetch', uid, '(RFC822)')
        if result == 'OK':
            return data[0][1].decode('utf-8')

    def copy_to_folder(self, uid, folder):
        self.mail.uid('copy', uid, folder)

    def delete(self, uid):
        self.mail.uid('store', uid, '+FLAGS', '\\Deleted')
        self.mail.expunge()

    def move_to_folder(self, uid, folder):
        self.copy_to_folder(uid, folder)
        self.delete(uid)

    def exit(self):
        self.mail.close()
        self.mail.logout()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.exit()
