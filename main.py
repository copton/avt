import guppy
import os

components = guppy.factory.create({
    "database" : guppy.Component("database.elixir.Elixir"),
    "database.connection_string" : "sqlite:///%s/.voctrain+/database.sqlite" % os.environ["HOME"],
    })

database = components["database"]

database.connect()

database.flush()

del database
