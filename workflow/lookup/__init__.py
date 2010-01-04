import workflow
from ui import Menu, Option
import dictionary
from guppy import *

def select_word(words):
    menu = Menu("select word", quit=True, delim="\n", footer="\n")
    for i, word in enumerate(words):
        menu.addOption(Option(str(word), str(i), i))

    return menu
     

class Workflow(workflow.Workflow):
    dictionary = RequiredFeature("dictionary", isInstanceOf(dictionary.Dictionary))

    def _process_matches(self, matches):
        if len(matches) == 0:
            return None

        if len(matches) == 1:
            self.ui.textoutput("found " + str(word))
            select = 0
        else:
            select = self.ui.play(select_word(matches))
            if select == Menu.quit:
                return None

        word = matches[select]
        word.lookupCnt += 1

        if self.ui.play(Menu("do you want to edit this word?", 
                        [("yes", "y", True), ("no", "n", False)], 
                        default="n", quit=False)):
            self.ui.edit(word)

        return select

    def db_lookup(self, pattern):
        Word = self.db.Word()
        matches = Word.query.filter(Word.contents.like(unicode(pattern))).all()
        return self._process_matches(matches) != None

    def dict_lookup(self, pattern):
        matches = self.dictionary.search(pattern)
        print "###", matches
        select = self._process_matches(matches)
        if select != None:
            matches.pop(select)
        self.dictionary.release(matches) 

        return select != None 

    def _run(self):

        while True:
            pattern = self.ui.textinput("please enter word ('%' is wildcard. Leave empty to quit.)")
            if pattern == "":
                return
            
            if self.db_lookup(pattern):
                continue
            if self.dict_lookup(pattern):
                continue
            self.ui.textoutput("not matches found")
            
