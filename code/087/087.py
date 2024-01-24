# Data removed from repo; too damn big
from collections import Counter
from nltk.corpus import stopwords

STOPWORDS = stopwords.words('english')

def is_not_stopword(word):
    return word not in STOPWORDS

if __name__ == "__main__":
    corpus = "data/internet_archive_scifi_v3.txt"

    with open(corpus) as fh:
        words = fh.read().strip().split()
        words = [word.lower() 
            for word in words 
            if word.lower() not in STOPWORDS]
        counts = Counter(words)

    top10 = counts.most_common(10)
    for word, count in top10:
        print(f"{word}: {count:,}")
    # one: 55,699
    # would: 52,453
    # could: 46,008
    # said: 44,243
    # like: 39,196
    # "i: 35,523
    # #: 29,304
    # back: 28,459
    # get: 26,540