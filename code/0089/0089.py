from textblob import TextBlob

def read_txt(text: str) -> tuple[str, list[str]]:
    label, message = text.strip().split(maxsplit=1)
    return label, message

source = "data/spam.txt"
with open(source) as fh:
    words = [read_txt(line) for line in fh]

index = 932
label, msg = words[index]  # it's ham
print(msg)
# 'Congratulations ore mo owo re wa. Enjoy it and 
# i wish you many happy moments to and fro wherever you go'

blob = TextBlob(msg)

print("blob.sentiment")
# Sentiment(polarity=0.567, subjectivity=0.667)

tokens = blob.words
print(tokens)
# ['Congratulations', 'ore', 'mo', 'owo', 're', 'wa', 'Enjoy', 'it', 'and', 
# 'i', 'wish', 'you', 'many', 'happy', 'moments', 'to', 'and', ... ]

sentences = blob.sentences
print(sentences)
# Sentence("Congratulations ore mo owo re wa."), 
# Sentence("Enjoy it and i wish you many happy moments to and fro wherever you go")

# https://stackabuse.com/simple-nlp-in-python-with-textblob-parts-of-speech-pos-tagging/
for word, pos in blob.tags:
    print(word, pos)
# Congratulations NNS
# ore VBP
# mo JJ
# owo NN
# re NN
# wa NN
# Enjoy VB

for ngram in blob.ngrams(3): 
    print(ngram)
# ['Congratulations', 'ore', 'mo']
# ['ore', 'mo', 'owo']
# ['mo', 'owo', 're']
# ['owo', 're', 'wa']
# ['re', 'wa', 'Enjoy']
# ['wa', 'Enjoy', 'it']
# ['Enjoy', 'it', 'and']
