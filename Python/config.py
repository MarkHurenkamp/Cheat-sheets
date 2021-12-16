from dataclasses import dataclass
import json


@dataclass
class Config:
    setting1: str
    setting2: str
    setting3: str


def read_config(config_file: str = "config.json") -> Config:
    with open(config_file, "r") as file:
        content = json.load(file)
        return Config(**content)


# Usage:
config = read_config()
print(
    config.setting1, config.setting2, config.setting3, sep=", "
)  # returns 'Some setting 1, Some setting 2, Some setting 3'
