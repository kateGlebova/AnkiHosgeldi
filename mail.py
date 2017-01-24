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

    # @staticmethod
    # def _message_to_tuple(message_obj):
    #     return message_obj['content-type'].split()[0], message_obj.get_payload()

    def get_by_uid(self, uid):
        result, data = self.mail.uid('fetch', uid, '(RFC822)')
        if result == 'OK':
            return data[0][1].decode('utf-8')
            # if letter.get_content_maintype() == 'multipart':
            #     [self._message_to_tuple(part) for part in letter.get_payload() if part.get_content_maintype() == 'text']
            # else:
            #     body.append(self._message_to_tuple(letter))

    def copy_to_folder(self, uid, folder):
        self.mail.uid('copy', uid, folder)

    def delete(self, uid):
        self.mail.uid('store', uid, '+FLAGS', '\\Deleted')
        self.mail.expunge()

    def move_to_folder(self, uid, folder):
        self.copy_to_folder(uid, folder)
        self.delete(uid)
