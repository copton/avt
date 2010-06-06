import workflow
from ui import Menu, Option
import database
from guppy import *
import dictionary

class Workflow(workflow.Workflow):
    """edit local database"""

    dictionary = RequiredFeature("dictionary", isInstanceOf(dictionary.Dictionary))

    def _run(self):
        def add():
            contents = self.ui.textinput("enter new word (leave blank to quit)")
            if contents == "":
                return
            word = database.Word(contents, "")
            self.ui.edit(word)
            self.db.add(word)

        def edit():
            pattern = self.ui.textinput("which word do you want to edit?")
            matches = self.db.search(pattern)
            if matches == []:
                self.ui.textoutput("no matches found.")
                return

            idx, word = self._selectWord(matches)
            if word == None:
                return
                
            select = self.ui.play(Menu("what do you want to do?", [
                        ("edit", "e", self.ui.edit),
                        ("delete", "d", self.db.remove)
                    ], quit=True, default="e"))
            if select != Menu.quit:
                select(word)

        while True:
            select = self.ui.play(
                Menu("what do you want to do?", [
                    ("add new word", "n", add),
                    ("edit an existing word", "e", edit),
                        ], quit=True, default="n"))

            if select == Menu.quit:
                break
            else:
                select()
