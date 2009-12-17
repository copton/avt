import guppy
import os

components = guppy.factory.create({
    "database" : guppy.Component("database.elixir.Elixir"),
    "ui" : guppy.Component("ui.console.UI"),
    "database.connection_string" : "sqlite:///%s/.voctrain+/database.sqlite" % os.environ["HOME"],
    })

db = components["database"]
ui = components["ui"]

db.connect()

w = db.Word()(contents="hallo", translation=db.Translation()(contents="hello"))

ui.edit(w)

db.flush()
