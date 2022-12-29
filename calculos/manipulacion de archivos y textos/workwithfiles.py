def main():
	item = createFile()
	data = addFile(item)
	print(data)


def createFile(name=input('Type here the name of your file with your extension, example: .txt, .doc, .xls')):
	# 1. hacer una condicional que valíde si el archivo con ese nombre ya existe, en caso falso, continue
	#       el codigo, en caso verdadero arroje mensaje de error y pida cambiar el nombre del archivo.
	# 2. igualmente debera validar que el nombre cumpla con criterios de control como: no usar algunos
	#       caracteres especiales y que siempre tenga una extension, al igual que un mínimo de longitud.
	nameFile = name
	file = open(nameFile, 'w')
	return str(nameFile)


def addFile(nameFile):
	# crear validacion para identificar si el color ya existe, si el dato sministrado es un string
	# y que almacene cada color que se vaya agregando a partir del documento ya creado
	item = input('Type a color:')
	af = open(str(nameFile), 'a')
	af.writelines(item)
	return item


if __name__ == '__main__':
	main()
