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
def excel_processing(file_excel, type:str, list_filter:list,text:str):    
    excel = Excel(file_excel)
    sheet = excel.open_spreadsheet()
    logger.info(f'Abrindo a planilha{file_excel}')

    datas_excel = excel.get_datas(sheet, 0,list_filter,1,type,text)

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
            list_excel.append({'doc': cleaned_excel_data,'linha': data.get('Linha')})
            logger.info(f'Dados tratados Excel: {list_excel}')
        return list_excel
    else:
        for data in datas_excel:
            if isinstance(data,float) or data is not None:
                excel_data = data.get('Valor ($)')
                valor_decimal = excel_data.quantize(Decimal("0.01")).normalize()
                valor_formatado = f'R$: {valor_decimal:,.2f}'.replace(',', 'X').replace('.', ',').replace('X', '.')
                linha_dict ={
                    'linha': data.get('Linha'),
                    'Total': valor_formatado
                }
                list_excel.append(linha_dict)
                logger.info(f'Dados tratados Excel: {list_excel}')
            
    return list_excel

def process_pdf_data(datas_pdf:list, type_pdf:str):
    list_pdf = []
    logger.info('Tratando o numero do Documento pdf para comparação')
    if type_pdf == 'Pefin':
        for data in datas_pdf:
            pdf_data = data.get('datas', {}).get('NumeroNota', '')
            cleaned_pdf_data = pdf_data.lstrip('0')
            list_pdf.append(cleaned_pdf_data)
            logger.info(f'Dados tratados Pdf: {list_pdf}')
    else:
        for data in datas_pdf:
            pdf_data = data.get('datas', {}).get('total', '')
            cleaned_pdf_data = 'R$: ' + pdf_data 
            list_pdf.append(cleaned_pdf_data)
            logger.info(f'Dados tratados Pdf {list_pdf}')
    return list_pdf
def compare_data(list_excel:list, list_pdf:list):
    values_excel = {item['doc'] for item in list_excel}
    # Converte a lista do PDF para um conjunto
    values_pdf = set(list_pdf)
    
    # Encontra os valores que estão no list_excel mas não no list_pdf
    only_in_excel = values_excel - values_pdf
    # Encontra os valores que estão no list_pdf mas não no list_excel
    only_in_pdf = values_pdf - values_excel

    # Cria um novo dicionário para os valores somente em Excel
    new_excel_dict = [item for item in list_excel if item['doc'] in only_in_excel]
    
    return new_excel_dict, only_in_pdf

def compare_data_protesto(list_excel:dict, list_pdf:list):
    values_excel = {item['Total'] for item in list_excel}
    # Converte a lista do PDF para um conjunto
    values_pdf = set(list_pdf)
    
    # Encontra os valores que estão no list_excel mas não no list_pdf
    only_in_excel = values_excel - values_pdf
    # Encontra os valores que estão no list_pdf mas não no list_excel
    only_in_pdf = values_pdf - values_excel

    # Cria um novo dicionário para os valores somente em Excel
    new_excel_dict = [item for item in list_excel if item['Total'] in only_in_excel]
    
    return new_excel_dict, only_in_pdf

if __name__ == "__main__":
    ...