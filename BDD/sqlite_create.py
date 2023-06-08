# SQLITE : CRÉATION DE LA TABLE

import sqlite3

# connexion = "albums2.db"
# executer / curseur
# commit
# fermer

connexion = sqlite3.connect("albums2.db")
curseur = connexion.cursor()

curseur.execute("""CREATE TABLE artiste (
    artiste_id INTEGER NOT NULL PRIMARY KEY, 
    nom VARCHAR);""")

curseur.execute("""CREATE TABLE album (
    album_id INTEGER NOT NULL PRIMARY KEY, 
    artiste_id INTEGER REFERENCES artiste,
    titre VARCHAR,
    annee_sortie INTEGER);""")

curseur.execute('INSERT INTO artiste (nom) VALUES ("Ninho");') # 1
mj_id = curseur.lastrowid
curseur.execute('INSERT INTO artiste (nom) VALUES ("Kendrick Lamar");')     # 2
cd_id = curseur.lastrowid

curseur.execute('INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (' + str(mj_id) + ', "M.I.L.S", 2016);')
curseur.execute('INSERT INTO album (artiste_id, titre, annee_sortie) VALUES (' + str(cd_id) + ', "good kid, d.A.A.m", 2012);')




connexion.commit()
connexion.close()

