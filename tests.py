import pytest

from hosgeldi import HosgeldiMessage
from mail import Mailbox


@pytest.fixture()
def mailbox():
    from settings.local import host, username, password
    with Mailbox(host, username, password) as mail:
        yield mail


@pytest.fixture
def message():
    with open('test_mail.txt', 'r') as f:
        f.readline()
        data = f.read()
    return data


def test_get_link(test_message):
    with open('test_mail.txt', 'r') as f:
        test_link = f.readline().strip()
    assert HosgeldiMessage(test_message).get_link() == test_link
