import workflow
from ui import Menu, Option
import infra

def select_word(words):
    menu = Menu("select word", quit=True, delimiter="\n", footer="\n")
    for i, word in enumerate(words):
        entry = word.contents + ": " + word.translation.contents
        menu.addOption(entry, str(i), i)

    return menu

class Workflow(workflow.Workflow):
    def _run(self):
        Word = self.db.Word()

        while True:
            pattern = self.ui.textinput("please enter word")
            local_matches = Word.query.filter(Word.contents.like(ur"%" + pattern + ur"%")).all()

            select = self.ui.play(select_word(local_matches))
            if select != Menu.quit:
                word = local_matches[select]
                word.lookupCnt += 1
                if self.ui.play(Menu("do you want to edit this word?", 
                                [("yes", "y", True), ("no", "n", False)], 
                                default="n"):
                    self.ui.edit(word)
                
                continue

             
                
                                            

