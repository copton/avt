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
