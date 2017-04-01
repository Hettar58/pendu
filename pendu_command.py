essais = 5
mot = input("Joueur 1, rentrez un mot\n")
mot_crypt = ""
j2_mot = ""
mot_found = []
lettre_try = []
i = 0
lettre = 0
found = 0
longueur = len(mot)


while longueur != found:
    if found == 0:
        while i <= (longueur - 1):
            mot_crypt = mot_crypt + "-"
            i += 1
    i = 0
    mot_crypt = list(mot_crypt)
    print(mot_crypt)
    print(lettre_try)
    print("entrez une lettre")
    print("essais = ", essais)

    j2_mot = str(input())

    if mot.find(j2_mot) != -1:
        lettre = mot.find(j2_mot)
        lettre_str = mot[lettre]
        del mot_crypt[lettre]
        mot_crypt.insert(lettre, lettre_str)
        i = 0
        
        print("cette lettre est dans ce mot\n\n")
        essais = 5
        found += 1
    else:
        print("cette lettre n'est pas dans le mot")
        lettre_try.append(j2_mot)
        essais -= 1

    if essais == 0:
        quit()

