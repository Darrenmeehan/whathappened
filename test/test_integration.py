import subprocess

import pytest


@pytest.mark.xfail()
def test_command_works_from_shell_exit_zero():
    """
    Basic sanity test that the command exits without error.
    """
    subprocess.run("whathappened", check=True)
