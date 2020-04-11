# %%
import pandas as pd
from utils.config import Config
import numpy as np
from glob import glob
import re
import string
import funcy as fp
from gensim import models
from gensim.corpora import Dictionary, MmCorpus
import nltk

# OBSOLETE (just to clean a file)
if __name__ == '__main__':
    # %%
    df = pd.read_csv(Config.csv_files[0], sep=';', encoding='ISO-8859-1')
    """ code used to removed fields with -1 from original file (will fail otherwise)
    todetele = np.equal(Config.labels_columns, -1)
    df = df.loc[:, np.invert(todetele)]
    file = Config.csv_files[2]
    file = file.replace(file[-6::], 'v5.csv')
    df.to_csv(file, sep=';', encoding='ISO-8859-1')
    
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)"""
    EMAIL_REGEX = re.compile(r"[a-z0-9\.\+_-]+@[a-z0-9\._-]+\.[a-z]*")
    FILTER_REGEX = re.compile(r"[^a-z '#]")
    TOKEN_MAPPINGS = [(EMAIL_REGEX, "#email"), (FILTER_REGEX, ' ')]


    def tokenize_line(line):
        res = line.lower()
        for regexp, replacement in TOKEN_MAPPINGS:
            res = regexp.sub(replacement, res)
        return res.split()


    def tokenize(lines, token_size_filter=2):
        tokens = fp.mapcat(tokenize_line, lines)
        return [t for t in tokens if len(t) > token_size_filter]


    def load_doc(filename):
        group, doc_id = filename.split('/')[-2:]
        with open(filename, errors='ignore') as f:
            doc = f.readlines()
        return {'group': group,
                'doc': doc,
                'tokens': tokenize(doc),
                'id': doc_id}

    def load_df(dfline):
        group = dfline["etiologie"]
        doc_id = dfline.name
        courrier = dfline["courrier"]

        if pd.isna(courrier):
            doc = ""
        else:
            doc = dfline["courrier"].splitlines()
        return {'group': group,
                'doc': doc,
                'tokens': tokenize(doc),
                'id': doc_id}


    tokenize(df["courrier"][1].splitlines())

    list_doc = []
    for line in df.iterrows():
        list_doc.append(load_df(line[1]))
    docs = pd.DataFrame(list_doc).set_index(['group', 'id'])
    # list(map(load_doc, [glob('notebooks/pyLDAvis/data/20news-bydate-train/*/*')[0]]))
    # docs = pd.DataFrame(list(map(load_doc, glob('notebooks/pyLDAvis/data/20news-bydate-train/*/*')))).set_index(['group', 'id'])

    docs.head()

# %%


# %%
    docs = docs[docs.astype(str)["tokens"] != '[]'] # remove empty letters
    dictionary, corpus = prep_corpus(docs['tokens'])
    MmCorpus.serialize('courrier.mm', corpus)
    dictionary.save('courrier.dict')

# %%
    num_topics=5
    lda = models.ldamodel.LdaModel(corpus=corpus, id2word=dictionary, num_topics=num_topics, passes=10)

    lda.save(f'courrier_{num_topics}_lda.model')

    import pyLDAvis.gensim as gensimvis
    import pyLDAvis

    #%%

    lda.load(f'courrier_{num_topics}_lda.model')
    vis_data = gensimvis.prepare(lda, corpus, dictionary)
    pyLDAvis.display(vis_data)