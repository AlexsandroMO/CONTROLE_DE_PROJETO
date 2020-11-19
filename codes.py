import numpy as np
import pandas as pd
import sqlite3
import pandasql as ps
from datetime import datetime
import xlrd

def ronina_carrega_pl():
    print('-------------- entrou!')
    def cria_user(doc_name, code_doc, format_doc, doc_type, date_today):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        qsl_datas = f"""
                    INSERT INTO taskproject_documentstandard(documment_name, doc_type, doc_format, doc_type_page, created_doc, update_doc)
                    VALUES ('{doc_name}','{code_doc}','{format_doc}','{doc_type}','{date_today}','{date_today}');
                    """
        c.execute(qsl_datas)
        conn.commit()
        conn.close()

    date_today = datetime.today()

    print('--------------', date_today)

    df = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','MODELO_DOCUMENTO')

    for a in range(len(df['LISTA_DOCUMENTOS'])):
        doc_name = df['LISTA_DOCUMENTOS'].loc[a]
        code_doc = df['COD_DOC_TIPO'].loc[a]
        format_doc = df['FORMATO'].loc[a]
        doc_type = df['TIPO'].loc[a]


        cria_user(doc_name, code_doc, format_doc, doc_type, date_today)


    return 'Feito!'