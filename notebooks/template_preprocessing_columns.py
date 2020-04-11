import pandas as pd
from utils.config import Config
import numpy as np

if __name__ == '__main__':
    # %%
    df = pd.read_csv(Config.csv_files[-1], sep=';', encoding='ISO-8859-1')
    df.columns
    #
    # d = {'col1': [1, 2], 'col2': [3, 4]}
    # df = pd.DataFrame(data=d)


    def fun_clean_categogy1(array):
        clean_array = -array  # do what you have to do here
        return clean_array


    List_cat1 = ["% tps ac ressenti"]
    for colname in List_cat1:
        print(df[colname])  # show value before
        df[colname] = fun_clean_categogy1(df[colname])
        print(df[colname])  # show value before
