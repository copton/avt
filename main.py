import guppy
import os

components = guppy.factory.create({
    "database" : guppy.Component("database.elixir.Elixir"),
    "ui" : guppy.Component("ui.console.UI"),
    "workflow" : guppy.Component("workflow.lookup.Workflow"),
    "database.connection_string" : "sqlite:///%s/.voctrain+/database.sqlite" % os.environ["HOME"],
    })

components["workflow"].run()
