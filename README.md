Simple tool for downloading metadata of EntrezAPI entries

```commandline
usage: EzMetaFetch [-h] [-t TERMS] [-i IDS] [-d DB] [-o OUTPUT] [-c CONFIG]

Simple tool for downloading metadata of EntrezAPI entries.

options:
  -h, --help            show this help message and exit
  -t TERMS, --terms TERMS
                        Path to '\n' separated file with search terms (e.g. SRR).
  -i IDS, --ids IDS     Path to '\n' separated file with NCBI Universal IDs.
  -d DB, --db DB        Entrez DataBase.
  -o OUTPUT, --output OUTPUT
                        Path to the output directory.
  -c CONFIG, --config CONFIG
                        Path to config file.
```