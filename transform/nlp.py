import nltk
from gensim.corpora import Dictionary, MmCorpus


def nltk_stopwords():
    nltk.download('stopwords')
    return set(nltk.corpus.stopwords.words('french'))


def prep_corpus(docs, additional_stopwords=set(), no_below=5, no_above=0.5):
    print('Building dictionary...')
    dictionary = Dictionary(docs)
    stopwords = nltk_stopwords().union(additional_stopwords)
    stopword_ids = map(dictionary.token2id.get, stopwords)
    dictionary.filter_tokens(stopword_ids)
    dictionary.compactify()
    dictionary.filter_extremes(no_below=no_below, no_above=no_above, keep_n=None)
    dictionary.compactify()

    print('Building corpus...')
    corpus = [dictionary.doc2bow(doc) for doc in docs]

    return dictionary, corpus

