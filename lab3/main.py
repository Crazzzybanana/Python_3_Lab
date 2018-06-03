from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

from mongo import mongo_data
from processing import process

import nltk
nltk.download('stopwords')
nltk.download('wordnet')


# Получение сообщений
messages = mongo_data()
# Подготовка сообщений
processed = process(messages)

# Обработка
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform([y for x in processed for y in x])

clusters = 10
model = KMeans(n_clusters=clusters)
model.fit(X)
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()
for i in range(clusters):
    print("Cluster %d:\n" % i)
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind])
    print('\n')
