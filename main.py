
# on va demander à l'utilisateur de faire un choix entre voir la liste de courses, supprimer un élément et ajouter un élément ainsi que vider la liste ou la fermer
# on va vérifier si il a choisi 1 et s'il a choisi 1, on va print la liste de courses
# on va vérifier s'il a choisi 2 et si il a choisi 2, on va demander quel élément supprimer
# on va vérifier s'il a choisi 3 et si il a choisi 3, on va demander quel élément ajouter
# on va vérifier s'il a choisi 4 et si il a choisi 4, on va vider la liste avec .clear
# on va vérifier s'il a choisi 5 et si il a choisi 5, on va dire au revoir et on va break
# si aucune des conditions respectés, on demande de rechoisir
import time
import sys
liste_de_course = []
while True:
    choix = int(input("Bienvenue dans votre liste de course. Merci de choisir parmi les 5 options suivantes laquelle voulez-vous exécuter :\n 1 : Afficher la liste de course\n 2 : Supprimer un élément de la liste de course\n 3 : Ajouter un élément à la liste de course\n 4 : Vider les éléments de la liste de courses\n 5 : Quitter le programme\n Votre choix : "))
    if choix < 1 or choix > 5:
        print("Veuillez choisir un nombre valide !")
        time.sleep(3)
    else:
        if choix == 1:
            print(f"Voici la liste : {liste_de_course}")
            time.sleep(5)
        elif choix == 2:
            retirer = input("Quel élément souhaitez-vous retirer : ")
            if retirer in liste_de_course:
                liste_de_course.remove(retirer)
                print("L'élément a bien été retiré")
                time.sleep(2)
            else:
                print(f"L'élément {retirer} n'est actuellement pas dans la liste")
        elif choix == 3:
            liste_de_course.append(input("Quel élément souhaitez-vous ajouter : "))
            print("L'élément a bien été ajouté")
            time.sleep(2)
        elif choix == 4:
            supp = input("Êtes-vous sûr de vouloir réinitialiser la liste : o/n ")
            if supp == "o":
                liste_de_course.clear()
                print("La liste de course a bien été réinitialisée")
                time.sleep(5)
            elif supp == "n":
                print("Ouf, j'ai eu peur")
                time.sleep(2)
            else:
                print("Merci de retourner une réponse valide")
                time.sleep(2)
        elif choix == 5:
            print("Fermeture du programme en cours")
            time.sleep(3)
            print("Le programme est fermé")
            sys.exit()
