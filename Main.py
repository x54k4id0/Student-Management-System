def rechercheparnom(n):
    import sqlite3 as sql
    cnx=sql.connect('data.sqlite')
    cr=cnx.execute('select * from etudiants where nom_etu ="{}"'.format(n))
    for k in cr :
        print('Num : ',k[0],'Nom : ',k[1],'DateNaiss : ',k[2],'Sexe : ',k[3],sep='  ')

def allstudent():
    import sqlite3 as sql
    cnx=sql.connect('data.sqlite')
    cr=cnx.execute(f'select * from etudiants')
    for k in cr :
         print('Num : ',k[0],'Nom : ',k[1],'DateNaiss : ',k[2],'Sexe : ',k[3],sep='  ')

def allteacher():
    import sqlite3 as sql
    cnx=sql.connect('data.sqlite')
    cr=cnx.execute(f'select * from enseignants')
    for k in cr :
        print('Num :',k[0],'Nom :',k[1],'Grade :',k[2],'Anciennte :',k[3],sep='  ')
        
def moyen(n):
    import sqlite3 as sql
    cnx=sql.connect('data.sqlite')
    cr=cnx.execute('select nom_etu , sum(note*coef)/sum(coef) from etudiants join notes on _num_etu=num_etu join matieres on _num_mat=num_mat where nom_etu="{}" group by nom_etu'.format(n))
    for k in cr :
        print('la moyenne coefficientée est:',k[1])

def relevernote(n):
    import sqlite3 as sql
    cnx=sql.connect('data.sqlite')
    cr=cnx.execute('select num_mat , nom_mat , coef , note from etudiants join notes on _num_etu=num_etu join matieres on _num_mat=num_mat where nom_etu ="{}"'.format(n))
    print('')
    for k in cr :
        print('Num_mat : ',k[0],'Mat : ',k[1],'Coef : ',k[2],'Note : ',k[3],sep='  ')
        print('')
    return moyen(n)

def addstudent(nom,datenaiss,sexe):
    import sqlite3 as sql
    cnx=sql.connect('data.sqlite')
    cr=cnx.execute("insert into etudiants(nom_etu,date_naiss,sexe) values ('{}','{}','{}')".format(nom,datenaiss,sexe))
    cnx.commit()

def addteacher(nom,grade,anciennete):
    import sqlite3 as sql
    cnx=sql.connect('data.sqlite')
    cr=cnx.execute("insert into enseignants(nom_ens,grade,anciennete) values ('{}',{},{})".format(nom,grade,anciennete))
    cnx.commit()

def tri():
    import sqlite3 as sql
    cnx=sql.connect('data.sqlite')
    cr=cnx.execute('select nom_etu from etudiants join notes on _num_etu=num_etu join matieres on _num_mat=num_mat group by nom_etu order by sum(note*coef)/sum(coef) desc')
    for k in cr :
        print(k[0])

def menu():
    choix=input('Entrer le numero de la fonction\n A pour la recherche par nom \n B pour voir tous les etudiants \n C pour voir tous les enseignants \n D pour calculer la moyenne generale \n E pour generer un relever de note \n F pour ajouter un etudiant au base de donnees \n G pour ajouter un enseignant au base de donnees \n H pour trier les etudiants par ordre de merite\n')
    if choix=='A':
        n=input('Entrer le nom\n')
        return rechercheparnom(n)
    elif choix=='B':
        return allstudent()
    elif choix=='C':
        return allteacher()
    elif choix=='D':
        n=input('Entrer le nom\n')
        moyen(n)
    elif choix=='E':
        n=input('Entrer le nom\n')
        relevernote(n)
    elif choix=='F':
        n=input('Entrer le nom \n')
        d=input('Entrer la date de naissance\n')
        s=input('Entrer le sexe\n')
        return addstudent(n,d,s)
    elif choix=='G':
        n=input('Entrer le nom\n')
        g=int(input('Entrer le grade\n'))
        a=int(input("Entrer l'anciennete\n"))
        return addteacher(n,g,a)
    elif choix=='H':
        return tri()

# Abdessamad KERROU