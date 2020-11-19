import pytest

from whathappened.cli import add_arguments


def test_sync_required_args_supplied(correct_commandline_arguments):
    parser = add_arguments()
    parser.parse_args(correct_commandline_arguments)


def test_sync_no_args_required():
    parser = add_arguments()
    with pytest.raises(SystemExit):
        parser.parse_args(["sync"])
