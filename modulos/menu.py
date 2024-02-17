import os
listop = [1,2,3,4]
def menu():
    os.system('cls')
    titulo = """
    +++++++++++++++++++++++++++++++++
    +SOFTWARE CENTRO DE SALUD CAMPUS+
    +++++++++++++++++++++++++++++++++
    """
    opciones = ('1.Registro de estudiantes\n2.Reportes\n3.Tabla\n4.Salir')
    print(titulo)
    try:
        print(opciones)
        op = int (input(':)_ '))
        if not (op in listop):
            print('Opcion invalida')
            os.system('Pause')
            menu()
    except ValueError:
        print('Error en la digitacion')
        os.system('pause')
        menu()
    return(op)