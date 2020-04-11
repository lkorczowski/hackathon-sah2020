import re
import funcy as fp
import pandas as pd


EMAIL_REGEX = re.compile(r"[a-z0-9\.\+_-]+@[a-z0-9\._-]+\.[a-z]*")
FILTER_REGEX = re.compile(r"[^a-z '#]")
TOKEN_MAPPINGS = [(EMAIL_REGEX, "#email"), (FILTER_REGEX, ' ')]


def map_column(df_table, dict_keywords=None):
    return df_table


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