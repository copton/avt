import database
import dictionary
import workflow
from guppy import *
from ui import Menu, Option

def select_word(words):
    menu = Menu("select word", quit=True, delim="\n", footer="\n")
    for i, word in enumerate(words):
        menu.addOption(Option(str(word), str(i), i))

    return menu

class Workflow(workflow.Workflow):
    dictionary = RequiredFeature("dictionary", isInstanceOf(dictionary.Dictionary)) 
    def _local_lookup(self, pattern):

        local_matches = self.db.search(pattern)

        if len(local_matches) == 0:
            self.ui.textoutput("no matches found in local database")
            return True

        if len(local_matches) == 1:
            select = 0
        else:
            select = self.ui.play(select_word(local_matches))
            if select == Menu.quit:
                return True

        word = local_matches[select]
        word.lookupCnt += 1
        self.ui.show(word)

        if self.ui.play(Menu("do you want to edit this word?", 
                        [("yes", "y", True), ("no", "n", False)], 
                        default="n",quit=False)) == True:
            self.ui.edit(word)
            
        return False

    def _dictionary_lookup(self, pattern):
        matches = self.dictionary.search(pattern):
          

    def _run(self):
        while True:
            pattern = self.ui.textinput("please enter word")
            self._local_lookup(pattern) && self._dictionary_lookup(pattern)
