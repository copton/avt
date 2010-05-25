from guppy import *

class Word(object):
    __slots__=[
        "contents", # thw word itself
        "translation", # the translation of this word
        "sentences", # a list of examples sentences using this word
        "lookupCnt", # how many times this word waslooked up
        "rightCnt", # how many times the user knew this word
        "wrontCnt", # how many times the user did not know this word
    ]

    def __init__(self, contents, translation):
        self.contens = contents
        self.translation = translation
        self.sentences = []
        self.lookupCnt = 0
        self.rightCnt = 0
        self.wrontCont = 0

    def __repr__(self):
        return self.contents + ": " + self.translation

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
        """returns all words that match the given regular expression"""
        raise NotImplementedError()
        
