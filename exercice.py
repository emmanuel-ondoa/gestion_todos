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

print ("=======MENU PRINCIPAL=======")
print ("1.creer un todo")
print("2.liste des todos")  
print("3: quitter") 
choix = int(input()) 
while choix != 3:
  if choix==1:
      creer_todos()
      print ("=======MENU PRINCIPAL=======")
      print ("1.creer un todo")
      print("2.liste des todos")  
      print("3: quitter") 
      choix = int(input())
  else:
      lister_todos()
      print ("=======MENU PRINCIPAL=======")
      print ("1.creer un todo")
      print("2.liste des todos")  
      print("3: quitter")
      choix = int(input()) 