from nltk.util import ngrams 
from nltk.tokenize import word_tokenize

def read_txt(text: str) -> tuple[str, list[str]]:
    words = text.strip().split()
    label = words[0]
    message = words[1:]
    return label, message

def create_ngrams(words: list[str], n: int = 2) -> list[str]:
     slices = (words[n-(n-i):len(words)-(n-i-1)] for i in range(n))
     return zip(*slices)

if __name__ == "__main__":
    with open("data/spam.txt") as fh:
        words = [read_txt(line) for line in fh]
    
    label, tokens = words[100]
    mygrams = list(create_ngrams(tokens, 3))
    trigrams = list(ngrams(tokens, 3))
    for foo, bar in zip(mygrams, trigrams):
        print(f"{foo} == {bar}")
    # ('Please', "don't", 'text') == ('Please', "don't", 'text')
    # ("don't", 'text', 'me') == ("don't", 'text', 'me')
    # ('text', 'me', 'anymore.') == ('text', 'me', 'anymore.')
    # ('me', 'anymore.', 'I') == ('me', 'anymore.', 'I')
    # ('anymore.', 'I', 'have') == ('anymore.', 'I', 'have')
    # ('I', 'have', 'nothing') == ('I', 'have', 'nothing')
    # ('have', 'nothing', 'else') == ('have', 'nothing', 'else')
    # ('nothing', 'else', 'to') == ('nothing', 'else', 'to')
    # ('else', 'to', 'say.') == ('else', 'to', 'say.')
