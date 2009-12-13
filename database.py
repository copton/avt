import elixir
import data_model

import os.path

import config

class FlushOnQuit(object):
    def __del__(self):
        flush()

flush_on_quit = None

def flush():
    elixir.session.commit()
    

def setup():
    db_path = os.path.join(config.data_path, config.db_file)

    elixir.metadata.bind = 'sqlite:///' + db_path
    elixir.metadata.bind.echo = True
    
    elixir.setup_all()
    elixir.create_all()

    global flush_on_quit
    flush_on_quit = FlushOnQuit()
