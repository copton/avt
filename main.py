#! /usr/bin/python
import os.path
from config import config
import sys

sys.path.append("/home/alex/scm/guppy")
import guppy

workflow = os.path.basename(sys.argv[0])

component_selection = {
    "database" : guppy.Component("database.ram.RAM"),
    "ui" : guppy.Component("ui.console.UI"),
    "workflow" : guppy.Component("workflow.%s.Workflow" % workflow),
    "dictionary" : guppy.Component("dictionary.trans_de_en.Dictionary"),
}

config.update(component_selection)

components = guppy.factory.create(config)

components["workflow"].run()
