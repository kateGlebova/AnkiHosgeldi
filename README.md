# Hosgeldi newsletter

You can subscribe to https://hosgeldi.com/ newsletter that every day sends you 10 words of the language you are learning.
## Requirements

1. Linux
2. Python 3
3. Anki desktop application


## Getting started

1. If you are using Gmail, allow [access for less secure apps](https://www.google.com/settings/security/lesssecureapps).

2. Create the file local.py in *settings* directory.

3. Specify there `host`, `username` and `password` of your mailbox and a `csv_path` to the directory where you want to store csv file according to *local.py.example*.

4. Specify the path to your Python 3 interpreter in the first line of hosgeldi.py file.

5. Specify the `path` to this project in the file hanki.py.

6. Copy file hanki.py to the folder with Anki addons (usually it's /home/username/Documents/Anki/addons)

If you want to change available languages, modify the dictionary `languages` in settings/base.py.

## Usage

1. Run Anki app.
2. Tools -> hosgeldi.
3. Choose the language.
4. Choose whether you want to delete processed messages.
5. Choose Type and Deck.
6. Click Import.

