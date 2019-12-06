"""
Provides unit tests for the Downloader class
"""
from pytest import raises

import dbvirus_downloader as dbdown
from dbvirus_downloader import exceptions


def test_downloader_fails_without_fasterq_dump(mocker):
    """
    Tests that an exception is raised if fasterq-dump binary is not available
    """

    # Mocks Shutil's which in orde to make "fasterq-dump" appear available
    mocker.patch("dbvirus_downloader.which")
    dbdown.which.return_value = False

    with raises(exceptions.FasterqDumpNotFound) as e:

        dbdown.Downloader()

    assert "install it using conda" in str(e.value)
