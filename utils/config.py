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