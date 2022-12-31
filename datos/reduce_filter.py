# generando la lista

start = int(input('Digite el número desde el cual quiere que inicie la lista: '))
end = int(input('Digite el número hasta donde quiere que llegue la lista: '))


def createList(contador=start, finalNum=end):
    lista = []
    while contador <= finalNum:
        lista.append(contador)
        contador += 1
    print('la lista que se creo contiene los siguientes elementos: ' + str(lista))
    return lista


print('los elementos que cumplen la condición son: ' + str(list(filter(lambda numeros_par: numeros_par % 2 == 0, createList()))))
