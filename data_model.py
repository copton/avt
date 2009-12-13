from elixir import *

class Word(Entity):
    contents = Field(Unicode(30))
    lookupCnt = Field(Integer, default=1)
    rightCnt = Field(Integer, default=0)
    wrongCnt = Field(Integer, default=0)

    sentences = OneToMany('Sentence')
    translation = OneToMany('Translation')

    def __repr__(self):
        return '<Word %s>' % self.contents

class Sentence(Entity):
    contents = Field(Unicode(200))
    word = ManyToOne('Word')

class Translation(Entity):
    contents = Field(Unicode(200))
    word = ManyToOne('Word')
