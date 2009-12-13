import elixir
import data_model

import os.path

import config

class Database(object):
    def __init__(self):
        db_path = os.path.join(config.data_path, config.db_file)

        elixir.metadata.bind = 'sqlite:///' + db_path
        elixir.metadata.bind.echo = True
        
        elixir.setup_all()
        elixir.create_all()

        #if not create_db_file():
        #    Base.metadata.create_all(self.engine)


    def __del__(self):
        self.flush()

    def flush(self):
        elixir.session.commit()

db = None

def setup():
    global db
    db = Database()
