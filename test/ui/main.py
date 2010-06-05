#! /usr/bin/python
import guppy
from ui import Menu, Option

config = {
    "ui" : guppy.Component("ui.console.UI"),
}

ui = guppy.factory.create(config)["ui"]

menu = Menu("das ist ein Test", 
        options=tuple([("nummer %d" % i, str(i), i) for i in range(20)]),
        delimiter="\n",
        footer="\n",
        confirm=True
)

select = ui.play(menu)
print select
