from abc import ABC, abstractmethod
from contrasenia import generar_contrasenia

lista_alumnos = []  
lista_profesores = []
lista_curso = ["Laboratorio I", "Ingles I", "Programacion I", "Ingles II","Laboratorio II", "Programacion II"]

class Usuario(ABC):
    def _init_(self, nombre, apellido, email, contrasenia):
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
    def _init_(self, nombre, apellido, email, contrasenia, legajo, anio_inscripcion_carrera):
        super()._init_(nombre, apellido, email, contrasenia)
        self.legajo = legajo 
        self.anio_inscripcion_carrera = anio_inscripcion_carrera
        self.cursos = []
        
    def _str_(self):
        return super().str() + f" \n- Legajo: {self.legajo}"
    
    def matriculacion_en_curso (self, curso):
        self.cursos.append(curso)
        print(f"Estudiante {self.nombre} matriculado en el curso {curso.nombre}")

    def validar_credenciales(self, email, contrasenia):
        super().validar_credenciales(email, contrasenia)
        if email == self.email and contrasenia == self.contrasenia:  
            return True
        else:
            return False


class Profesor(Usuario):
    def _init_(self, nombre, apellido, email, contrasenia, titulo, anio_egreso):
        super()._init_(nombre, apellido, email, contrasenia)
        self.titulo = titulo
        self.anio_egreso = anio_egreso
        self.cursos = []

    def str(self):
        return super().str() + f" \n- Título: {self.titulo}"

    def dictar_curso(self, curso):
        self.cursos.append(curso)
        print(f"Profesor {self.nombre} dictando el curso {curso.nombre}")

    def validar_credenciales(self, email, contrasenia):
        super().validar_credenciales(email, contrasenia)
        if email == self.email and contrasenia == self.contrasenia:
            return True
        else:
            return False


class Curso: 
    def _init_(self, nombre):
        self.nombre = nombre
        self.contrasenia_matriculacion = generar_contrasenia()

    
    def str(self):
        return f"Curso: {self.nombre}"


def submenu_alumno():
    print ("1- Matricularse a un curso")
    print ("2- Ver curso.")
    print ("3- Volver al menu principal.")
    opcion_alumno = int(input("Seleccione una opcion: "))
    return opcion_alumno

def menu_principal ():
    print ("\n---Menu---")
    print ("1- Ingresar como alumno.")
    print ("2- Ingresar como profesor.")
    print ("3- Ver cursos.")
    print ("4- Salir.")  
    print ("")
    opcion = int(input("Seleccione una opcion: "))
    return opcion

def programa_principal():
    opcion = 0

    while opcion != 4:
        opcion = menu_principal()
        if opcion == 1:
            validacion_email = input("Ingrese su email:\n")
            print("")
            validacion_contrasenia = input("Ingrese su contrasenia:\n")
            alumno_encontrado = None
            for alumno in lista_alumnos:
                if alumno.validar_credenciales(validacion_email, validacion_contrasenia):
                    alumno_encontrado = alumno
                    break
            if alumno_encontrado:
                print(f"Bienvenido, {alumno_encontrado.nombre}")
                opcion_alumno = submenu_alumno()
                if opcion_alumno == 1:
                    print("")
                if opcion_alumno == 2:
                    print()
                if opcion_alumno == 3: 
                    programa_principal()
            else:
                print("Credenciales incorrectas o estudiante inexistente, debe darse de alta en alumnado.")

        
        elif opcion == 2:
            validacion_email_profe = input("Ingrese su email:\n")
            print("")
            validacion_contrasenia_profe = input("Ingrese su contrasenia:\n")
            profe_encontrado = None
            for profe in lista_profesores:
                if profe.validar_credenciales(validacion_email_profe, validacion_contrasenia_profe):
                    profe_encontrado = profe
                    break
            if profe_encontrado:
                print(f"Bienvenido, {profe_encontrado.nombre}")
            else:
                print("Credenciales incorrectas o profe inexistente, debe darse de alta en alumnado.")


        elif opcion == 3:
            for i in sorted(lista_curso):
                print("Materia: ", i, "- Carrera: Tecnicatura Universitaria en Programacion")


        elif opcion == 4:
            print("Hasta luego!!")
            break
        else:
            print("Ingrese una opcion correcta! (1-4)")


alumno = Estudiante("Mauro", "Brizio", "mauro@gmail.com", "123", 123, 2023)
lista_alumnos.append(alumno)

profesor = Profesor("Mateo", "Caranta", "mateo@gmail.com", "123", "Licenciado", 1990)
lista_profesores.append(profesor)

programa_principal()