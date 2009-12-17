#! /usr/bin/python
import guppy
import sys
import os.path
from config import config

workflow = os.path.basename(sys.argv[0])

component_selection = {
    "database" : guppy.Component("database.elixir.Elixir"),
    "ui" : guppy.Component("ui.console.UI"),
    "workflow" : guppy.Component("workflow.%s.Workflow" % workflow),
}

config.update(component_selection)

components = guppy.factory.create(config)

components["workflow"].run()
