from utils.data_processing import pdf_processing,excel_processing,process_excel_data,process_pdf_data,compare_data
from service.ExcelService import Excel
from utils.logs import logger
from PySide6.QtWidgets import QApplication
from GoWindow.views.ui import (
    StartWindow,
    InstructionWindow,
    FileWindow,
    FolderWindow,
    DateWindow,
    SuccessWindow,
    ErrorWindow
)
from GoWindow.controller import Controller
from window.window_selector import SelectButtonWindow, SelectTextWindow2

def step1_pefin(file_pdf:str, type_pdf:str,file_excel:str, type_excel:str, list_filter:list,text:str):
    datas_excel = excel_processing(file_excel,type_excel,list_filter,text)
    list_excel = process_excel_data(datas_excel, type_excel)

    datas_pdf = pdf_processing(file_pdf, type_pdf)
    list_pdf = process_pdf_data(datas_pdf, type_pdf)
    #Faz a verificação se tem no excel e no pdf
    diferentes, somente_excel = compare_data(list_excel, list_pdf)
    excel = Excel(file_excel)
    excel.open_spreadsheet()
    excel.filter_column()
    #Altera o status para concluidos por não ter achado no pdf
    logger.info('Realizando o filtro')
    rows_list = excel.find_row_by_criteria('F',list(somente_excel), type_excel)
    logger.info('Colocando status como conluidos')
    excel.insert_data_in_spreadsheet_concluido('Concluído',rows_list,'B')
    #Inseri os dados que não tem no Excel e que tem no pdf
    if diferentes:
        last_row = excel.get_last_row('B')
        logger.info(f'Obtendo a ultima linha{last_row}')
        result_pdf = []
        for data in datas_pdf:
            if data.get('datas').get('NumeroNota').lstrip('0') in diferentes: 
                result_pdf.append(data.get('datas'))
        excel.insert_data_in_spreadsheet_new(result_pdf, last_row, type_excel)
    else: 
        logger.info('Fim do processo')

def step2_protesto(file_pdf:str, type_pdf:str,file_excel:str, type_excel:str, list_filter:list, text:str):
    datas_excel = excel_processing(file_excel, type_excel,list_filter,text)
    list_excel = process_excel_data(datas_excel,type_excel)

    datas_pdf = pdf_processing(file_pdf, type_pdf)
    list_pdf = process_pdf_data(datas_pdf, type_pdf)

    diferentes, somente_excel = compare_data(list_excel, list_pdf)
    excel = Excel(file_excel)
    excel.open_spreadsheet()
    excel.filter_column()
    #Altera o status para concluidos por não ter achado no pdf
    logger.info('Realizando o filtro')
    dados_tratados = []
    for data in somente_excel:
        datas = data.replace("R$: ","").replace(".","")
        dados_tratados.append(datas)
    print(dados_tratados)
    rows_list = excel.find_row_by_criteria('G',list(dados_tratados),type_excel)
    logger.info('Colocando status como conluidos')
    excel.insert_data_in_spreadsheet_concluido('Concluído',rows_list,'B')
    #Inseri os dados que não tem no Excel e que tem no pdf
    diferentes = list(diferentes)
    if diferentes:
        last_row = excel.get_last_row('B')
        logger.info(f'Obtendo a ultima linha{last_row}')
        valores_sem_prefixo = {valor.replace('R$: ', '') for valor in diferentes}
        result_pdf = []
        for data in datas_pdf:
            if data.get('datas').get('total') in valores_sem_prefixo: 
                result_pdf.append(data.get('datas'))
        excel.insert_data_in_spreadsheet_new(result_pdf, last_row, type_excel)
    else: 
        logger.info('Fim do processo')
