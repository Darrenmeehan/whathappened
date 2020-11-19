import pytest


@pytest.fixture()
def correct_commandline_arguments():
    return ["sync,", "--bucket-name", "hello"]
