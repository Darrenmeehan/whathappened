import subprocess

import pytest

from whathappened.core import main


def test_application_handler(correct_commandline_arguments):
    args = correct_commandline_arguments
    main(args)
