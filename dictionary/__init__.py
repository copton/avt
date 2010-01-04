from guppy import *
import database

class Dictionary(object):
    db = RequiredFeature("database", isInstanceOf(database.Database))
    def search(self, pattern):
        raise NotImplementedError()

    def release(self, words):
        raise NotImplementedError()
