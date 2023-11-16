#Exercice 1: 

partie1 = {
    'Sir_chapeau': ('chateau', 20, 12),
    'Hetre_dit_mot': ('forêt', 16, 13),
    'Ratopnu': ('grotte', 12, 2),
    'Trop_dit_glau': ('grotte', 9, 3)
}

partie2 = {
    'Sir_chapeau': ('chateau', 6, 3),
    'Hetre_dit_mot': ('forêt', 7, 6),
    'Ratopnu': ('grotte', 11, 6),
    'Trop_dit_glau': ('grotte', 14, 5),
    'Elfe_lest': ('chateau', 3, 1)
}

def meilleur_adversaire(dic):
    adversaire = []
    
    # Calcul des résultats et stockage dans la liste adversaire
    for i in dic.keys():
        combat, victoire = dic[i][1], dic[i][2]
        resultat = combat - victoire
        adversaire.append(resultat)
    
    # Recherche du maximum dans la liste
    max_resultat = max(adversaire)
    
    # Recherche des adversaires ayant le résultat maximum
    meilleurs_adversaires = [cle for cle, valeur in dic.items() if valeur[1] - valeur[2] == max_resultat]
    
    return max_resultat, meilleurs_adversaires

# Test avec partie1
resultat_max, adversaires_max = meilleur_adversaire(partie1)
print("Le meilleur adversaires (partie1) est :", adversaires_max, "avec", resultat_max, "victoire pour lui !")

# Test avec partie2
resultat_max, adversaires_max = meilleur_adversaire(partie2)
print("Le meilleur adversaires (partie2) est :", adversaires_max, "avec", resultat_max, "victoire pour lui !")

#----------------------------------------------------------------

#Exercice 2 : 

class Noeud():
    """
    Implémentation d'un arbre binaire
    """

    def __init__(self, valeur):
        """
        Constructeur :
        valeur est une chaîne de caractères ou un nombre entier.
        """
        self.valeur = valeur
        self.gauche = None
        self.droit = None

    def cree_fils_gauche(self, fils_gauche):
        """
        fils_gauche est une chaîne de caractères ou un nombre entier qui sera rajouté comme fils gauche au noeud de
        l'arbre binaire sur lequel s'applique cette méthode.
        La valeur de ce fils rajouté est renvoyée par la méthode.
        """
        self.gauche = Noeud(fils_gauche)
        return self.gauche

    def cree_fils_droit(self, fils_droit):
        """
        fils_droit est une chaîne de caractères ou un nombre entier qui sera rajouté comme fils droit au noeud de
        l'arbre binaire sur lequel s'applique cette méthode.
        La valeur de ce fils rajouté est renvoyée par la méthode.
        """
        self.droit = Noeud(fils_droit)
        return self.droit

    def est_feuille(self):
        """
        méthode renvoyant True si le noeud sur lequel s'applique la méthode est une feuille de l'arbre et False sinon.
        """
        return self.gauche is None and self.droit is None
    
# Création d'un nœud
arbre = Noeud("A")

# Création de fils gauche et droit
fils_gauche = arbre.cree_fils_gauche("B")
fils_droit = arbre.cree_fils_droit("D")
arbre.cree_fils_droit("C")

# Vérification si le nœud est une feuille
print(arbre.est_feuille())  # False
print(fils_droit.est_feuille())  # True
print(arbre.gauche.valeur) #B