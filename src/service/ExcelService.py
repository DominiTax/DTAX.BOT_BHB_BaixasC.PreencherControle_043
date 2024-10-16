import xlwings as xw
import sys
import os
import openpyxl
# Adiciona o diretório 'src' ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models import ExcelModel
class Excel:
    def __init__(self, file) -> None:
        self.file = file
        self.sheet = None
    def open_spreedsheet(self) -> xw.Sheet:
        if self.sheet:
            return self.sheet
        workbook = xw.Book(self.file)
        sheet = workbook.sheets['Resumo']
        
        self.sheet = sheet
        return self.sheet
    
    @staticmethod
    def get_last_row(sheet: xw.Sheet, column:str) -> int:
        """Retorna o número da última linha preenchida na coluna A."""
        return sheet.range(f"{column}" + str(sheet.cells.last_cell.row)).end('up').row

    @staticmethod
    def filter_column(sheet: xw.Sheet, column_index: int, criteria1: str, criteria2:str) -> None:
        """Aplica um filtro em uma coluna específica com base nos critérios fornecidos."""

        sheet.range('A1').expand().api.AutoFilter(column_index, criteria1, Operator=1, Criteria2=criteria2)
    @staticmethod
    def get_datas(sheet: xw.Sheet, filter_column: int, criterios:list,filter_column2:int,criterios2:str) -> list:
        # Obtenha todos os dados
        datas = sheet.range('B5').expand().value
        cabecalho = datas[0]
        resultados = []

        for linha in datas[1:]:  # Começando da segunda linha para ignorar o cabeçalho
            if linha[filter_column] in criterios and linha[filter_column2] in criterios2:
                # Criar um dicionário para a linha
                linha_dict = {cabecalho[i]: linha[i] for i in range(len(cabecalho))}
                resultados.append(linha_dict)

        return resultados
            
    @staticmethod
    def insert_data_in_spreadsheet(sheet: xw.Sheet, data: list, start_row: int) -> None:
        """Insere dados na planilha a partir da linha especificada."""
        sheet.range(f'A{start_row}').value = data
    

if __name__  == "__main__":
    ...
   