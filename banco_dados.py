import sqlite3

conn = sqlite3.connect("galeria.db")

cursor = conn.cursor()

def criar_tabela():
    sql = """
    CREATE TABLE albums(titulo text, artista text, data_lancamento text,
    data_publicacao text, midia text)
    """

    cursor.execute(sql)

    conn.commit()

def grava_album():
    sql = "INSERT INTO albums VALUES('Glow', 'Andy Hunter', '24/07/2012','Xplore Records', 'MP3')"

    cursor.execute(sql)

    conn.commit()


def grava_muitos():
    albums = [('Exodus', 'Andy Hunter', '9/7/2002', 'Sparroe Records', 'CD'),
              ('Until We Have Faces', 'Red', '1/2/2011', 'Essential Records', 'CD')]


    cursor.executemany("INSERT INTO albums VALUES(?,?,?,?,?)", albums)


    conn.commit()
     

def atualiza ():
    sql = """
    UPDATE albums SET artista = 'Jonh Doe'
    where artista = 'Andy Hunter'
    """

    cursor.execute(sql)
    conn.commit()


def excluir():
    sql = """
    DELETE FROM albums where artista = 'Jonh Doe'
    """

    cursor.execute(sql)

    conn.commit()

def listar():
    sql = """
    SELECT rowid, * FROM albums ORDER BY artista
    """

    cursor.execute(sql)

    for row in cursor.fetchall()
    print(row)
    
    





























    

