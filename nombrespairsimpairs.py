# Demande à l'utilisateur d'entrer un nombre
n = int(input("Entrez un nombre: "))
if (n % 2) == 0:
   print("{0} est Paire".format(n))#Dit si le nombre est paire
else:
   print("{0} est Impaire".format(n))#Dit si le nombre est impaire
