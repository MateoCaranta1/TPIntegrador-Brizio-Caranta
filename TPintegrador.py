from abc import ABC, abstractmethod
from contrasenia import generar_contrasenia

class Usuario(ABC):
    def __init__(self, nombre, apellido, email, contrasenia):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contrasenia = contrasenia

    def str(self):
        return f"Nombre: {self.nombre} Apellido: {self.apellido}\n- Email: {self.email}"

    @abstractmethod
    def validar_credenciales(self, email, contrasenia):
        pass

class Estudiante(Usuario): 
    def __init__(self, nombre, apellido, email, contrasenia, legajo, anio_inscripcion_carrera):
        super().__init__(nombre, apellido, email, contrasenia)
        self.legajo = legajo 
        self.anio_inscripcion_carrera = anio_inscripcion_carrera
        self.cursos = []
        
    def __str__(self):
        return super().str() + f" \n- Legajo: {self.legajo}"
    
    def matriculacion_en_curso (self, curso):
        self.cursos.append(curso)
        print(f"Estudiante {self.nombre} matriculado en el curso {curso.nombre}")

class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, titulo, anio_egreso):
        super().__init__(nombre, apellido, email, contrasenia)
        self.titulo = titulo
        self.anio_egreso = anio_egreso
        self.cursos = []

    def __str__(self):
        return super().str() + f" \n- Título: {self.titulo}"

    def dictar_curso(self, curso):
        self.cursos.append(curso)
        print(f"Profesor {self.nombre} dictando el curso {curso.nombre}")

class Curso: 
    def init(self, nombre):
        self.nombre = nombre
        self.contrasenia_matriculacion = generar_contrasenia()

    def str(self):
        return f"Curso: {self.nombre}"
    

def menu_principal (self):
    print ("---Menu---")
    print ("1- Ingresar como alumno.")
    print ("2- Ingresar como profesor.")
    print ("3- Ver cursos.")
    print ("4- Salir.")  
    opcion = int(input())
    return opcion

def programa_principal ():
    opcion = 0 
    while opcion != 4:
        opcion == menu_principal()
        if opcion == 1:
            email = input("Ingrese su email:\n")
            contrasenia = input("Ingrese su contrasenia:\n")
            alumno = Estudiante(email, contrasenia)
            Estudiante.cursos(alumno)
        elif opcion == 2:
            print("")
        elif opcion == 3:
            print("")
        elif opcion == 4:
            print("Hasta luego!!")
            break
        else:
            print("Ingrese una opcion correcta! (1-4)")

        
        
