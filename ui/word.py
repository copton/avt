import data_model

def remove_sentence(word, sentence):
    for i, s in enumerate(word.sentences):
        if sentence == s.contents:
            s.delete()
            del word.sentences[i]
            return

class Word(object):
    def __init__(self, word):
        self.contents = word.contents
        self.translation = word.translation.contents
        self.sentences = [s.contents for s in word.sentences]
        self.word = word

    def update(self):
        self.word.contents = unicode(self.contents)
        if self.word.translation.contents != self.translation:
            self.word.translation.delete()
            self.word.translation = data_model.Translation(contents=self.translation)

        current_set = set(s.contents for s in self.word.sentences)
        new_set = set(self.sentences)

        to_be_added = new_set.difference(current_set)
        to_be_removed = current_set.difference(new_set)

        for s in to_be_removed:
            remove_sentence(s, self.word)
 
        for s in to_be_added:
            self.word.sentences.append(data_model.Sentence(contents=s))
