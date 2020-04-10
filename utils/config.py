""" Configuration methods for tinnsleep loading/testing
"""

from glob import glob
import os
import getpass


class Config():
    """Load user-dependent variable and path
    """

    username = getpass.getuser()
    known_users = {
        "louis": "/Users/louis/Data/SIOPI/",
        "runner": "/runner/"}

    if username in known_users.keys():
        data_path = known_users[username]
    else:
        raise KeyError(username + ": User path not defined, please add path in utils.config.")

    csv_files = sorted(glob(os.path.join(data_path, '*csv')))

    required_columns = ["% tps ac ressenti", "etiologie", "ETIOLOGIE FINALE"]

    # labels columns :
    # -1: to delete ABSOLUTELY (anonymity)
    #  0: unkown
    #  1: to keep if possible (not priority)
    #  2: to keep but a lot of missing columns to reformat
    #  3: to keep ABSOLUTELY
    #  4: redundant (preprocessing required to find `related_columns`)
    labels_columns = [3, 3, 0, 0, 0, 1, 1, 1, 2, 3, 3, 0, -1, 2, 3, 2, 0, 0, 2, -1, -1, 2, 2, 2, 0, 0, 0, 2, 2, 3, 2,
                      -1, -1, -1, -1, -1, 2, -1, 2, 2, 2, 0, 2, 2, 3, 4, 3, 4, 2, 2, 2, 3, 4, 4, 3, 4, 4, 4, 4, 3, 3, 3,
                      4, 4, 3, 4, 4, 3, 3, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 4, 4, 3, 3, 4, 4, 2, 2, 2, 2,
                      2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 2, 2, 2, 2, 0, 2, 2, 2, 2, -1, 2, 3, 3, 4, 3, 3, 3, 3, 3, 3, 2, 2,
                      -1, 0, 0, 2, 0, 3, 2, 2, -1, -1, -1, -1, -1, 0, 3, -1, -1, -1, -1, -1, 2, 0, 0, 0, 0, 0, 2, 2, 2,
                      -1, 2, 2, 0, 0, 0, 0, 0, 2, 2, 2, 3, 1, 2, -1, -1, 2, 2, 0, 1, 1, 1, 2, 2, 0, 0, 0, 0, 2, 2, 2, 2,
                      2, 4, 2, 2, 2, 2, 2, -1, 2, 2, 0, -1, 1, -1, -1, 0, 3, 0, 2, 0, 4, 0, 2, 4, 4, -1, 3, 2, 2, 2, 2,
                      2, 2, 2, 2, 2, 2, 0]

    related_columns = {"etiologie": ["etiologie", "ETIOLOGIE FINALE"],
                       "epworth": ["epworth, epoworth 2"]}
