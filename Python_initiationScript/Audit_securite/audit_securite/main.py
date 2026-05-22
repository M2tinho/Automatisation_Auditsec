"""#le but étant de savoir si le nbr est premier
n=int(input("entrez un nombre"))

def nbr_premier(n):
    nbr_incre=0
    for i in range(2,n-1):
        reste=n%(i)
        if reste==0: 
            nbr_incre+=1 
    if nbr_incre>=1:
        res= f"{n} pas premier"
    else:
        res=f"{n} est premier"
    return res

print(nbr_premier(n))

"""
"""
# but étant de faire une fonction récursive de factoriel
#la fonction factoriel effectue le produit de chaque nombre sauf 0 jusqu'à le nombre entrez en paramètre
# une fonction récursive est composé d'un cas de base et d'un cas où la fonction se rapelle elle même
n=int(input("entrez un nbr entier"))
def factoriel(n):
    #cas de base comme toutes les fonctions récursive
    





print(factoriel(n))
"""

import os
import re
import shutil
from email import policy
from email.parser import BytesParser
import typer

app = typer.Typer()
app=typer.Typer()

@app.command() #permet d'appeler de manière automatiser via terminal tel une commande ?
def afficher_fichier(chemin:str=typer.Argument(...,help="chemin")): 
    #on précise en parametre le type d'argument attendu et on précise que cette argument est obligatoire et on donne une indication a notre user 

    #on créer une liste qui va contenir nos fichiers
    files=[
        name for name in os.listdir(chemin) #énumère les fichier présent dans le chemin passé en parametre donc trie avec les possibles sous dossier
        if os.path.isfile(os.path.join(chemin,name)) #on verifie si c'est bien un fichier ici puis on l'ajoute à la liste 
    ]
    for name in files: #énumère l'ensemble des fichiers dans la liste "fichier" creer au préalable
        print(name) #affiche leurs noms via typer 
    
@app.command() #commande automatiser pour ouvrir un fichier txt

#on va utiliser splitexte pour obtenir type du fichier
#splitexte permet de séparer un fichier en un tuple à partir  
def ouvrir_fichier_txt(chemin: str=typer.Argument(...,help="chemin")):
    txt_files= [
        name for name in os.listdir(chemin)
        if os.path.isfile(os.path.join(chemin,name)) and name.endswith(".txt")
    ]
    for filename in txt_files:
        full_path=os.path.join(chemin,filename) #en concaténant le chemin et le nom du fichier on obtient et on stock le chemin complet
        typer.echo(f"\n {filename}")
        with open(full_path,"r",encoding="utf-8") as f:
           print(f.read())


def quarantine_exe_file(path:str)->None:
    #mets les fichiers .exe dans un dossier quarantaine et enlève les droits d'éxecution de ces fichiers
    quarantine_dir=os.path.join(path,"quarantine")
    os.makedirs(quarantine_dir,exist_ok=True)
    for entry in os.scandir(path):
        if entry.is_file() and entry.name.lower().endswith(".exe"):
            src=entry.path
            dst=os.path.join(quarantine_dir,entry.name)

            shutil.move(src,dst) #cmd qui déplace le fichier 
            current_mode=os.stat(dst).st_mode
            os.chmod(
                dst,
                current_mode & ~(stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH) #on retire en inversant (~) les droits d'excution (X) pour tout le monde après les avoir combiné via le OU
            )




@app.command(name="Scanmail")
def scanmail(path: str = typer.Argument(..., help="Chemin du dossier")):
    mots_suspects = ["urgent", "password", "bank", "winner", "payment", "cliquez ici"]

    dossier_spam = os.path.join(path, "spam")
    os.makedirs(dossier_spam, exist_ok=True)

    fichiers_eml = [
        name for name in os.listdir(path)
        if os.path.isfile(os.path.join(path, name)) and name.lower().endswith(".eml")
    ]

    if not fichiers_eml:
        print("Aucun fichier .eml trouve.")
        return

    for name in fichiers_eml:
        chemin_fichier = os.path.join(path, name)

        with open(chemin_fichier, "rb") as f:
            mail = BytesParser(policy=policy.default).parse(f)

        expediteur = mail.get("From", "").lower()
        contenu = mail.as_string().lower()

        lien_trouve = "http://" in contenu or "https://" in contenu
        mot_suspect = False

        for mot in mots_suspects:
            if mot in contenu:
                mot_suspect = True

        lien_different = False
        liens = re.findall(r"https?://[^\s]+", contenu)

        if "@" in expediteur:
            domaine_expediteur = expediteur.split("@")[-1].replace(">", "").strip()

            for lien in liens:
                if domaine_expediteur not in lien:
                    lien_different = True

        if lien_trouve and (mot_suspect or lien_different):
            shutil.move(chemin_fichier, os.path.join(dossier_spam, name))
            print(f"{name} : spam")
        else:
            print(f"{name} : normal")


if __name__=="__main__":
    app()