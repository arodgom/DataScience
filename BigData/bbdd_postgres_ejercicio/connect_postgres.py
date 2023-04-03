# CRUD : Create, Read, Update, Delete
# pip install psycopg2-binary

import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = psycopg2.connect(user='arodgom', password='ejercicio',
                        database='actividad', host='localhost', port=5432) 

cur = conn.cursor()

def createDatabase():
    conn = psycopg2.connect(user='arodgom', password='ejercicio',
                            host='localhost', port=5432) 
    
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    
    cur = conn.cursor()
    
    try:
        cur.execute(sql.SQL("CREATE DATABASE {};").format(sql.Identifier("actividad")))
    except psycopg2.Error as e:
        print("Error al crear la base de datos: %s" % str(e))
    
    cur.close()
    conn.close()

# createDatabase()

    
def createTable_edicion(cur):
    try:
        cur.execute("CREATE TABLE edicion(id_edic serial primary key, numero varchar)")
    except psycopg2.Error as e:
        print("Error al crear tabla: %s" % str(e))
    
# createTable_edicion(cur) 

def createTable_notas(cur):
    try:
        cur.execute("CREATE TABLE notas(id_notas serial primary key, name varchar, edad int, notas real, id_edic int)")
    except psycopg2.Error as e:
        print("Error al crear tabla: %s" % str(e))
    
# createTable_notas(cur) 


def insertar_edicion(cur):
    try:
        consulta = "INSERT INTO edicion VALUES (%s, %s);"
        cur.execute(consulta, (1, "Uno"))
        cur.execute(consulta, (2, "Dos"))
        cur.execute(consulta, (3, "Tres"))
    except psycopg2.Error as e:
        print("Error al insertar dato: %s" % str(e))
        
# insertar_edicion(cur)

def insertar_notas(cur):
    try:
        consulta2 = "INSERT INTO notas VALUES (%s, %s, %s, %s, %s);"
        cur.execute(consulta2, (1, "Isabel Maniega", 30, 5.6, 1))
        cur.execute(consulta2, (2, "José Manuel Peña", 30, 7.8, 1))
        cur.execute(consulta2, (3, "Pedro López", 25, 5.2, 2))
        cur.execute(consulta2, (4, "Julia García", 22, 7.3, 1))
        cur.execute(consulta2, (5, "Amparo Mayora", 28, 8.4, 3))
        cur.execute(consulta2, (6, "Juan Martínez", 30, 6.8, 3))
        cur.execute(consulta2, (7, "Fernando López", 35, 6.1, 2))
        cur.execute(consulta2, (8, "María Castro", 41, 5.9, 3))
                     
    except psycopg2.Error as e:
        print("Error al insertar dato: %s" % str(e))
        
# insertar_notas(cur)

def actualizar(cur):
    try:
        cur.execute("UPDATE notas SET notas=6.4 WHERE id_notas='3'")
        cur.execute("UPDATE notas SET notas=5.2 WHERE id_notas='8'")
    except psycopg2.Error as e:
        print("Error al actualizar dato: %s" % str(e))

# actualizar(cur)


def eliminar(cur):
    try:
        cur.execute("DELETE FROM notas WHERE name='Pedro López'")
    except psycopg2.Error as e:
        print("Error al eliminar dato: %s" % str(e))

# eliminar(cur)

conn.commit()

cur.close()
conn.close()