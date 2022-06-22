n = True
suma = 0
while n :
    print ("dame un numero")
    print ("La suma es ", suma)
    incremento = int(input())
    suma = suma + incremento
    if suma >= 1000:
        print("Hasta luego alcanzaste los 1000")
        n = False