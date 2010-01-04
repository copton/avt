import dictionary
from guppy import *
import re

class Dictionary(dictionary.Dictionary):
    path = RequiredFeature("dictionary.trans_de_en.path", isInstanceOf(str))

    def release(self, words):
        for word in words:
            word.delete()

    def search(self, pattern):
        regex = re.compile(pattern)
        Word = self.db.Word()
        Translation = self.db.Translation()

        f = open(self.path, "r")
        res = []
        for line in f.readlines():
            if line.startswith('#'):
                continue
            parts = line.split('::')
            if len(parts) != 2:
                continue
            
            de, en = parts
            if regex.search(en):
                de_parts = map(str.strip, de.split('|'))
                en_parts = map(str.strip, en.split('|'))
                assert len(de_parts) == len(en_parts)
                for i in range(len(de_parts)):
                    trans = Translation(contents = de_parts[i])
                    word = Word(contents = en_parts[i], translation = trans)
                    res.append(word)

        return res
