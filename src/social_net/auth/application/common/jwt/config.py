from dataclasses import dataclass
from typing import Literal

Algorithm = Literal[
    'HS256',
    'HS384',
    'HS512',
    'RS256',
    'RS324',
    'RS512',
]


@dataclass(frozen=True)
class ConfigJWT:
    algorithm: Algorithm
    key: str
