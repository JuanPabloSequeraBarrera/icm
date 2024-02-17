import os 
import main as m
def modulregister(estudiantes : list):
    os.system('cls')
    titulo = """
    +++++++++++++++++++++++++++++++++
    +Registro de IMC campers 2024(M)+
    +++++++++++++++++++++++++++++++++
    """
    print (titulo)
    nombre = str(input('Escriba su nombre ').upper())
    edad = int(input('Indique su edad '))
    altura = float(input('Indique su altura en M '))
    peso = int(input('Indique su peso en KG '))
    imc = (peso/altura**2)
    redondeo = round(imc)
    if (redondeo >= 18.5) and (redondeo <= 24.9):
        print(f'Su boody mass index es {redondeo}, tiene valores normales')
    elif (redondeo >= 25) and (redondeo <= 29.9):
        print(f'Su boody mass index es {redondeo}, tiene valores de sobrepeso')
    elif (redondeo >= 30) and (redondeo <= 34.9):
        print(f'Su boody mass index es {redondeo}, tiene valores de obesidad I')
    elif (redondeo >= 35) and (redondeo <= 39.9):
        print(f'Su boody mass index es {redondeo}, tiene valores de obesidad II')
    elif (redondeo > 40):
        print(f'Su boody mass index es {redondeo}, tiene valores de obesidad III')       
    estudiantes.append([nombre,edad,altura,peso,redondeo])
    op = bool (input('Desea registrar otro estudiante? Si(S) No(Enter)'))
    if op == True:
        modulregister()
    else:
        os.system('pause')

