"""
This module provides classes and helpers to download SRA Data
"""

from enum import Enum
from shutil import which

from dbvirus_cacher.documents import EntrezItem

__version__ = "0.1.0"

# pylint: disable=invalid-name
DownloadStrategy = Enum("DownloadStrategy", ["FASTERQDUMP", "MANUAL"])


class Downloader:
    """
    Downloader chooses between different strategies of download in order to
    perform faster SRA data dumping
    """

    strategy = DownloadStrategy.MANUAL

    def __init__(self):
        if self.is_fasterqdump_available():
            self.strategy = DownloadStrategy.FASTERQDUMP

    @staticmethod
    def is_fasterqdump_available():
        """
        returns true if NCBI's fasterq-dump is available in PATH
        """
        return bool(which("fasterq-dump"))

    def available_data(self):
        """
        returns an iterator over the data available at the local
        cache that wasn't yet downloaded.
        """
        # pylint: disable=no-member,no-self-use
        return EntrezItem.objects.all()


__all__ = ["Downloader", "DownloadStrategy"]
