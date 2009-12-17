import guppy

from config import config

component_selection = {
    "database" : guppy.Component("database.elixir.Elixir"),
    "ui" : guppy.Component("ui.console.UI"),
    "workflow" : guppy.Component("workflow.lookup.Workflow"),
}

config.update(component_selection)

components = guppy.factory.create(config)

components["workflow"].run()
