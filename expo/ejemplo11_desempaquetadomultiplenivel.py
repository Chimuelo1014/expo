datos = [("A",(1,2,3)),("B",(4,5,6)),("C",(7,8,9))]
for letra, (a,b,c) in datos:
    print("La letra es", letra)
    print("Los valores son", a, b, c)
    #Desempaquetado automatico
    # asigna automaticamente a 
    # letra y (a,b,c)
    # En este caso, la variable letra recibe el primer elemento de la tupla y la variable