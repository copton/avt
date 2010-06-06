import dictionary
from database import Word
import re
from threading import Thread
from guppy import *

class Dictionary(dictionary.Dictionary):

    def __init__(self):
        startupNotification(self.startup)

    def startup(self):
        self.source = Source()

    def search(self, pattern):
        entries = self.source.getEntries()
        rep = re.compile(pattern)
        
        res = []
        for entry in entries:
            for word in entry.en:
                mo = rep.search(word)
                if mo:
                    res.append(Word(word, "|".join(entry.de)))
        return res

class Entry(object):
    __slots__ = ["de", "en"]
    def __init__(self, de, en):
        self.de = de
        self.en = en

class Source(Thread):
    dict_file = RequiredFeature("dictionary.dict_file", isInstanceOf(str))

    def __init__(self):
        Thread.__init__(self)
        self.entries = []
        self.daemon = True
        self.start()

    def getEntries(self):
        self.join()
        return self.entries 

    def run(self):
        f = open(self.dict_file)
        for line in f.readlines():
            if line.startswith('#'):
                continue
            try:
                de, en = line.split('::')
            except ValueError:
                continue
            de_parts = map(str.strip, de.split('|'))
            en_parts = map(str.strip, en.split('|'))
            self.entries.append(Entry(de_parts, en_parts))

        f.close()
