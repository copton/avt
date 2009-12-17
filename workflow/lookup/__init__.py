import workflow

class Workflow(workflow.Workflow):
    def _run(self):
        self.ui.textoutput("here we go")

# words = Word.query.filter(Word.contents.like(u"%%%s" % sys.argv[1])).all()
