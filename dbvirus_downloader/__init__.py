"""
This module provides classes and helpers to download SRA Data
"""

from shutil import which

from dbvirus_cacher.documents import EntrezItem

from .exceptions import FasterqDumpNotFound

__version__ = "0.1.0"


class Downloader:
    """
    Downloader chooses between different strategies of download in order to
    perform faster SRA data dumping
    """

    def __init__(self):
        if not self.is_fasterqdump_available():
            raise FasterqDumpNotFound()

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


__all__ = ["Downloader"]
