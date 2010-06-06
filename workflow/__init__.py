from guppy import *
import ui
import database

class Workflow(object):
    ui = RequiredFeature("ui", isInstanceOf(ui.UI))
    db = RequiredFeature("database", isInstanceOf(database.Database))
    
    def run(self):
        self.db.connect()
        self._run()
        self.db.flush()

    def _run(self):
        raise NotImplementedError()

    def _selectWord(self, words, prompt="select word"):
        menu = ui.Menu(prompt, quit=True, default="q", delimiter="\n", footer="\n")
        for i, word in enumerate(words):
            menu.addOption(ui.Option(word.contents + ": " + word.translation, str(i), i))
        select = self.ui.play(menu)
        if select == ui.Menu.quit:
            return (-1, None)
            
        return (select, words[select])