def main(controller = Controller):
    controller.add_window(SelectButtonWindow,text='lembrando',title='EMPRESAS')
    text = controller.get_specific_data('get_selected_button')
    controller.add_window(SelectTextWindow2,text='tipo', title='tipo')
    type = controller.get_specific_data('get_selected_button')
    if text == 'baker':
        try:
            if type == 'pefin':
                controller.add_window(FileWindow)
                excel_file_path = controller.get_specific_data("get_file_path")
                controller.add_window(FileWindow)
                pdf_file_path = controller.get_specific_data("get_file_path")
                list = ['Em tratamento com o fornecedor','Em tratamento com financeiro Domini','Em tratamento BHB']
                process = step1_pefin(pdf_file_path,'Pefin',excel_file_path,'Pefin',list,text)
                logger.info('Processo concluido')
                controller.add_window(SuccessWindow)
            elif type == 'protesto':
                controller.add_window(FileWindow)
                excel_file_path = controller.get_specific_data("get_file_path")
                controller.add_window(FileWindow)
                pdf_file_path = controller.get_specific_data("get_file_path")
                list = ['Em tratamento com o fornecedor','Em tratamento com financeiro Domini','Em tratamento BHB']
                process = step2_protesto(pdf_file_path,'Protesto',excel_file_path,'Protesto',list,text)
                logger.info('Processo concluido')
                controller.add_window(SuccessWindow)
        except Exception as e:
            controller.add_window(ErrorWindow)
            logger.info(f'Não foi possivel pegar o arquivo {e}')
    elif text == 'bently':
        try:
            if type == 'pefin':
                controller.add_window(FileWindow)
                excel_file_path = controller.get_specific_data("get_file_path")
                controller.add_window(FileWindow)
                pdf_file_path = controller.get_specific_data("get_file_path")
                list = ['Em tratamento com o fornecedor','Em tratamento com financeiro Domini','Em tratamento Bently', 'Em tratamento BENTLY']
                process = step1_pefin(pdf_file_path,'Pefin',excel_file_path,'Pefin',list,text)
                logger.info('Processo concluido')
                controller.add_window(SuccessWindow)
            elif type == 'protesto':
                controller.add_window(FileWindow)
                excel_file_path = controller.get_specific_data("get_file_path")
                controller.add_window(FileWindow)
                pdf_file_path = controller.get_specific_data("get_file_path")
                list = ['Em tratamento com o fornecedor','Em tratamento com financeiro Domini','Em tratamento Bently', 'Em tratamento BENTLY']
                process = step2_protesto(pdf_file_path,'Protesto',excel_file_path,'Protesto',list,text)
                logger.info('Processo concluido')
                controller.add_window(SuccessWindow)
        except Exception as e:
            logger.info(f'Não foi possivel pegar o arquivo {e}')
            controller.add_window(ErrorWindow)
            logger.info(f'Não foi possivel pegar o arquivo {e}')
    else:
        try:
            if type == 'pefin':
                controller.add_window(FileWindow)
                excel_file_path = controller.get_specific_data("get_file_path")
                controller.add_window(FileWindow)
                pdf_file_path = controller.get_specific_data("get_file_path")
                list = ['Em tratamento com o fornecedor','Em tratamento com financeiro Domini','Em tratamento BHB']
                process = step1_pefin(pdf_file_path,'Pefin',excel_file_path,'Pefin',list,text)
                logger.info('Processo concluido')
            elif type == 'protesto':
                controller.add_window(FileWindow)
                excel_file_path = controller.get_specific_data("get_file_path")
                controller.add_window(FileWindow)
                pdf_file_path = controller.get_specific_data("get_file_path")
                list = ['Em tratamento com o fornecedor','Em tratamento com financeiro Domini','Em tratamento BHB']
                process = step2_protesto(pdf_file_path,'Protesto',excel_file_path,'Protesto',list,text)
                logger.info('Processo concluido')
        except Exception as e:
            controller.add_window(ErrorWindow)
            logger.info(f'Não foi possivel pegar o arquivo {e}')

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    controller = Controller(main)
    controller.add_window(StartWindow)
    controller.add_window(InstructionWindow)
    controller.run()
    sys.exit(app.exec())
    # teste = step1_pefin(r'C:\Users\christian.silva\Desktop\DTAX.BOT_BHB_BaixasC.PreencherControle_043\src\temp\RelatrioSERASA04Set2024-BentlyCNPJ01.128.902_0001-701.pdf', 'Pefin', r'C:\Users\christian.silva\Desktop\DTAX.BOT_BHB_BaixasC.PreencherControle_043\src\temp\2024-BENTLY-Macro-ProjetoBaixasCartorrias.xlsm','Pefin')
    # teste = step2_protesto(r'C:\Users\christian.silva\Desktop\DTAX.BOT_BHB_BaixasC.PreencherControle_043\src\temp\RelatrioSERASA04Set2024-BentlyCNPJ01.128.902_0001-701.pdf', 'Protesto', r'C:\Users\christian.silva\Desktop\DTAX.BOT_BHB_BaixasC.PreencherControle_043\src\temp\2024-BENTLY-Macro-ProjetoBaixasCartorrias.xlsm','Protesto')
    