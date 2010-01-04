import os

config = {
    "database.connection_string" : "/%s/.voctrain+/database.sqlite" % os.environ["HOME"],
    "dictionary.trans_de_en.path" : "/usr/share/trans/de-en",
}
