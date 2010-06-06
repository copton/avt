import workflow
from ui import Menu, Option
import database

def score(word):
    return word.lookupCnt + word.wrongCnt - word.rightCnt

def compare(lhs, rhs):
    return score(lhs) - score(rhs) 

class Workflow(workflow.Workflow):
    """train on local database"""

    def _run(self):
        self.ui.textoutput("starting training\n")
        words = self.db.sort(compare)
        for word in words:
            self.ui.textoutput("score: %d\n" % score(word))
            self.ui.textoutput("\n".join([word.contents] + word.sentences + [""]))
            self.ui.textinput("press any key to see the translation") 
            self.ui.textoutput(word.translation + "\n")
            select = self.ui.play(Menu("did you know it?", [
                    ("yes", "y", True),
                    ("no", "n", False)
                ], quit=True))
            if select == Menu.quit:
                return
            if select == True:
                word.rightCnt += 1
            else:
                word.wrongCnt += 1 
        self.ui.textoutput("training complete")
