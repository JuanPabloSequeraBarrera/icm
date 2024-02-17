import os
import main as x
def menreport(estudiantes:list):
    isWorking = True
    os.system('cls')
    lstop =['A','B','C','D','E','F']
    titulo = """
    ++++++++++++++++++++++++++++++++++++++++++++++
    +REPORTES GENERALES DE BALANCE DE ESTUDIANTES+   
    ++++++++++++++++++++++++++++++++++++++++++++++
    
    """
    opciones =('A.Peso ideal\nB.Sobrepeso\nC.Obesidad I\nD.ObesidadII\nE.ObesidadIII\nF.Salir')
    print(titulo)
    print(opciones)
    while isWorking:
        op =input(':)_ ').upper()
        if (op in lstop):
            if(op =='A'):
                idealweight(estudiantes)
            elif(op == 'B'):
                overweight(estudiantes)
            elif(op == 'C'):
                obesityweight(estudiantes)
            elif(op == 'D'):
                obesityiiweight(estudiantes)
            elif(op == 'E'):
                obesityiiiweight(estudiantes)
            elif(op == 'F'):
                isWorking = False
def idealweight(estudiantes: list):
    for i, item in enumerate(estudiantes):
        for j in range(int(i+1),len(estudiantes),1):
            if (estudiantes[i][4]>= 18.5) and (estudiantes[i][4]<=24.9):
                aux = estudiantes[i]
                estudiantes[i]= estudiantes[j]  
                estudiantes[j] = aux
            normalw = estudiantes[i][1]
            print(f'Los esutidantes con peso ideal {normalw} ')
            break
def overweight(estudiantes:list):
    for i, item in enumerate(estudiantes):
        for j in range(int(i+1),len(estudiantes),1):
            if (estudiantes[i][4]>= 25) and (estudiantes[i][4]<=29.9):
                aux = estudiantes[i]
                estudiantes[i]= estudiantes[j]  
                estudiantes[j] = aux
            normalw = estudiantes[i][1]
            print(f'Los esutidantes con sobrepeso son {normalw} ')
            break
def obesityweight(estudiantes:list):
    for i, item in enumerate(estudiantes):
        for j in range(int(i+1),len(estudiantes),1):
            if (estudiantes[i][4]>= 30) and (estudiantes[i][4]<=34.9):
                aux = estudiantes[i]
                estudiantes[i]= estudiantes[j]  
                estudiantes[j] = aux
            normalw = estudiantes[i][1]
            print(f'Los esutidantes con obesidad I son {normalw} ')
            break
def obesityiiweight(estudiantes:list):
    for i, item in enumerate(estudiantes):
        for j in range(int(i+1),len(estudiantes),1):
            if (estudiantes[i][4]>= 35) and (estudiantes[i][4]<=39.9):
                aux = estudiantes[i]
                estudiantes[i]= estudiantes[j]  
                estudiantes[j] = aux
            normalw = estudiantes[i][1]
            print(f'Los esutidantes con sobrepeso II son {normalw} ')
            break
def obesityiiiweight(estudiantes:list):
    for i, item in enumerate(estudiantes):
        for j in range(int(i+1),len(estudiantes),1):
            if (estudiantes[i][4]>40):
                aux = estudiantes[i]
                estudiantes[i]= estudiantes[j]  
                estudiantes[j] = aux
            normalw = estudiantes[i][1]
            print(f'Los esutidantes con sobrepeso III son {normalw} ')
            break
