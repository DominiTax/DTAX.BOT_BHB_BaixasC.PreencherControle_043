from utils.data_processing import pdf_processing,excel_processing,process_excel_data,process_pdf_data,compare_data
from service.ExcelService import Excel
from utils.logs import logger


def step1_pefin(file_pdf:str, type_pdf:str,file_excel:str, type_excel:str):
    datas_excel = excel_processing(file_excel, type_excel)
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
    last_row = excel.get_last_row('B')
    logger.info(f'Obtendo a ultima linha{last_row}')
    result_pdf = []
    for data in datas_pdf:
        if data.get('datas').get('NumeroNota').lstrip('0') in diferentes: 
            result_pdf.append(data.get('datas'))
    excel.insert_data_in_spreadsheet_new(result_pdf, last_row, type_excel)

    
def step2_protesto(file_pdf:str, type_pdf:str,file_excel:str, type_excel:str):
    datas_excel = excel_processing(file_excel, type_excel)
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
        datas = data.replace("R$: ","")
        dados_tratados.append(datas)
    print(dados_tratados)
    rows_list = excel.find_row_by_criteria('G',list(dados_tratados),type_excel)
    logger.info('Colocando status como conluidos')
    excel.insert_data_in_spreadsheet_concluido('Concluído',rows_list,'B')
    #Inseri os dados que não tem no Excel e que tem no pdf
    if diferentes:
        last_row = excel.get_last_row('B')
        logger.info(f'Obtendo a ultima linha{last_row}')
        result_pdf = []
        for data in datas_pdf:
            if data.get('datas').get('Valor ($)') in diferentes: 
                result_pdf.append(data.get('datas'))
        excel.insert_data_in_spreadsheet_new(result_pdf, last_row, type_excel)
    else: 
        logger.info('Fim do processo')

if __name__ == "__main__":
    teste = step1_pefin(r'C:\Users\christian.silva\Desktop\DTAX.BOT_BHB_BaixasC.PreencherControle_043\src\temp\RelatrioSERASA04Set2024-BentlyCNPJ01.128.902_0001-701.pdf', 'Pefin', r'C:\Users\christian.silva\Desktop\DTAX.BOT_BHB_BaixasC.PreencherControle_043\src\temp\2024-BENTLY-Macro-ProjetoBaixasCartorrias.xlsm','Pefin')
    teste = step2_protesto(r'C:\Users\christian.silva\Desktop\DTAX.BOT_BHB_BaixasC.PreencherControle_043\src\temp\RelatrioSERASA04Set2024-BentlyCNPJ01.128.902_0001-701.pdf', 'Protesto', r'C:\Users\christian.silva\Desktop\DTAX.BOT_BHB_BaixasC.PreencherControle_043\src\temp\2024-BENTLY-Macro-ProjetoBaixasCartorrias.xlsm','Protesto')
    