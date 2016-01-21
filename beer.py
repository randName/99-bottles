class Noun:
    def __init__(self, word, number=1, plural=None):
        self.base_word = word
        self.number = number
        self.plural = plural if plural else self.default_plural
        self.word = self.plural()

    def default_plural(self):
        if self.number == 1:
            return self.base_word
        else:
            return self.base_word + 's'

    def __add__(self, number):
        return Noun( self.base_word, self.number + number )
        
    def __sub__(self, number):
        return Noun( self.base_word, self.number - number )

    def __iadd__(self, number):
        self.number += number

    def __isub__(self, number):
        self.number -= number

    def __str__(self):
        return "{0} {1}".format( self.number, self.word )

def sing( start ):
    lyrics = "{0} on the wall, {0}.\nTake one down, pass it around, {1} on the wall.\n"
    of_beer = lambda x: '%s of beer' % x
    bottles = Noun( "bottle", start )

    for i in range(start): print( lyrics.format( of_beer( bottles-i ), of_beer( bottles-i-1 ) ) )

if __name__ == '__main__':
    sing(99)
