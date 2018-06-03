from nltk import RegexpTokenizer, WordNetLemmatizer
from nltk.corpus import stopwords
from tqdm import tqdm


def process(messages):
    tokenizer = RegexpTokenizer(r"\w+")
    lemmatizer = WordNetLemmatizer()
    processed = []
    for m in tqdm(messages):
        tokens = [t for t in tokenizer.tokenize(str.lower(m)) if t not in stopwords.words("english")]
        if len(tokens) > 0:
            processed.append([lemmatizer.lemmatize(t) for t in tokens])

    return processed
