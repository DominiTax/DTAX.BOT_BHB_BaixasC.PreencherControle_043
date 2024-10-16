import sys
import os
# Adiciona o diretório 'src' ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from service.ExcelService import Excel
from service.PdfService import PdfService
from utils.logs import logger

def pdf_processing(file_pdf:str, type:str) -> list :
    data_pdf = PdfService._read_pdf(file_pdf, type)
    lista = []
    for pdf in data_pdf:
       text = pdf.__dict__
       lista.append(text)
    logger.info(f'dados transformados em dict:{lista}')
    return lista
def excel_processing(file_excel, type:str):
    excel = Excel(file_excel)
    sheet = excel.open_spreadsheet()
    logger.info(f'Abrindo a planilha{file_excel}')
    datas_excel = excel.get_datas(sheet, 0,['Em tratamento com o fornecedor','Em tratamento BENTLY'],1,type)

    return datas_excel

def process_excel_data(datas_excel:list):
    list_excel = []
    logger.info('Tratando o numero do Documento Excel para comparação')
    for data in datas_excel:
        excel_data = data.get('Nº do Documento') 
        if isinstance(excel_data, float):
            cleaned_excel_data = str(int(excel_data))
        else:
            cleaned_excel_data = excel_data
        list_excel.append(cleaned_excel_data)
        logger.info(f'Dados tratados{list_excel}')
        
    return list_excel

def process_pdf_data(datas_pdf:list):
    list_pdf = []
    logger.info('Tratando o numero do Documento pdf para comparação')
    for data in datas_pdf:
        pdf_data = data.get('datas', {}).get('NumeroNota', '')
        cleaned_pdf_data = pdf_data.lstrip('0')
        list_pdf.append(cleaned_pdf_data)
        logger.info(f'Dados tratados{list_pdf}')
        
    return list_pdf
def compare_data(list_excel:list, list_pdf:list):
    logger.info('Comparando dados')
    diferentes = set(list_pdf) - set(list_excel)
    logger.info('Dados diferentes do pdf para o excel')  # Números que estão em list_pdf e não em list_excel
    somente_excel = set(list_excel) - set(list_pdf)  # Números que estão em list_excel e não em list_pdf
    logger.info('Dados que somente tem no excel')    

    return diferentes, somente_excel

if __name__ == "__main__":
    ...