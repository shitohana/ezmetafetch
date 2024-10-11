from functools import cached_property
from logging import DEBUG, INFO, Logger
from pathlib import Path

from pydantic import BaseModel, Field, field_validator

from .args_parser import parser, existent_path
from .config_model import ConfigModel


class Base(BaseModel):
    terms_file: Path | None = Field(default=None)
    ids_file: Path | None = Field(default=None)
    db: str = Field(default="sra")
    output: Path = Field(default_factory=lambda: Path.cwd())
    config: ConfigModel = Field(default_factory=ConfigModel)
    
    @field_validator("output")
    @classmethod
    def init_output(cls, path: Path):
        if not path.exists():
            try:
                path.mkdir()
            except Exception as e:
                raise(e)
        return path
    
    @classmethod
    def from_args(cls, args_list: list[str] | None = None):
        args = parser.parse_args(args_list)
        config_path = existent_path(args.config)
        if config_path is None:
            config = ConfigModel()
        else:
            if config_path.suffix == ".json":
                config = ConfigModel.from_json(config_path)
            elif config_path.suffix == ".yaml":
                config = ConfigModel.from_yaml(config_path)
            else:
                raise KeyError(f"Unsupported file extension: {config_path.suffix}")
        return cls(
            terms_file=args.terms,
            ids_file=args.ids,
            db=args.db,
            output=args.output,
            config=config
        )
    
    @cached_property
    def logger(self) -> Logger:
        return Logger("EzMetaFetch", level=DEBUG if self.config.http.debug else INFO)
    
    @cached_property
    def terms_list(self):
        if self.terms_file is not None:
            return self.terms_file.read_text().strip().split("\n")
        else:
            return []
    
    @cached_property
    def ids_list(self):
        if self.ids_file is not None:
            return list(map(int, self.ids_file.read_text().strip().split("\n")))
        else:
            return []
        