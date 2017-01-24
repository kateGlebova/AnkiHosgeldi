import pytest

from hosgeldi_message import HosgeldiMessage


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

