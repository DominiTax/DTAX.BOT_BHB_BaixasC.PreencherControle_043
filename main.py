import sys
import os
# Adiciona o diretório 'src' ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from service.ExcelService import Excel
from service.PdfService import PdfService


def step1(file_excel, file_pdf):
    pefin_pdf = PdfService._read_pdf(file_pdf, 'Pefin')
    excel = Excel(file_excel)
    sheet = excel.open_spreedsheet()
    datas = excel.get_datas(sheet, 0,['Em tratamento com o fornecedor','Em tratamento BENTLY'],1,'Pefin')
    pefin_excel = datas
    print(pefin_excel)
    print(pefin_pdf)




def step2():
    pass


if __name__ == "__main__":
    ...