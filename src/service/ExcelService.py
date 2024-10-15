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
    
    def get_datas(self, filter_column: int, criterios:list, result_column:list) -> list:
        filter_column = 8  # Por exemplo, coluna H
        criterios = ["SANTANA03", "OLIVAMA", "DOSSSAR13"]
        result_column = [12, 24, 1]  # Por exemplo, colunas A, L e X
        workbook = openpyxl.load_workbook(self.file)
        sheet = workbook['Resumo']

        resultados = dict()  # Lista para armazenar resultados

        # Iterar pelas linhas da planilha
        for linha in sheet.iter_rows(min_row=2, values_only=True):  # Ignorar cabeçalho
            if linha[filter_column - 1] in criterios and linha[0] not in resultados.keys():
                # Verifica se o valor na coluna de filtro corresponde
                resultado = tuple(linha[coluna - 1] for coluna in result_column)
                resultados[resultado[0]] = resultado[1:]

                # resultados.add(resultado)  # Adiciona o resultado à lista
        return resultados

            
    @staticmethod
    def insert_data_in_spreadsheet(sheet: xw.Sheet, data: list, start_row: int) -> None:
        """Insere dados na planilha a partir da linha especificada."""
        sheet.range(f'A{start_row}').value = data
    

if __name__  == "__main__":

    ...