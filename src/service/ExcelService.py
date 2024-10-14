import xlwings as xw
import sys
import os
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
    def filter_column(sheet: xw.Sheet, column_index: int, criteria: str) -> None:
        """Aplica um filtro em uma coluna específica com base nos critérios fornecidos."""
        sheet.range('A1').expand().api.AutoFilter(column_index, criteria)
    @staticmethod
    def get_datas(sheet: xw.Sheet, column_index: int) -> list:
        """Retorna os dados visíveis em uma coluna específica após a aplicação do filtro."""
        # Obtenha o intervalo da coluna
        # range_to_check = sheet.range('F500:F600')

        # # visible_values = []
        # # for cell in range_to_check:
        # #     if not cell.api.EntireRow.Hidden:
        # #         visible_values.append(cell.value)
        # # return visible_values
        
        # visible_cells = range_to_check.api.SpecialCells(12)

        # # # Faz algo com as células visíveis (exemplo: imprimir os valores)
        # for cell in visible_cells:
        #     print(cell.value)
            
    @staticmethod
    def insert_data_in_spreadsheet(sheet: xw.Sheet, data: list, start_row: int) -> None:
        """Insere dados na planilha a partir da linha especificada."""
        sheet.range(f'A{start_row}').value = data

if __name__  == "__main__":
    ...