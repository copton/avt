import dictionary
from database import Word
import re
from guppy import *

class Dictionary(dictionary.Dictionary):
    dict_file = RequiredFeature("dictionary.trans_de_en.dict_file", isInstanceOf(str))

    def search(self, pattern):
        rep = re.compile(pattern)
        f = open(self.dict_file)
        res = []
        for line in f.readlines():
            if line.startswith('#'):
                continue
            try:
                de, en = line.split('::')
            except ValueError:
                continue
            de_parts = map(str.strip, de.split('|'))
            en_parts = map(str.strip, en.split('|'))
            for de, en in zip(de_parts, en_parts):
                for synonym in en.split(';'):
                    mo = rep.search(synonym)
                    if mo:
                        res.append(Word(synonym, de))

        f.close()
        return res
