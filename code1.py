#coding:UTF-8

# print("junior de \" damso\" code avec python")
# print("junior le best\nplayer nin\nthe whord")
# print("junior",'"best"',"#DRPIEFT#")
# print("Bonjour", "tout", "le", "monde", sep="_")
# print("Bonjour", "tout", "le", "monde", end="!", sep='_')
"""
fonction vue print()                    -> Affiche a l'ecrant
             input()                    -> lire au clavier
             type()                     ->  retourne le type d'une donnee,variables,ect...
             str.format()               -> formater une chaine
             int(),srt(),bool(),float() -> "caster" convertire une donner d'un type a l'autre

             boucle =>              while
                                    for
            mot clet =>             break qui permet de quiter la boucle
                                    continue : qui permet de reentrer dans la boucle                        


"""

# AgePersone=14
# Agepersone2="25"
# print(type(AgePersone))
# print(type(Agepersone2))

# agepersone=14
# prixht=15000
# text=" l'age de la personne est {} et le prix hors taxe est {}$"
# print(text.format(agepersone,prixht))

# NamePlayer=input(" Enter the Name of Player")
# print("Wlecome sir",NamePlayer)


# n=input("entrer votre age")
# p=input("enter the http tarifs")
# print("Vous avez {} et le prix hht est a {}".format(n,p))

# n=True
# n=int(n)
# print(n)

# duxieme facon de faire

# print("enter your name")
# nn=input()
# print(nn)

# input("entrer votre premier nombre")

# n1=input()
# n1=float(n1)  
# input("entrer votre deuxieme nombre")
# n2=input()
# n2=float(n2) 
# calcule=n1/n2
# r=float(n1%n2)
# calcule=float(calcule)
# print("le resultat du calcule est:{} et a pour reste:{}".format(calcule,r))

# condition ifb
# name="junior"
# user_id="junior123"
# print('interface de connection')
# newuser=input('enttrer votre nom')
# newid=input('enttrer votre identifiant')

# if((name ==newuser) and(newid== user_id)):
#     print("connection reusi")
# else:
#     print("impossible de vous connecter")
# if('j' in newuser):
#     print("votre nom contien la lettre j")
# else:
#     print("votre nom ne contien pas de j")    

# JEUX DE DEVINETTE A BIEN RETRAVAILLER

# print("JEUX DE DEVINETTE")
# mot_adeviner="he"
# user_tentative=input("essayer de deviner le mot et pour indice le mot est former de deux lettre :")
# if(user_tentative !=mot_adeviner):
#     if('h' in user_tentative):
#         print('il y a la lettre h dans votre reponse et elle est egalement dans le mot a deviner a vous de trouver la bonne position')
#         if('e' in user_tentative):
#             print("il y a la lettre e dans votre reponse et elle est egalement dans le mot a deviner a vous de trouver la bonne position")
#         else:
#             print ('heurer')

#Boucle
## while
# jeulance=True
# print("")
# while (jeulance):
#     choix=input(">")
#     if(choix=="again"):
#         continue
#     elif(choix=="quit"):
#         break
#     else:
#         print("Commande introuvable")
    
# print("jeux quitter")  

# ## For lui il affiche par secence
# phrase="Hello whord"
# for lettre in phrase:
#     print(lettre)

##### JEUX#### 
# print("jeux de devinette")
# debujeux=True
# mot_deviner="junior"
# ajout="azertyuiopqsdfghjklmwxcvbn"
# x=0

# while(debujeux):
#      print("essayer de deviner LE MOT MAGIQUE")
#      mot=input(">")
#      if(mot==mot_deviner):
#          print("waouuu vous avez trouver")
#          print("")
#          print("Voulez vous jouer encore")
#          contnue=input(">")
#          if((contnue =="oui") or (contnue=="yes")or(contnue=="OUI") or (contnue=="YES")):
#              mot_deviner="junior"+ajout[x]
#              x+=1  
#              continue
#          elif((contnue=="non") or (contnue=="NON")or(contnue=="no") or (contnue=="NO")):
#              break
#          else:
#              print("cette comande n'est pas reconnue par le systheme")
#              continue
#      else:
#          print("mauvaise reponse")
#          print("")
#          print("voulez vous reesayer ")
#          print("")
#          necon=input(">")   
#          if((necon=="oui") or (necon=="yes")or(necon=="OUI") or (necon=="YES")):
#              continue
#          elif((necon=="non") or (necon=="NON")or(necon=="no") or (necon=="NO")):
#              break
#          else:
#              print("cette comande n'est pas reconnue par le systheme")
#              continue


### TEXTE #### 

print("jeux de devinette")
debujeux=True
mot_deviner="junior"
ajout="azertyuiopqsdfghjklmwxcvbn"
x=0

while(debujeux):
     print("essayer de deviner LE MOT MAGIQUE")
     mot=input(">")
     if(mot==mot_deviner):
         print("waouuu vous avez trouver")
         print("")
         print("Voulez vous jouer encore")
         contnue=input(">")
         if((contnue =="oui") or (contnue=="yes")or(contnue=="OUI") or (contnue=="YES")):
             mot_deviner="junior"+ajout[x]
             x+=1  
             continue
         elif((contnue=="non") or (contnue=="NON")or(contnue=="no") or (contnue=="NO")):
             break
         else:
             print("cette comande n'est pas reconnue par le systheme")
             continue
     else:
         print("mauvaise reponse")
         print("")
         print("voulez vous reesayer ou voulez vous un indice taper r pour reesayer et i pour indice et n pour sortire  ")
         print("")
         necon=input(">")   
         if((necon=="i") or (necon=="indice")):
             
             continue
         elif((necon=="non") or (necon=="NON")or(necon=="no") or (necon=="NO")):
             break
         else:
             print("cette comande n'est pas reconnue par le systheme")
             continue


print("Merci d'avoire jouer a bientot")        




    
    

    

