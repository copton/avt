import workflow

class Workflow(workflow.Workflow):
    def _run(self):
        self.ui.textoutput("here we go")
