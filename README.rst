DBVirus Downloader
==================

This component of the DBVirus project downloads RNA sequences whose metadata
was searched by the Searcher step and saved in a databases through the Caching
layer.

Usage
-----

1. Download _any_ available sequence that wasn't yet downloaded:

`dbvirus-downloader --mongo-url=mongodb://server:port/db`

2. Download a specific sequence if it wasn't yet downloaded

2.1. By UID

`dbvirus-downloader <uid> --mongo-url=mongodb://server:port/db`
`dbvirus-downloader 9362723 --mongo-url=mongodb://server:port/db`

2.2. By SRA Filename

`dbvirus-downloader <filename> --mongo-url=mongodb://server:port/db`
`dbvirus-downloader DRR182531 --mongo-url=mongodb://server:port/db`

2.3 By Experiment Accession

`dbvirus-downloader <filename> --mongo-url=mongodb://server:port/db`
`dbvirus-downloader DRX173036 --mongo-url=mongodb://server:port/db`
