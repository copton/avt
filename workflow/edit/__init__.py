import workflow
from ui import Menu, Option

def delete(word):
    word.delete()
    del word

class Workflow(workflow.Workflow):
    def _enter(self):
        contents = self.ui.textinput("enter new word")
        word = self.db.Word()(contents=contents) 
        self.ui.edit(word)

    def _search(self):
        pattern = self.ui.textinput("enter pattern")
        Word = self.db.Word()
        matches = Word.query.filter(Word.contents.like(ur"%" + pattern + "%")).all()
        if matches == []:
            self.ui.textoutput("no matches found.")
            return

        menu = Menu("select word", quit=True, default="q", delim="\n", footer="\n")
        for i, word in enumerate(matches):
            menu.addOption(Option(str(word), str(i), i))
        select = self.ui.play(menu)
        if select == Menu.quit:
            return
            
        word = matches[select]
        menu = Menu("what do you want to do?", [
                    ("edit", "e", self.ui.edit),
                    ("delete", "d", delete)
                ], quit=True, default="e")
        select = self.ui.play(menu)
        if select == Menu.quit:
            return
        
        select(word)

    def _run(self):
        while True:
            select = self.ui.play(
                Menu("what do you want to do?", [
                    ("enter new word", "n", self._enter),
                    ("search in local database", "s", self._search),
                        ], quit=True, default="n"))

            if select == Menu.quit:
                break
            else:
                select()
