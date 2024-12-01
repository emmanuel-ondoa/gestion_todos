todos= []

def creer_todos () :
    titre =input("inserer le nom de la tache :")
    todos.append ({"titre": titre ,"statut" : "A faire"})
    print (" la tache",titre ," ajouter avec succes")


def lister_todos() :
        if  not  todos:
          print("aucune tache disponible ")
        else:
         for index , todo  in enumerate(todos) :
            index=index+1
            print (f"{index}.{todo['titre']}-{todo['statut']}")

def modifier_statut_todo():
    lister_todos()
    index = int(input("Entrez le numéro de la tâche à modifier : ")) - 1
    if todos[index]['statut'] == "A faire":
        todos[index]['statut'] = "Fait"
    else:
        todos[index]['statut'] = "A faire" 
    print(f"Statut de la tâche '{todos[index]['titre']}' modifié.")

def supprimer_todo():
    lister_todos()
    index = int(input("Entrez le numéro de la tâche à supprimer : ")) - 1
    confirmation = input(f"Confirmez-vous la suppression de '{todos[index]['titre']}' ? (o/n) : ")
    if confirmation.lower() == 'o':
        del todos[index]
        print("Tâche supprimée avec succès.")
    else:
        print("Suppression annulée.")

        

choix = ''
while choix != 'q':
    print('\n==== Menu principal ====')
    print('1: Lister les todos')
    print('2: Créer un todo')
    print('3:modifier le statut d un todo ')
    print ('4:supprimer un todo')
    print('q: Quitter')
    choix = input('=> Choix : ')
    match choix:
        case '1': lister_todos()
        case '2': creer_todos()
        case '3' : modifier_statut_todo()
        case '4': supprimer_todo()
        case 'q': print('Au revoir')
        case _: print('Choix invalide')
