
import numpy as np
import pandas as pd
import sqlite3
import pandasql as ps
from datetime import datetime


   #Trata Cotation lista
    #-----------------------------------
def trata_cotation():

    df_cota = pd.read_excel('media_files/uploads/TABELAS_PROJETO_CONTROLE_DE_PROJETO.xlsx','COTATION_DOC')

    def read_sql_proj(): #Information Tables Read
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_myproject;
        """

        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db

    def read_sql_subj(): #Information Tables Read
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_subject;
        """

        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db

    def read_sql_doc(): #Information Tables Read
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_documentstandard;
        """

        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db




    date_today = datetime.today()

    list_ids = []
    A, B, C = '','',''

    for i in range(len(df_cota['PROJETO'])):
        for a in range(len(read_sql_proj()['project_name'])): 
            if read_sql_proj()['project_name'].loc[a] == df_cota['PROJETO'].loc[i]:
                A = read_sql_proj()['id'].loc[a]

        for b in range(len(read_sql_subj()['subject_name'])): 
            if read_sql_subj()['subject_name'].loc[b] == df_cota['DISCIPLINA'].loc[i]:
                B = read_sql_subj()['id'].loc[b]

        for c in range(len(read_sql_doc()['doc_type'])): 
            if read_sql_doc()['doc_type'].loc[c] == df_cota['COD_DOC_TIPO'].loc[i]:
                C = read_sql_doc()['id'].loc[c]

        list_ids.append([A, B, C,df_cota['QT_FOLHA'].loc[i], df_cota['QT_DOC'].loc[i],df_cota['QT_HH'].loc[i], df_cota['CUSTO_HH'].loc[i], df_cota['CUSTO_DOC'].loc[i], date_today, date_today])
            
    
    new_df = pd.DataFrame(data=list_ids,columns=['proj_name_id','subject_name_id','doc_name_id','qt_page','qt_doc','qt_hh','cost_hh','cost_doc','created_ct','update_ct'])

    return new_df
    