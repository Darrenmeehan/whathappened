import pytest


@pytest.fixture()
def correct_commandline_arguments():
    return ["sync,", "--bucket-name", "hello"]


@pytest.fixture(autouse=True)
def mock_aws_credentials(monkeypatch):
    """
    Mock out AWS credentials.

    Tests should not reach out to the Internet.
    But they inevitably will. This will stop anything from happening.
    """
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "AWS_ACCESS_KEY_ID")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "AWS_SECRET_ACCESS_KEY")
