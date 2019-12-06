"""
Provides custom exceptions for
DBVirus Downloader
"""


class DownloaderException(Exception):
    """Generic exception"""


class FasterqDumpNotFound(DownloaderException):
    """Exception when the binary for fasterq-dump is not found in $PATH"""

    message = """fasterq-dump not found!
    Tip: install it using conda:
        conda config --add channels bioconda
        conda install sra-tools

    For more info, see https://github.com/ncbi/sra-tools/wiki/02.-Installing-SRA-Toolkit
    """

    def __init__(self):

        DownloaderException.__init__(self, self.message)
