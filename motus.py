import random
import  json
import unicodedata

'''
liste="le la le tset test autres."
dictionnaire={}
a=0
mots=""

for i in range(len(liste)):
    if liste[i] != " " and liste[i] != ";" and liste[i] != ".":
        mots+=liste[i]
    else:
        dictionnaire.update({mots:a})
        mots=""
    a+=1

for i in dictionnaire:
    print(dictionnaire[i])
'''

liste_mots=[]
f=open("C:\\Users\Formation\python\motus_game\Mots.json","r" ,encoding="utf-8-sig")
file=json.load(f)
def strip_accents(s):
   return ''.join(c for c in unicodedata.normalize('NFD', s)
                  if unicodedata.category(c) != 'Mn')


for i in file["test"]:
    if i["type"]=="subst." or i["type"]=="adj." or i["type"]=="verbe":
        liste_mots.append(strip_accents(i["label"]))

relance=True
while relance==True:
    selec_mot=random.randint(0,len(liste_mots))
    mot=liste_mots[selec_mot]
    tiret=""
    gagne=False
    tirets=[]
    for i in range(len(mot)):
        tirets.append("_")
        tiret+="_"
    while gagne==False:
        print(tiret)
        print(f"entrez un mot de longueur {len(mot)}")
        mot_user=input()
        compteur_ok=0
        compteur_dans_mot=0
        compteur_faux=0
        for i in range(len(mot)):
            if mot_user=="cheat":
                print(mot)
            if len(mot_user)<len(mot):
                print("mot trop court")
                break
            elif len(mot_user)>len(mot):
                print("mot trop long")
                break

            if  mot_user[i] in mot and mot[i]==mot_user[i]:
                compteur_ok+=1
                tirets[i]=mot[i]
                tiret=""
                for i in range(len(tirets)):
                    tiret+=tirets[i]
                    #tiret=tiret.replace(tiret[mot.index(mot[i])][2], mot_user[i],mot.count(mot_user[i]))
                    #tiret = tiret[:i] + mot_user[i] + tiret[i+1:]
            elif mot_user[i] in mot:
                compteur_dans_mot+=1
            else:
                compteur_faux+=1
        print(tiret)
        print(f"il y'a {compteur_ok} lettre(s) qui sont bien placée(s) et dans le mot")
        print(f"il y'a {compteur_dans_mot} lettre(s) qui sont dans le mot")
        print(f"il y'a {compteur_faux} lettre(s) qui ne sont pas dans le mot")
        if compteur_ok==len(mot):
            print("trouver")
            print("rejouer? oui/non")
            rejouer=input()
            if rejouer=="oui":
                relance=True
            elif(rejouer=="non"):
                relance=False
            gagne=True