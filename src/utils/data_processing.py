import sys
import os
# Adiciona o diretório 'src' ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from service.ExcelService import Excel
from service.PdfService import PdfService
from utils.logs import logger
from decimal import Decimal


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

    datas_excel = excel.get_datas(sheet, 0,['Em tratamento com o fornecedor','Em tratamento com financeiro Domini','Em tratamento BENTLY','Em tratamento Bently'],1,type)

    return datas_excel

def process_excel_data(datas_excel:list,type_excel:str):
    list_excel = []
    logger.info('Tratando o numero do Documento Excel para comparação')
    if type_excel == 'Pefin':
        for data in datas_excel:
            excel_data = data.get('Nº do Documento') 
            if isinstance(excel_data, float):
                cleaned_excel_data = str(int(excel_data))
            else:
                cleaned_excel_data = excel_data
            list_excel.append(cleaned_excel_data)
            logger.info(f'Dados tratados{list_excel}')
    else:
        for data in datas_excel:
            excel_data = data.get('Valor ($)')
            valor_decimal = excel_data.quantize(Decimal("0.01")).normalize()
            valor_formatado = f'R$: {valor_decimal:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
            list_excel.append(valor_formatado)
            logger.info(f'Dados tratados: {list_excel}')
            
    return list_excel

def process_pdf_data(datas_pdf:list, type_pdf:str):
    list_pdf = []
    logger.info('Tratando o numero do Documento pdf para comparação')
    if type_pdf == 'Pefin':
        for data in datas_pdf:
            pdf_data = data.get('datas', {}).get('NumeroNota', '')
            cleaned_pdf_data = pdf_data.lstrip('0')
            list_pdf.append(cleaned_pdf_data)
            logger.info(f'Dados tratados: {list_pdf}')
    else:
        for data in datas_pdf:
            pdf_data = data.get('datas', {}).get('total', '')
            cleaned_pdf_data = 'R$: ' + pdf_data 
            list_pdf.append(cleaned_pdf_data)
            logger.info(f'Dados tratados: {list_pdf}')
    return list_pdf
def compare_data(list_excel:list, list_pdf:list):
    logger.info('Comparando dados')
    diferentes = set(list_pdf) - set(list_excel)
    logger.info(f'Dados diferentes do pdf para o excel {diferentes}')  # Números que estão em list_pdf e não em list_excel
    somente_excel = set(list_excel) - set(list_pdf)  # Números que estão em list_excel e não em list_pdf
    logger.info(f'Dados que somente tem no excel {somente_excel}')    

    return diferentes, somente_excel

if __name__ == "__main__":
    ...