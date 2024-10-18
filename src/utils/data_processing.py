import sys
import os
# Adiciona o diretório 'src' ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from service.ExcelService import Excel
from service.PdfService import PdfService

def pdf_processing(file_pdf:str, type:str) -> list :
    data_pdf = PdfService._read_pdf(file_pdf, type)
    lista = []
    for pdf in data_pdf:
       text = pdf.__dict__
       lista.append(text)
    return lista
def excel_processing(file_excel, type:str):
    excel = Excel(file_excel)
    sheet = excel.open_spreadsheet()
    datas_excel = excel.get_datas(sheet, 0,['Em tratamento com o fornecedor','Em tratamento BENTLY'],1,type)
    return datas_excel

def process_excel_data(datas_excel:list):
    print('Pegando dados do Excel...')
    list_excel = []
    
    for data in datas_excel:
        excel_data = data.get('Nº do Documento') 
        if isinstance(excel_data, float):
            cleaned_excel_data = str(int(excel_data))
        else:
            cleaned_excel_data = excel_data
        list_excel.append(cleaned_excel_data)
        
    return list_excel

def process_pdf_data(datas_pdf:list):
    print('Pegando dados do PDF...')
    list_pdf = []
    
    for data in datas_pdf:
        pdf_data = data.get('datas', {}).get('NumeroNota', '')
        cleaned_pdf_data = pdf_data.lstrip('0')
        list_pdf.append(cleaned_pdf_data)
        
    return list_pdf
def compare_data(list_excel:list, list_pdf:list):
    diferentes = set(list_pdf) - set(list_excel)  # Números que estão em list_pdf e não em list_excel
    somente_excel = set(list_excel) - set(list_pdf)  # Números que estão em list_excel e não em list_pdf
    
    return diferentes, somente_excel

if __name__ == "__main__":
    ...