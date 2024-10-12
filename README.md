# EzMetaFetch

Simple tool for downloading metadata of EntrezAPI entries.

# Installation

EzMetaFetch can be either installed from PyPI:

```commandline
pip install ezmetafetch
```

Or from GitHub release:

```commandline
pip install ezmetafetch-0.1.0-py3-none-any.whl
```

# Usage

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

# Example

All example files are available at [example folder](example).

```commandline
ezmetafetch -t example/input/example_srp.txt -c example/input/config.yaml -o example/output
```