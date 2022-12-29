peso = int(input('Por favor, indíquenos su peso en kg: '))
estatura = float(input('Por favor, indíquenos  su estatura en mts: '))
IMC = float(peso / estatura ** 2)

print('Tu índice de masa corporal (IMC) es: ' + str(round(IMC, 2)))
