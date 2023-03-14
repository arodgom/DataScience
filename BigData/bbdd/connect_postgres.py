# CRUD : Create, Read, Update, Delete
# pip install psycopg2-binary

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(user='IsaMan', password='cursoPython',
                        database='itti', host='localhost', port=5432) 

cur = conn.cursor()

def createDatabase():
    conn = psycopg2.connect(user='IsaMan', password='cursoPython',
                            host='localhost', port=5432) 
    
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    
    cur = conn.cursor()
    
    try:
        cur.execute(sql.SQL("CREATE DATABASE {};").format(sql.Identifier("itti")))
    except psycopg2.Error as e:
        print("Error al crear la base de datos: %s" % str(e))
    
    cur.close()
    conn.close()

# createDatabase()

    
def createTable(cur):
    try:
        cur.execute("CREATE TABLE notas(name varchar(80), age int, grades real, date date)")
    except psycopg2.Error as e:
        print("Error al crear tabla: %s" % str(e))
    
# createTable(cur) 


def insertar(cur):
    try:
        cur.execute("INSERT INTO notas VALUES(%s, %s, %s, %s)", ("Jose Peña", 205, 7.6, "07/07/2023"))
    except psycopg2.Error as e:
        print("Error al insertar dato: %s" % str(e))
        
# insertar(cur)

def actualizar(cur):
    try:
        cur.execute("UPDATE notas SET grades=9.5 WHERE name='Isabel Maniega'")
    except psycopg2.Error as e:
        print("Error al actualizar dato: %s" % str(e))

# actualizar(cur)


def eliminar(cur):
    try:
        cur.execute("DELETE FROM notas WHERE name='Isabel Maniega'")
    except psycopg2.Error as e:
        print("Error al eliminar dato: %s" % str(e))

# eliminar(cur)

def mostrar(cur):
    try:
        cur.execute("SELECT * FROM notas;")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except psycopg2.Error as e:
        print("Error al mostrar datos: %s" % str(e))

mostrar(cur)


conn.commit()

cur.close()
conn.close()