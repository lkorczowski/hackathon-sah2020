import pandas as pd
from utils.config import Config
import numpy as np


def fun_clean_categogy1(array, keyw1, index, BOW):
    compty = 0
    c = 0
    for elm in array:
        if elm == "oui" or elm == "parfois":
            BOW[c].append(keyw1[index])
            compty += 1
        c += 1
    # print(compty)
    return BOW


def fun_clean_categogy2(array, BOW):
    compty = 0
    c = 0
    for elm in array:
        if not elm == "":
            if not BOW[c].__contains__(elm):
                BOW[c].append(elm)
                compty += 1
        c += 1
    # print(compty)
    return BOW


def fun_clean_categogy3(array, keyw3, index, BOW, list_THR):
    compty = 0
    c = 0
    for elm in array:
        # print(elm)
        if not np.isnan(float(str(elm).replace(",", "."))):
            if float(str(elm).replace(",", ".")) > list_THR[index]:
                if not BOW[c].__contains__(elm):
                    BOW[c].append(keyw3[index])
                    compty += 1
        c += 1
    print(compty)
    return BOW


if __name__ == '__main__':
    # %%
    df = pd.read_csv(Config.csv_files[-1], sep=';', encoding='ISO-8859-1')
    df.columns
    #
    # d = {'col1': [1, 2], 'col2': [3, 4]}
    # df = pd.DataFrame(data=d)


    List_cat1 = ["difficulté endormisst", "fatigue au reveil", "hyperacousie", "surdité", "SDE", "vertiges",
                 "depression", "anxiété"]

    keyw1 = ["endormissement", "fatigue", "hyperacousie", "surdité", "somnolence", "vertige", "dépression", "anxiété"]

    List_cat2 = ["timbre acouphène", "type de douleurs", "type otalgie", "type de vertiges",
                 "caractere particulier", "mode apparition"]

    List_cat3 = ["EVA  depression", "epworth", "EVA anxiété", "EVA douleurs", "EVA hyperac", "EVA hypoac",
                 "EVA Otalgie 1", "EVA SADAM", "EVA vertiges", "ISI", "score khalfa hyperacousie", "EVA  concentration"]

    keyw3 = ["dépression", "somnolence", "anxiété", "douleurs", "hyperacousie", "hypoacousie", "otalgie", "mâchoire",
             "vertige", "sommeil", "hyperacousie", "concentration"]

    List_THR = [5, 10, 5, 5, 5, 5, 4, 3, 3, 12, 20, 5]

    cat4 = ["intensité ac"]

    compt = 0
    BOW = [[] for i in range(len(df[df.columns[0]]))]


    for colname in List_cat1:
        # print(df[colname])  # show value before
        print(colname)
        BOW = fun_clean_categogy1(df[colname], keyw1, compt, BOW)
        compt += 1

    compt=0
    for colname in List_cat2:
        print(colname)
        BOW = fun_clean_categogy2(df[colname], BOW)
        compt += 1

    compt=0
    for colname in List_cat3:
            print(colname)
            BOW = fun_clean_categogy3(df[colname], keyw3, compt, BOW, List_THR)
            compt += 1

    for elm in BOW:
        if elm.__contains__(np.nan):
            elm.pop(elm.index(np.nan))

    print(BOW[:200])  # show value after
