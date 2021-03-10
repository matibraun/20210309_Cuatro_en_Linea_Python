filas = input('Por favor ingrese la cantidad de filas: ');
columnas = input('Por favor ingrese la cantidad de columnas: ');

while filas.isnumeric() == False or columnas.isnumeric() == False:
    print ('Los valores ingresados son incorrectos.\n')
    filas = input('Por favor ingrese la cantidad de filas: ');
    columnas = input('Por favor ingrese la cantidad de columnas: ');

print (int(filas))
print (int(columnas))


