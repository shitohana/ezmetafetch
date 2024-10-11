import argparse
from pathlib import Path

parser = argparse.ArgumentParser(
    prog="EzMetaFetch",
    description="TODO",
    add_help=True,
    epilog="TODO (Output dir file structure.)",
)


def existent_path(filename: str | Path | None) -> Path | None:
    if filename is None:
        return None
    path = Path(filename)
    if not path.exists():
        raise FileNotFoundError(path)
    else:
        return path


_ = parser.add_argument(
    "-t",
    "--terms",
    type=existent_path,
    default=None,
    help="Path to '\\n' separated file with search terms (e.g. SRR).",
)
_ = parser.add_argument(
    "-i",
    "--ids",
    type=existent_path,
    required=False,
    default=None,
    help="Path to '\\n' separated file with NCBI Universal IDs.",
)
_ = parser.add_argument("-d", "--db", type=str, required=False, default="sra", help="Entrez DataBase.")
_ = parser.add_argument(
    "-o",
    "--output",
    type=Path,
    default=Path.cwd(),
    help="Path to the output directory.",
)
_ = parser.add_argument("-c", "--config", type=existent_path, required=False, help="Path to config file.")
