import workflow
from ui import Menu, Option
import database
from guppy import *
import dictionary

class Workflow(workflow.Workflow):
    """edit local database"""

    dictionary = RequiredFeature("dictionary", isInstanceOf(dictionary.Dictionary))

    def selectWord(self, words, prompt="select word"):
        menu = Menu(prompt, quit=True, default="q", delimiter="\n", footer="\n")
        for i, word in enumerate(words):
            menu.addOption(Option(word.contents + ": " + word.translation, str(i), i))
        select = self.ui.play(menu)
        if select == Menu.quit:
            return None
            
        return words[select]

    def _run(self):
        def add():
            def manually():
                contents = self.ui.textinput("enter new word (leave blank to quit)")
                if contents == "":
                    return
                word = database.Word(contents, "")
                self.ui.edit(word)
                self.db.add(word)

            def search():
                pattern = self.ui.textinput("enter the search pattern")
                words = self.dictionary.search(pattern)  
                if words == []:
                    self.ui.textoutput("no matches found.")
                    return
                word = self.selectWord(words)
                if word == None:
                    return

                self.ui.edit(word)
                self.db.add(word)

            select=self.ui.play(Menu("what do you want to do?", [
                        ("add manually", "m", manually),
                        ("search in dictionary", "s", search)
                    ], quit=True, default="s"))
            if select != Menu.quit:
                select()

        def edit():
            pattern = self.ui.textinput("which word do you want to edit?")
            matches = self.db.search(pattern)
            if matches == []:
                self.ui.textoutput("no matches found.")
                return

            word = self.selectWord(matches)
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
