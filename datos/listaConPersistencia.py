import os.path

# requiere mas ampliacion de utilidad y validaciones o facilidades, como crear una lista de los archivos
# ya existentes y que a traves un
# menu el usuario pueda elegir el archivo que desea utilizar, igualmente requiere de un bucle que mantenga al usuario
# dentro del programa, mientras este no decida salirse al terminar de agregar elementos a la lista.

nombreArchivo = input('Escriba el nombre de la lista que desea crear: ') + '.txt'
item = input('Escriba el nombre del elemento de la lista que quiere agregar: ').capitalize()


def inicio(data=nombreArchivo):
    archivo = open(f'{data}', 'w')
    archivo.close()


def agregar(data=nombreArchivo, rsc=item):
    archivo = open(f'{data}', 'a')
    archivo.write(f'{rsc}' + ', ')
    archivo.close()


def cargar(data=nombreArchivo):
    paises = []
    archivo = open(f'{data}', 'r')
    for linea in archivo:
        paises = linea.split(',')
    archivo.close()
    print(sorted(set(paises)))
    return paises


if os.path.isfile(f'{nombreArchivo}'):
    confirm = input('El archivo que mencionas ya existe, quieres pasar a cargar datos? S/N: ')
    if confirm.lower() == 's':
        agregar()
        cargar()
    else:
        exit()
else:
    print(f'Se creo el archivo {nombreArchivo}, a continuación agregaremos el elemento indicado a la lista')
    inicio()
    agregar()
    cargar()
