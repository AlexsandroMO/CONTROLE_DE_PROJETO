import numpy as np
import pandas as pd
import sqlite3
import pandasql as ps
from datetime import datetime
import xlrd


def delete_befor():
    #------------------------------------------------
    def read_proj():
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_myproject;
        """
        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db


    def read_sub():
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_subject;
        """
        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db


    def read_doc():
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_documentstandard;
        """
        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db


    def read_emp():
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_employee;
        """
        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db


    def read_st():
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_statusdoc;
        """
        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db


    def read_ac():
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_action;
        """
        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db

 
    #------------------------------------------------
    new_proj, new_sub, new_doc, new_emp, new_st, new_ac = [],[],[],[],[],[]
    
    #------------------------------------------------
    for i in read_proj()['id']:
        new_proj.append(i)

    for i in read_sub()['id']:
        new_sub.append(i)

    for i in read_doc()['id']:
        new_doc.append(i)

    for i in read_emp()['id']:
        new_emp.append(i)

    for i in read_st()['id']:
        new_st.append(i)

    for i in read_ac()['id']:
        new_ac.append(i)

    read_all = [new_proj, new_sub, new_doc, new_emp, new_st, new_ac]

    return read_all

    

def delete_cotation():
    #------------------------------------------------
    def read_cota():
        conn = sqlite3.connect('db.sqlite3')
        sql_datas = f"""
                    SELECT * FROM taskproject_cotation;
        """
        read_db = pd.read_sql_query(sql_datas, conn)
        conn.close()
        
        return read_db

    new_cota = []

    for i in read_cota()['id']:
        new_cota.append(i)

    read_all = new_cota

    return read_all