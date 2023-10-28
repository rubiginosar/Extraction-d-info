from bs4 import BeautifulSoup as bs 
import sqlite3

posologies = []
with open('corpus-medical_snt/concord.html', 'r') as concord:
    text = concord.read()
    soup = bs(text, 'html.parser')
    for tr in soup.find_all('tr'):
        posologies.append(tr.find('a').get_text())

# Creer la connexion 
con = sqlite3.connect('extraction.db')

# Creer le curseur 
cur = con.cursor()

# creer la table
cur.execute('''CREATE TABLE EXTRACTION
               (id integer primary key, posologie text)''')

# inserer les lignes d'info a partir de concord.html
i = 1
for posologie in posologies:
    cur.execute("INSERT INTO EXTRACTION VALUES ('%d','%s')" %(i, posologie))
    print("%4d | %s" %(i, posologie))
    i += 1

# enregistrer les modifications
con.commit()
#on peut aussi fermer la connexion quand on termine mais on doit d'abord sauvgarder les modifs
con.close()
