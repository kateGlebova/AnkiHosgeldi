# -*- coding: utf-8 -*-
from subprocess import call

import sys
from aqt import mw
from aqt.utils import chooseList, askUser
from aqt.qt import *
from os.path import exists

path = u"/media/kate/D/stuff/anki_hosgeldi/"


def import_hosgeldi_csv():
    sys.path.append(path)
    from settings.base import languages
    languages_list = languages.keys()
    language = languages_list[chooseList('Choose the language', languages_list)]

    call_shell = ["%shosgeldi.py" % path, "%s" % language]

    delete = askUser('Do you want to delete processed mail?')
    if delete:
        call_shell.append("-d")

    call(call_shell)

    from settings.local import csv_path
    csv_file = u"{}hosgeldi_{}.csv".format(csv_path, language)
    if exists(csv_file):
        mw.handleImport(csv_file)


action = QAction("hosgeldi", mw)
action.triggered.connect(import_hosgeldi_csv)
mw.form.menuTools.addAction(action)
