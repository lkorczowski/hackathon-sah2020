import pytest
import os
import getpass


@pytest.mark.skipif(getpass.getuser()=='runner', reason="Not expecting to work in CI because data required locally")
def test_Config():
    from utils.config import Config
    assert os.path.split(Config.csv_files[0])[1].endswith('.csv')