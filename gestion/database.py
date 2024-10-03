import sqlite3

data = sqlite3.connect("first.db")
cur = data.cursor()

cur.execute(
    '''CREATE TABLE IF NOT EXISTS pers(
    id INTEGER PRIMARY KEY,
    nom TEXT,
    prenom TEXT,
    class TEXT
    );'''
)



eleves= [(6, "BOO", "ALBERT", "TleC2"), (2, "SONDE", "daniel", "5ème"), (3, "KOY", "jean", "4ème"),
          (4, "POUHE", "bellarmin", "CM1"), (5, "SONG KOY", "sami", "CE2")]

"""cur.executemany(
    '''INSERT INTO eleve VALUES(?,?,?,?);''',eleves)

"""
cur.execute(
    '''
    SELECT *
    FROM eleve ;
    '''
)

lab = cur.fetchall()

for el in lab:
    print("l'eleve numero %s s'appelle %s %s et il fait la classe de %s" %(el[0], el[2], el[1], el[3] ))

data.commit()