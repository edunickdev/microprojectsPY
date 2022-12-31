# este codigo podría mejorar mucho mas, agregando una función que recorra la lista al final y guarde cada elemento
# en un archivo txt y de esta manera darle persistencia a este programa.
# tambien podria subdivirse en funciones para que el codigo sea mas organizado y claro.

lista = []
elemento = input('Digite el elemento de la lista que desea agregar: ').capitalize()
lista.append(elemento)
masElementos = input('¿desea agregar mas datos a la lista? S/N: ').lower()

while masElementos == 's':
    elemento = input('Digite el elemento de la lista que desea agregar: ')
    lista.append(elemento)
    masElementos = input('¿desea agregar mas datos a la lista? S/N: ').lower()
else:
    print(lista)
    exit()
