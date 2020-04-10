import pandas as pd
from utils.config import Config
import numpy as np

# OBSOLETE (just to clean a file)
if __name__ == '__main__':

    # %%
    df = pd.read_csv(Config.csv_files[3], sep=';', encoding='ISO-8859-1')
    todetele = np.equal(Config.labels_columns, -1)
    df = df.loc[:, np.invert(todetele)]
    file = Config.csv_files[2]
    file = file.replace(file[-6::], 'v5.csv')
    df.to_csv(file, sep=';', encoding='ISO-8859-1')