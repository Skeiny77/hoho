import sqlite3
#from sqlite3 import error

def sql_connection():
    try:
        con = sqlite3.connect('sesion13_g31.db')
        return con
    except :
        print ('error')

def sql_login(usuario, contrasena):
    #strsql = f"select * from login where usuario = '{usuario}' and password = '{contrasena}'"
    strsql = ("select * from login where usuario = ? and password = ?;",(usuario, contrasena))
    print(strsql)#' or ''='
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.executescript(*strsql)
    usuarios = cursorObj.fetchall()
    return usuarios

def sql_inyeccion_javascript():
    strsql = "select * from usuarios"
    print(strsql)#' or ''='
    con = sql_connection()
    cursorObj = con.cursor()
    cursorObj.execute(strsql)
    usuarios = cursorObj.fetchone()
    return usuarios