import os 
import modulos.menu as m
import modulos.registro as r
import modulos.registrotab as t
import modulos.reportes as p

if __name__ == '__main__':
    estudiantes = []
    isActive = True
    while isActive:
        os.system('cls')
        options = m.menu()
        if (options == 1):
            r.modulregister(estudiantes)
        elif (options == 2):
            p.menreport(estudiantes)
        elif (options == 3):
            t.tableR(estudiantes)
        elif (options == 4):
            isActive = False
            print('Gracias por usar el software')
            os.system('pause')

