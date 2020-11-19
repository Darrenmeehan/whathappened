import pytest

from whathappened.core import main

@pytest.mark.xfail()
def test_application_handler():
    main()
