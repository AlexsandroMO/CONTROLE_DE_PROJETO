
import numpy as np
import pandas as pd
import sqlite3
import pandasql as ps
from datetime import datetime


#Trata Cotation lista
#-----------------------------------
def trata_cotation(cost_type, cost_proj):
    
    print('>>>>>>>>>>>>', cost_type, cost_proj)

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

    def cria_cota(proj_name_id,subject_name_id,doc_name_id,qt_page,qt_doc,qt_h,cost_doc,date_today):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        qsl_datas = f"""
                    INSERT INTO taskproject_cotation(proj_name_id,subject_name_id,doc_name_id,qt_page,qt_doc,qt_hh,cost_doc,created_ct,update_ct)
                    VALUES ('{proj_name_id}','{subject_name_id}','{doc_name_id}','{qt_page}','{qt_doc}','{qt_hh}','{cost_doc}','{date_today}','{date_today}');
                    """
        c.execute(qsl_datas)
        conn.commit()
        conn.close()

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

        list_ids.append([A, B, C,df_cota['QT_FOLHA'].loc[i], df_cota['QT_DOC'].loc[i],df_cota['QT_HH'].loc[i], df_cota['CUSTO_DOC'].loc[i], date_today, date_today])
            
    
    new_df = pd.DataFrame(data=list_ids,columns=['proj_name_id','subject_name_id','doc_name_id','qt_page','qt_doc','qt_hh','cost_doc','created_ct','update_ct'])

    for a in range(len(new_df['proj_name_id'])):
        proj_name_id = new_df['proj_name_id'].loc[a]
        subject_name_id = new_df['subject_name_id'].loc[a]
        doc_name_id = new_df['doc_name_id'].loc[a]
        qt_page = new_df['qt_page'].loc[a]
        qt_doc = new_df['qt_doc'].loc[a]
        qt_hh = new_df['qt_hh'].loc[a]
        #cost_hh = 100 * qt_hh
        if cost_type == 'option1':
            cost_doc = cost_proj[0] * qt_hh

        elif cost_type == 'option2':
            cost_doc = cost_proj[1] * qt_doc

        elif cost_type == 'option3':
            cost_doc = cost_proj[2] * qt_page
   
        cria_cota(proj_name_id,subject_name_id,doc_name_id,qt_page,qt_doc,qt_hh,cost_doc,date_today)

    
    return 'Feito!'
    



def cria_orc(result_itens):

    def read_sql_doc(id): #Information Tables Read
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_DocumentStandard
                    WHERE id = {id};
        """

        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db


    def cria_cotation(proj_name,subj_name,doc_name,doc_type,page_type,format_doc,date_today):
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

        qsl_datas = f"""
                    INSERT INTO taskproject_cotation(proj_name_id,subject_name_id,doc_name_id,doc_type_id,page_type_id,format_doc_id,created_ct,update_ct)
                    VALUES ('{proj_name}','{subj_name}','{doc_name}','{doc_type}','{page_type}','{format_doc}','{date_today}','{date_today}');
                    """
        c.execute(qsl_datas)
        conn.commit()
        conn.close()


    date_today = datetime.today()
    print('\n-----------------------------')
    
    for i in range(len(result_itens[1])):
        print('i:        ',result_itens[1][i])
        doc = read_sql_doc(int(result_itens[1][i]))
        print('entrou!!!!', doc)

        cria_cotation(int(result_itens[0][1]), int(result_itens[0][2]), doc['id'].loc[0], doc['doc_type_id'].loc[0],doc['doc_type_page_id'].loc[0],doc['format_doc_id'].loc[0], date_today)

 
    return 'feito!'



