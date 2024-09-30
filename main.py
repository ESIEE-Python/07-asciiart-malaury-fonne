"""Fonction qui permet d'encoder une chaine de charactere"""
#### Imports et définition des variables globales
import sys
sys.setrecursionlimit(10000)

#### Fonctions secondaires


def artcode_i(s:str):
    """retourne la liste de tuples encodant
     une chaîne de caractères passée en argument 
     selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici
    l=[]
    n=1
    if len(s)==1:
        l.append((s[0],1))
        return l
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            n=n+1
        else:
            if i == len(s)-1:
                l.append((s[i-1],n))
                l.append((s[i],1))
            else:
                l.append((s[i-1],n))
            n=1
    if n>1:
        l.append((s[len(s)-1],n))
    return l


def artcode_r(s):
    """retourne la liste de tuples encodant une chaîne 
    de caractères passée en argument selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    # votre code ici

    # cas de base
    # recherche nombre de caractères identiques au premier
    # appel récursif
    l=[]
    n=1
    if len(s)==1:
        l.append((s[0],1))
        return l
    while n < len(s) and s[0]==s[n]:
        n=n+1
    l.append((s[0],n))
    if n==len(s) and s[0]==s[n-1]:
        return l
    return l+artcode_r(s[n:])

#### Fonction principale


def main():
    """Execute et affiche pour des valeurs tests"""
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('MMMMaaacXolloMM'))
    print(artcode_i('vbhibeiRRRRttt   UUUUU'))
    print(artcode_r('vbhibeiRRRRttt   UUUUU'))

if __name__ == "__main__":
    main()
