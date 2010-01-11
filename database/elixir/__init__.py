import database
import elixir

import data_model

class Elixir(database.Database):
    def connect(self):
        elixir.metadata.bind = "sqlite:///" + self.connection_string
        elixir.metadata.bind.echo = False

        elixir.setup_all()
        elixir.create_all()

    def flush(self):
        elixir.session.commit()

    def createWord(self, contents, translation="", sentences=[], lookupCnt=1, rightCnt=0, wrongCnt=0):
        return data_model.Word(
            contents=contents,
            translation=data_model.Translation(contents=translation),
            sentences = [data_model.Sentence(contents=sentences[s]) for s in sentences],
            lookupCnt=lookupCnt,
            rightCnt=rightCnt,
            wrontCnt=wrongCnt,
        )

    def query_by_contents(self, pattern):
        return data_model.Word.query.filter(data_model.Word.contents.like(pattern)).all()
