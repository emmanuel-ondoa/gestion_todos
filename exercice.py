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
        todos[index]['statut'] = "A fair"  
    print(f"Statut de la tâche '{todos[index]['titre']}' modifié.")

print ("=======MENU PRINCIPAL=======")
print ("1.creer un todo")
print("2.liste des todos")
print("3.modifier le statut d un todo ")
print("4. quitter")
choix = int(input())
while choix != 4:
  if choix==1:
      creer_todos()
      print ("=======MENU PRINCIPAL=======")
      print ("1.creer un todo")
      print("2.liste des todos")
      print("3.modifier le statut d un todo")
      print("4: quitter")
      choix = int(input())
  elif choix==2:
      lister_todos()
      print ("=======MENU PRINCIPAL=======")
      print ("1.creer un todo")
      print("2.liste des todos")
      print("3.modifier le statut d un todo")
      print("4: quitter")
      choix = int(input())
  else:
      modifier_statut_todo()
      print ("=======MENU PRINCIPAL=======")
      print ("1.creer un todo")
      print("2.liste des todos")
      print("3.modifier le statut d un todo")
      print("4: quitter")
      choix = int(input())