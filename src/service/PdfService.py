import sys
import os
# Adiciona o diretório 'src' ao PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.DocModel import DocModel
from utils.pdf_utils import extract_pdf_text
import traceback
from datetime import datetime
import re

class PdfService:
    @staticmethod
    def _read_pdf(file:str, filter:str):
            extract_text = extract_pdf_text(file)
             # Dividindo o texto em partes usando 'Protestos '
            parts = extract_text.split('Protestos\n ')  # Limita a 1 divisão

            # Verificando se obteve exatamente duas partes
            if len(parts) == 2:
                index1, index2 = parts
                
                # Filtrando os dados com base na condição
                if filter == "Pefin":
                    pdf_pefin = PdfService._get_datas_pdf_perfin(index1)
                    return pdf_pefin
                elif filter == "protestos":
                    part = index2.split('\nTotal')
                    pdf_protesto = PdfService._get_datas_pdf_protesto(part[0])
                    return pdf_protesto
            else:
                raise ValueError("O texto não contém a divisão esperada.")
    
    def _get_datas_pdf_perfin(text:str) -> list[DocModel]:
        pattern = r"(?P<NumeroNota>\d+)(?P<Nome>\D+)(?P<Data>[\d\/]*) (?P<Valor>[\d\.\,]+)[\s\S]+?Credor.+?(?P<CNPJ>\d{2}\.\d{3}\.\d{3}\/\d{4}-\d{2})"
        matches = re.finditer(pattern, text)

        doc_model_list: list[DocModel] = []
        try:
            for match in matches:
                dados = match.groupdict()
                doc_model = DocModel(dados,type='Perfin',inclusion_data=datetime.now())
                doc_model_list.append(doc_model)
            return doc_model_list
        except Exception as e:
            return traceback.format_exc(e)
    def _get_datas_pdf_protesto(text:str) -> list[DocModel]:
        pattern = r'\d{2}\/\d{2}\/\d{4} (?P<total>.+)'
        matches = re.finditer(pattern, text)
        try:
            doc_model_list: list[DocModel] = []
            for match in matches:
                dados = match.groupdict()
                doc_model = DocModel(dados,type='Protesto',inclusion_data=datetime.now())
                doc_model_list.append(doc_model)
            return doc_model_list
        except Exception as e:
            return traceback.format_exc(e)
    
if __name__ == '__main__':
   ...
    

