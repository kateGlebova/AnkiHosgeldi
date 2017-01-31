# -*- coding: utf-8 -*-
from subprocess import call

import sys
from aqt import mw
from aqt.utils import chooseList
from aqt.qt import *
from os.path import exists

path = u"/media/kate/D/stuff/anki_hosgeldi/"


def import_hosgeldi_csv():
    sys.path.append(path)
    from settings.base import languages
    languages_list = languages.keys()
    language = languages_list[chooseList('Choose the language', languages_list)]

    call(["%shosgeldi.py" % path, "%s" % language])

    csv_file = u"{}hosgeldi_{}.csv".format(path, language)
    if exists(csv_file):
        mw.handleImport(csv_file)


action = QAction("hosgeldi", mw)
action.triggered.connect(import_hosgeldi_csv)
mw.form.menuTools.addAction(action)