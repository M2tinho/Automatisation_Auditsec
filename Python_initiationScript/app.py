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

import os #module qui nous permets d'avoir accès a notre systeme d'exploitation et donc d'une certaine manière les fonctions qui vont être exploiter vont fonctionner de la même manière que le terminal cmd
import typer #module qui nous permettra de passer une commande avec un argument

app=typer.Typer()

@app.command() #permet d'appeler de manière automatiser via terminal tel une commande ?
def list_fichiers(doc:str):
    fichiers=os.listdir(doc) #ici via le module os on va lister (creer une liste) l'ensemble des dossiers présent dans le doc via la précision du chemin
    for fichier in fichiers:
        print(fichier) #on énumère chaque fichier de présent dans la liste de fichier présent dans le dossier selon notre chemin précédement construit

@app.command() #commande automatiser pour ouvrir un fichier txt

#on va utiliser splitexte pour obtenir type du fichier
#splitexte permet de séparer un fichier en un tuple à partir  
def ouvrir_fichier(nom_fichier: str):
    nom,terminaison=os.path.splitext(nom_fichier)

    if terminaison != "txt":
        return
    else:
        with open(nom_fichier) as f:
            contenu=f.read()
            print(contenu)
    return

if __name__=="__main__":
    app()