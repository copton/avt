import os

config = {
    "database.connection_string" : "/%s/.voctrain+/database.pickle" % os.environ["HOME"],
    "dictionary.dict_file" : "/usr/share/trans/de-en",
}
