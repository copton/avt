import os

config = {
    "database.connection_string" : "/%s/.voctrain+/database.pickle" % os.environ["HOME"],
    "dictionary.trans_de_en.dict_file" : "/usr/share/trans/de-en",
}
