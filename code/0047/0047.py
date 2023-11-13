import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import NearestNeighbors # LSHForest??

url = "https://raw.githubusercontent.com/brmson/dataset-sts"
url = f"{url}/master/data/sts/sick2014/SICK_train.txt"
df = pd.read_csv(url, sep='\t')
print(df.head())
sentences = df['sentence_A'].tolist()

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(sentences)
query = vectorizer.transform(["A person and steak."])

# lshf = LSHForest(n_estimators=5, n_candidates=5, random_state=42)
# lshf.fit(X)
# neighbors = lshf.kneighbors(query, n_neighbors=2)

nn = NearestNeighbors(n_neighbors=2, algorithm='brute', metric='cosine')
nn.fit(X)
neighbors = nn.kneighbors(query, n_neighbors=5)
neighbors = neighbors[1][0]  # Inexes

for index in neighbors:
    print(sentences[index])
