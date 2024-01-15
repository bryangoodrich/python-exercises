import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Data Prepartion
with open("data/spam.txt") as fh:
    data = (line.strip().split(maxsplit=1) for line in fh)
    data = ((label, message.lower()) for label, message in data)
    df = pd.DataFrame(data, columns = ("label", "message"))
    df['label'] = df['label'].map({'ham':0, 'spam':1})

# Train vs Test Data Split of X variables and Y labels
x_train, x_test, y_train, y_test = train_test_split(
    df.message, 
    df.label, 
    test_size = 0.2)

# Feature Engineering: bag-o-words count vs ngrams/tfidf
bow_model = CountVectorizer()
tfidf_model = TfidfVectorizer(ngram_range=(1, 2))
count_features = bow_model.fit_transform(x_train)
tfidf_features = tfidf_model.fit_transform(x_train)

# Naive Bayes Classifier Model Fitting
nb_bow = MultinomialNB()
nb_tfidf = MultinomialNB()
nb_bow.fit(count_features, y_train)
nb_tfidf.fit(tfidf_features, y_train)

# Test Prediction Validation
bow_preds = nb_bow.predict(bow_model.transform(x_test))
ngram_preds = nb_tfidf.predict(tfidf_model.transform(x_test))
print(f"""
Bag-of-words accuracy: {accuracy_score(y_test, bow_preds):0.2f} 
N-gram accuracy: {accuracy_score(y_test, ngram_preds):0.2f}
""")
