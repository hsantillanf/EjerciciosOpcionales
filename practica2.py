elemento=[]

def separarL(lista):
    n = int(input("Cuantos valores desea agregar: "))
    for i in range(n):
        no = int(input("Valor: "))
        elemento.append(no)
        i+=1
        print(elemento)
    lista.sort()
    pares= []
    impares=[]
    for i in lista:
        if i % 2 ==0:
            pares.append(i)
        else:
            impares.append(i)
    return pares, impares

pares,impares= separarL(elemento)
print("Los números pares son: ",pares)
print("Los números impares son: ",impares)

if __name__ == "__main__":
    separarL(elemento)
