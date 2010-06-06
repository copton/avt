import workflow
from ui import Menu, Option
import database

class Workflow(workflow.Workflow):
    """edit local database"""

    def _run(self):
        def edit(words):
            idx, word = self._selectWord(words)
            if word == None:
                return 

            select = self.ui.play(Menu("what do you want to do?", [
                        ("edit", "e", self.ui.edit),
                        ("delete", "d", self.db.remove)
                    ], quit=True, default="e"))
            if select != Menu.quit:
                select(word)

        def add():
            contents = self.ui.textinput("enter new word (leave blank to quit)")
            if contents == "":
                return
            word = database.Word(contents, "")
            self.ui.edit(word)
            self.db.add(word)

        def listWords():
            def compare(lhs, rhs):
                return lhs.contents < rhs.contents 
            words = self.db.sort(compare)
            edit(words)

        def search():
            pattern = self.ui.textinput("enter pattern")
            matches = self.db.search(pattern)
            if matches == []:
                self.ui.textoutput("no matches found.")
                return
            edit(matches)
            
        while True:
            select = self.ui.play(
                Menu("what do you want to do?", [
                    ("add new word", "n", add),
                    ("search a word", "s", search),
                    ("list all words", "l", listWords),
                        ], quit=True, default="n"))

            if select == Menu.quit:
                break
            else:
                select()
