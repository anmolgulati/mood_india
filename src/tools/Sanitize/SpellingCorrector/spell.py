import re, collections

class SpellingCorrector:
    _NWORDS = {}
    _alphabet = ""

    def __init__(self):
        _NWORDS = train(words(file('big.txt').read()))
        _alphabet = 'abcdefghijklmnopqrstuvwxyz'

    @staticmethod
    def words(self,text): return re.findall('[a-z]+', text.lower())

    @staticmethod
    def train(self,features):
        model = collections.defaultdict(lambda: 1)
        for f in features:
            model[f] += 1
        return model

    @staticmethod
    def editsInitial(self,word):
       splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
       deletes    = [a + b[1:] for a, b in splits if b]
       transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
       replaces   = [a + c + b[1:] for a, b in splits for c in self._alphabet if b]
       inserts    = [a + c + b     for a, b in splits for c in self._alphabet]
       return set(deletes + transposes + replaces + inserts)

    @staticmethod
    def knownEdits(self,word):
        return set(e2 for e1 in self.editsInitial(word) for e2 in self.editsInitial(e1) if e2 in self._NWORDS)

    @staticmethod
    def known(self,words): return set(w for w in words if w in self._NWORDS)

    @staticmethod
    def correct(self,word):
        candidates = self.known([word]) or self.known(self.editsInitial(word)) or self.knownEdits(word) or [word]
        return max(candidates, key=self._NWORDS.get)