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

    def open_spreadsheet(self) -> xw.Sheet:
        if self.sheet:
            return self.sheet
        workbook = xw.Book(self.file)
        sheet = workbook.sheets['Resumo']
        
        self.sheet = sheet
        return self.sheet
    
    def get_last_row(self, column: str) -> int:
        """Retorna o número da última linha preenchida na coluna especificada."""
        if self.sheet.api.AutoFilterMode:
            self.sheet.api.AutoFilterMode = False
        return self.sheet.range(f"{column}{self.sheet.cells.last_cell.row}").end('up').row

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
    def insert_data_in_spreadsheet_concluido(self, data: str, rows: list,col_letter:str,start_col: int =2) -> None:
        """Insere dados na planilha a partir da linha e coluna especificadas."""
        # Define o intervalo para a inserção dos dados
        for value in rows:
            
            range_address = f'{col_letter}{value}'
            
            # Insere os dados
            self.sheet.range(range_address).value = data
            print(f'Colocando cocluido na linha{value}')
    def insert_data_in_spreadsheet_new(self, data: list, rows: int,start_col =2) -> None:
        """Insere dados na planilha a partir da linha e coluna especificadas."""
        # Define o intervalo para a inserção dos dados
        i=1
        for entry in data:
            
            row = rows + i
            
            # Insere os dados
            self.sheet.range(row, start_col).value = entry.get('NumeroNota')
            self.sheet.range(row, start_col+1).value = entry.get('Nome')
            self.sheet.range(row, start_col+2).value = entry.get('Data')
            self.sheet.range(row, start_col+3).value = entry.get('Valor')
            self.sheet.range(row, start_col+4).value = entry.get('CNPJ')
            print(f'Colocando cocluido na linha{row}')
            i+=1 

    def find_row_by_criteria(self, column, criterios):
        """Encontra a primeira linha que atende ao critério especificado na coluna dada."""  # Você pode ajustar a coluna se necessário
        last_row = Excel.get_last_row(self, column)
        linhas_encontradas = []
        for i in range(1, last_row + 1):  # Começando em 1 para ignorar o cabeçalho
            valor = self.sheet.range(f'{column}{i}').value
            if isinstance(valor, float):
                cleaned_excel_data = str(int(valor))
            else:
                cleaned_excel_data = valor
            if cleaned_excel_data in criterios:
                linhas_encontradas.append(i)
        return linhas_encontradas
    

if __name__  == "__main__":
    ...
   