import os

config = {
    "database.connection_string" : "/%s/.voctrain+/database.sqlite" % os.environ["HOME"],
}
