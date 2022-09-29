for nombre in range (1, 1000000): #Pour la variable nombre comprus entre 1 et 100000
    count = 0 #On initialise la var count à zero
    for i in range(2, (nombre//2 + 1)):
        if(nombre % i == 0): #Si le reste de la division de nombre et i et 0
            count = count + 1 #la variable count est maintenant égale à sa valeur initiale + 1
            break

    if (count == 0 and nombre != 1):#Si la valeur de count est 0 et la valeur de nombre est different de 1 
        print(" %d" %nombre, end = '  ')#Affiche les nombres premiers
