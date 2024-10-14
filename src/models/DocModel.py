from dataclasses import dataclass
from typing import Literal

@dataclass
class DocModel:
    cnpj: str
    type: Literal['Pefin','Protesto']
    fornecedor: str
    number_doc: str
    total: float
    date_doc: str
    inclusion_data: str