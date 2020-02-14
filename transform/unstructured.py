def replace_str(string, dict_keywords=None):
    """Replace all related keywords in file by the key in a dictionary


    Parameters
    ----------
    string : str
        a long string
    dict_keywords : dict
        A dictionnary
    """
    for i, j in dict_keywords.items():
        string = string.replace(i, j)
    return string