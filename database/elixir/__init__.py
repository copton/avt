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

    def Word(self):
        return data_model.Word

    def Sentence(self):
        return data_model.Sentence
    
    def Translation(self):
        return data_model.Translation

    def deleteWord(self, word):
        if word == None:
            return

        self.deleteTranslation(word.translation)
        for s in word.sentences:
            self.deleteSentence(s)

        word.delete()

    def deleteTranslation(self, translation):
        if translation == None:
            return
    
        translation.delete()

    def deleteSentence(self, sentence):
        sentence.delete()
