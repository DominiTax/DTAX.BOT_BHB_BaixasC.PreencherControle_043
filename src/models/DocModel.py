from dataclasses import dataclass
from typing import Literal

@dataclass
class DocModel:
    datas: list
    type: Literal['Pefin','Protesto']
    inclusion_data: str

# Credor: (?<CNPJ>\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2})