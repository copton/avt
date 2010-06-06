from guppy import *

class Word(object):
    def __init__(self, contents, translation):
        self.contents = contents
        self.translation = translation
        self.sentences = []
        self.lookupCnt = 1
        self.rightCnt = 0
        self.wrongCnt = 0

#    def __repr__(self):
#        return "%s: %s (%d, %d, %d)" % (self.contents, self.translation, self.lookupCnt, self.rightCnt, self.wrongCnt)

class Database(object):
    connection_string = RequiredFeature("database.connection_string", isInstanceOf(str))

    def connect(self):
        """opens the database connection"""
        raise NotImplementedError()

    def flush(self):
        """flushes the current database to disk"""
        raise NotImplementedError()

    def add(self, word):
        """adds a word to the database"""
        raise NotImplementedError()

    def remove(self, word):
        """removes a word from the database"""
        raise NotImplementedError()

    def search(self, pattern):
        """returns a list of words that match the given regular expression"""
        raise NotImplementedError()
        
    def sort(self, compare):
        """return the list of all words, sorted in descending order according to the compare function"""
        raise NotImplementedError()
