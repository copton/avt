import database
import dictionary
import workflow
from guppy import *
from ui import Menu, Option

class Workflow(workflow.Workflow):
    dictionary = RequiredFeature("dictionary", isInstanceOf(dictionary.Dictionary)) 

    def remove_duplicates(self, words):
        result = []
        def exists(word):
            for r in result:
                if word.contents == r.contents  \
                  and word.translation == r.translation:
                    return True
            return False

        for word in words:
            if not exists(word):
                result.append(word)
        return result
                
    def _run(self):
        while True:
            pattern = self.ui.textinput("please enter word (leave blank to quit)")
            if pattern == "":
                break

            words = self.db.search(pattern)
            db_idx = len(words)
            words += self.dictionary.search(pattern)

            if words == []:
                self.ui.textoutput("no matches found")
                continue
                 
            words = self.remove_duplicates(words)
            idx, word = self._selectWord(words)
            if word == None:
                continue

            if idx < db_idx:
                word.lookupCnt += 1
                self.ui.textoutput("increased lookup count for word '%s'\n" % word.contents)
                continue
        
            self.ui.edit(word)
            self.db.add(word)
            self.ui.textoutput("added word '%s' to database\n" % word.contents)
