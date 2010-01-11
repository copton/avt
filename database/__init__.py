from guppy import *

class Database(object):
    connection_string = RequiredFeature("database.connection_string", isInstanceOf(str))

    def connect(self):
        raise NotImplementedError()

    def flush(self):
        raise NotImplementedError()

    def createWord(self, contents, translation="", sentences=[], lookupCnt=1, rightCnt=0, wrongCnt=0):
        raise NotImplementedError()

    def updateWord(self, word, attr):
        raise NotImplementedError()

    def query_by_contents(self, contents):
        raise NotImplementedError()
