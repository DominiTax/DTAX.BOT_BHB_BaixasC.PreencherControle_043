import sys
import os
import openpyxl
# Adiciona o diretório 'src' ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from service.ExcelService import Excel
from service.PdfService import PdfService

def pdf_processing(file_pdf):
    data_pdf = PdfService._read_pdf(file_pdf, 'Pefin')
    lista = []
    for pdf in data_pdf:
       text = pdf.__dict__
       lista.append(text)
    return lista
def excel_processing(file_excel):
    excel = Excel(file_excel)
    sheet = excel.open_spreedsheet()
    datas = excel.get_datas(sheet, 0,['Em tratamento com o fornecedor','Em tratamento BENTLY'],1,'Pefin')
    data_excel = datas
    return data_excel


if __name__ == "__main__":
    ...