from dataclasses import dataclass
from typing import Literal
@dataclass
class ExcelModel:
    type: Literal['Perfin', 'Protesto']
    cnpj_emissor: str
    supplier: str
    number_doc:str
    total:str
    date_doc: str