import database
import pickle
import os
import os.path
import re

class RAM(database.Database):
    def connect(self):
        conf_path = os.path.split(self.connection_string)[0]
        if not os.path.isdir(conf_path):
            os.mkdir(conf_path)
            self.words = []
        else:
            if os.path.isfile(self.connection_string):
                f = open(self.connection_string, "r")
                self.words = pickle.load(f)
            else:
                self.words = []

    def flush(self):
        f = open(self.connection_string, "w")
        pickle.dump(self.words, f)
        f.close()

    def add(self, word):
        self.words.append(word)

    def remove(self, word):
        for i in range(len(self.words)):
            if self.words[i] == word:
                self.words.pop(i)
                return

    def search(self, pattern):
        rep = re.compile(pattern)
        return [word for word in self.words if rep.match(word.contents)]

    def sort(self, compare):
        res = [w for w in self.words]
        res.sort(compare, reverse=True)
        return res
