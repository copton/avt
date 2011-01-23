import database
import dictionary
import workflow
from guppy import *
from ui import Menu, Option

class Workflow(workflow.Workflow):
    dictionary = RequiredFeature("dictionary", isInstanceOf(dictionary.Dictionary)) 
                
    def _run(self):
        while True:
            pattern = self.ui.textinput("please enter word (leave blank to quit)")
            if pattern == "":
                break

            self.ui.textoutput("searching local database:\n")
            words = self.db.search(pattern)
            if words == []:
                self.ui.textoutput("no matches found\n")
            else:
                idx, word = self._selectWord(words)
                if word != None:
                    word.lookupCnt += 1
                    self.ui.textoutput("increased lookup count for word '%s'\n" % word.contents)
                    continue

            self.ui.textoutput("searching dictionary:\n")
            words = self.dictionary.search(pattern)
            if words == []:
                self.ui.textoutput("no matches found\n")
            else: 
                idx, word = self._selectWord(words)
                if word != None:
                    self.ui.edit(word)
                    self.db.add(word)
                    self.ui.textoutput("added word '%s' to database\n" % word.contents)
