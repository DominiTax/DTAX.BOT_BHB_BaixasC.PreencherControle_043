from utils.data_processing import pdf_processing,excel_processing,process_excel_data,process_pdf_data,compare_data


def step1_pefin(file_pdf:str, type_pdf:str,file_excel:str, type_excel:str):
    datas_excel = excel_processing(file_excel, type_excel)
    list_excel = process_excel_data(datas_excel)

    datas_pdf = pdf_processing(file_pdf, type_pdf)
    list_pdf = process_pdf_data(datas_pdf)

    compare_data(list_excel, list_pdf)
    print(compare_data)
    # print('pegando dados Excel')
    # list_excel = []
    # list_pdf = []
    # for data in datas_excel:
    #     excel_data = data.get('Nº do Documento')
    #     if isinstance(excel_data, float):
    #         cleaned_excel_data = str(int(excel_data))
    #     else:
    #         cleaned_excel_data = excel_data
    #     list_excel.append(cleaned_excel_data)
    # datas_pdf = pdf_processing(file_pdf, type_pdf)
    # print('pegando dados pdf')
    # for data in datas_pdf: 
    #     pdf_data = data.get('datas').get('NumeroNota')
    #     cleaned_pdf_data = pdf_data.lstrip('0')
    #     list_pdf.append(cleaned_pdf_data)
    # diferentes = set(list_pdf) - set(list_excel)  # Números que estão em list_pdf e não em list_excel (adicionar o valor)
    # print(diferentes)
    # # Números que estão em list_excel e não em list_pdf (concluidos)
    # somente_excel = set(list_excel) - set(list_pdf)
    # print(somente_excel)
def step2_protesto():
    pass


if __name__ == "__main__":
    teste = step1_pefin(r'C:\Users\christian.silva\Desktop\DTAX.BOT_BHB_BaixasC.PreencherControle_043\src\temp\RelatrioSERASA04Set2024-BentlyCNPJ01.128.902_0001-701.pdf', 'Pefin', r'C:\Users\christian.silva\Desktop\DTAX.BOT_BHB_BaixasC.PreencherControle_043\src\temp\2024-BENTLY-Macro-ProjetoBaixasCartorrias.xlsm','Pefin')
    