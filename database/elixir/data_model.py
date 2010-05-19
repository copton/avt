from elixir import *

class Word(Entity):
    contents = Field(Unicode(30))
    lookupCnt = Field(Integer, default=1)
    rightCnt = Field(Integer, default=0)
    wrongCnt = Field(Integer, default=0)

    sentences = OneToMany('Sentence', cascade='all, merge, delete, delete-orphan')
    translation = OneToOne('Translation', cascade='all, merge, delete, delete-orphan')

    def __repr__(self):
        if self.translation:
            return "%s: %s" % (self.contents, self.translation.contents)
        else:
            return "%s: -" % (self.contents)

class Sentence(Entity):
    contents = Field(Unicode(200))
    word = ManyToOne('Word')
    
    def __repr__(self):
        return self.contents

class Translation(Entity):
    contents = Field(Unicode(200))
    word = ManyToOne('Word')
