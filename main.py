class Program:
    estudiantes={}
    opcion=0
    while opcion!=4:
        print("""1. Registrar Estudiante: 
           2. Mostrar todos los estudiantes por sus cursos:
           3. Buscar estudiante por carnet:
           4. Salir""")
        opcion=int(input("Seleccione una opcion: "))
        try:
            if opcion==1:
                carnet=input("Ingrese el numero de carnet")
                nombre= input("Ingrese el nombre del estudiante: ")
                edad=int(input("Ingrese la edad: "))
                carrera=input("Ingrese la carrera: ")
                cantCursos=int(input("Ingrese la cantidad de cursos: "))
                for i in range(cantCursos):
                    curso=input("Ingrese el nombre del curso: ")




        except :
            print("Ocurrio un error, intente de nuevo...")
##xd