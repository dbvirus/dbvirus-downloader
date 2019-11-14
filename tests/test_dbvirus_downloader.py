"""
Provides unit tests for the Downloader class
"""
import dbvirus_downloader
from dbvirus_downloader import Downloader, DownloadStrategy


def test_downloader_finds_fasterq_dump(mocker):
    """
    Tests that if the fasterq-dump binary is available, it is used
    as a strategy
    """
    mocker.patch("dbvirus_downloader.which")
    dbvirus_downloader.which.return_value = True

    downloader = Downloader()

    assert downloader.strategy == DownloadStrategy.FASTERQDUMP
