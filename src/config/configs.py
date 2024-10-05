from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

@dataclass
class Config:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super(Config, cls).__new__(cls)
        return cls.instance
    
    # this your configurations
    # example:
    # host: str = "localhost"
    # port: int = 8080
    # log_level: str = "INFO"