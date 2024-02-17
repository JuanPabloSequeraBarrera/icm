import os
from tabulate import tabulate
def tableR(estudiantes : list):
    estudiantes.sort(key=lambda item :item[4])
    print(tabulate(estudiantes,headers=('Nombre','Edad','Altura','Peso','IMC')))
    os.system('pause')