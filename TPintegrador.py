from abc import ABC, abstractmethod
from contrasenia import generar_contrasenia

#AGREGAR QUE LAS CLASES SEAN PUBLICAS Y PRIVADAS.

#- DECLARACION DE VARIABLES GLOBALES
lista_alumnos = []  
lista_profesores = []
mis_cursos = {}

#----INICIO DECLARACION DE CLASES ------------------------------------
class Usuario(ABC):
    def __init__(self, nombre, apellido, email, contrasenia):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia

    def __str__(self):
        return f"Nombre: {self._nombre} Apellido: {self._apellido}\n- Email: {self._email}"

    @abstractmethod
    def validar_credenciales(self, email, contrasenia):
        pass

class Estudiante(Usuario): 
    def __init__(self, nombre, apellido, email, contrasenia, legajo, anio_inscripcion_carrera):
        super().__init__(nombre, apellido, email, contrasenia)
        self._legajo = legajo 
        self._anio_inscripcion_carrera = anio_inscripcion_carrera
        self.cursos = []
        
    def __str__(self):
        return super().__str__() + f" \n- Legajo: {self._legajo}"
    
    def matriculacion_en_curso (self, curso):
        lista_alumnos.append(curso)
        print(f"Estudiante {self._nombre} matriculado en el curso {curso}")

    def validar_credenciales(self, email, contrasenia):
        super().validar_credenciales(email, contrasenia)
        if email == self._email and contrasenia == self._contrasenia:  
            return True
        else:
            return False


class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, contrasenia, titulo, anio_egreso):
        super().__init__(nombre, apellido, email, contrasenia)
        self._titulo = titulo
        self._anio_egreso = anio_egreso
        self.cursos = []

    def __str__(self):
        return super().__str__() + f" \n- Título: {self._titulo}"

    def dictar_curso(self, curso):
        self.cursos.append(curso)
        print(f"\nProfesor {self._nombre} dictando el curso '{curso._nombre}'")

    def validar_credenciales(self, email, contrasenia):
        super().validar_credenciales(email, contrasenia)
        if email == self._email and contrasenia == self._contrasenia:
            return True
        else:
            return False


class Curso: 
    def __init__(self, nombre):
        self._nombre = nombre
        self._contrasenia_matriculacion = generar_contrasenia()

    
    def __str__(self):
        return f"Curso: {self._nombre}"
    
#----CIERRE DECLARACION DE CLASES ------------------------------------

#---INICIO SUBMENU ALUMNOS Y OPCIONES ------------------------------------
def submenu_alumno():
    print ("\n1- Matricularse a un curso.")
    print ("2- Ver curso.")
    print ("3- Volver al menu principal.")
    opcion_alumno = int(input("\nSeleccione una opcion: "))
    print("")
    return opcion_alumno

def opcion1_submenu_alumno(alumno):
    print("Lista de cursos disponibles:")
    if len(mis_cursos) == 0:
        print("\nNo hay cursos disponibles de momento.")
        return

    for i, curso in enumerate(mis_cursos.values(), 1):
        print(f"{i}. {curso._nombre}")

    opcion_curso = int(input("Seleccione el curso al que desea matricularse: "))

    if opcion_curso < 1 or opcion_curso > len(mis_cursos):
        print("Opcion invalida. Por favor, elija un curso valido.")
        return

    curso_seleccionado = list(mis_cursos.values())[opcion_curso - 1]

    if curso_seleccionado in alumno.cursos:
        print(f"Ya esta matriculado en el curso '{curso_seleccionado._nombre}'.")
    else:
        contrasenia_ingresada = input(f"Ingrese la contraseña de matriculación para '{curso_seleccionado._nombre}': ")

        if contrasenia_ingresada == curso_seleccionado._contrasenia_matriculacion:
            alumno.cursos.append(curso_seleccionado)
            print(f"Matriculado en el curso '{curso_seleccionado._nombre}'.")
        else:
            print("Contraseña de matriculación incorrecta. No se pudo matricular en el curso.")

def opcion2_submenu_alumno(alumno):
    if not alumno.cursos:
        print("No esta inscrito en ningun curso.")
    else:
        for i, curso in enumerate(alumno.cursos, 1):
            print(f"{i} - {curso._nombre.title()}")

#---CIERRE SUBMENU ALUMNOS Y OPCIONES ----------------------------------------

#---INICIO SUBMENU PROFESOR Y OPCIONES --------------------
def submenu_profe():
    print ("\n1- Dictar curso.")
    print ("2- Ver curso.")
    print ("3- Volver al menu principal.")
    opcion_profe = int(input("\nSeleccione una opcion: "))
    print("")
    return opcion_profe

def opcion1_submenu_profe(profesor, mis_cursos):
    nombre_curso_principal = input("Ingrese el nombre del curso: ")
    nombre_curso = nombre_curso_principal.lower()
    if nombre_curso in mis_cursos:
        print ("\nEste curso ya fue dado de alta.")
    else:
        curso = Curso(nombre_curso)
        profesor.dictar_curso(curso)
        mis_cursos[nombre_curso] = curso
        print(f"Nombre: {nombre_curso} \nContraseña: {curso._contrasenia_matriculacion}")

def opcion2_submenu_profe(profesor):
    for i , curso in enumerate (profesor.cursos,1):
        print(f"{i}- {curso._nombre.title()}.")

#---CIERRE SUBMENU PROFESOR Y OPCIONES --------------------


#--- FUNCION MENU PRINCIPAL -------------------------
def menu_principal():
    print ("\n---Menu---")
    print ("1- Ingresar como alumno.")
    print ("2- Ingresar como profesor.")
    print ("3- Ver cursos.")
    print ("4- Salir.")  
    print ("")
    opcion = int(input("Seleccione una opcion: "))
    return opcion

#------ INICIO PROGRAMA PRINCIPAL ------------------------------------------------------------
def programa_principal():
    opcion = 0

    while opcion != 4:
        opcion = menu_principal()
        if opcion == 1:
            validacion_email = input("\nIngrese su email: ")
            print("")
            validacion_contrasenia = input("Ingrese su contraseña: ")
            alumno_encontrado = None
            for alumno in lista_alumnos:
                if alumno.validar_credenciales(validacion_email, validacion_contrasenia):
                    alumno_encontrado = alumno
                    break
            if alumno_encontrado:
                print(f"\nBienvenido, {alumno_encontrado._nombre}")
                while True:
                    opcion_alumno = submenu_alumno()
                    if opcion_alumno == 1:
                        opcion1_submenu_alumno(alumno_encontrado)
                    elif opcion_alumno == 2:
                        opcion2_submenu_alumno(alumno_encontrado)
                    elif opcion_alumno == 3: 
                        break
                    else: 
                        print("Opcion incorrecta! Ingresela nuevamente.\n")
            else:
                print("Credenciales incorrectas o estudiante inexistente, debe darse de alta en alumnado.")
        
        elif opcion == 2:
            validacion_email_profe = input("\nIngrese su email: ")
            print("")
            validacion_contrasenia_profe = input("Ingrese su contraseña: ")
            profe_encontrado = None
            for profe in lista_profesores:
                if profe.validar_credenciales(validacion_email_profe, validacion_contrasenia_profe):
                    profe_encontrado = profe
                    break
            if profe_encontrado:
                print(f"\nBienvenido, {profe_encontrado._nombre}")
                while True:
                    opcion_profe = submenu_profe()
                    if opcion_profe == 1:
                        opcion1_submenu_profe(profe_encontrado, mis_cursos)
                    elif opcion_profe == 2:
                        opcion2_submenu_profe(profe_encontrado)
                    elif opcion_profe == 3: 
                        break
                    else: 
                        print("Opcion incorrecta! Ingresela nuevamente.\n")
            else:
                print("Credenciales incorrectas o profe inexistente, debe darse de alta en alumnado.")

        elif opcion == 3:
            for profe_encontrado in lista_profesores:
                for curso in sorted(profe_encontrado.cursos):
                    print(f"Materia: {curso._nombre.title()} - Carrera: Tecnicatura Universitaria en Programacion")

        elif opcion == 4:
            print("Hasta luego!!\n")
            break
        else:
            print("Ingrese una opcion correcta! (1-4)")

#------ CIERRE PROGRAMA PRINCIPAL ------------------------------------------------------------

#DECLARACION DE ALUMNOS Y PROFESORES ------------------------------------------------------------

alumno1 = Estudiante("Mauro", "Brizio", "mauro@gmail.com", "123", 123, 2023)
lista_alumnos.append(alumno1)

alumno2 = Estudiante("Matias", "D'Anunzio", "mati@gmail.com", "123", 456, 2023)
lista_alumnos.append(alumno2)

profesor1 = Profesor("Mateo", "Caranta", "mateo@gmail.com", "123", "Licenciado", 1990)
lista_profesores.append(profesor1)

profesor2 = Profesor("Valentin", "Cura", "cura@gmail.com", "123", "Doctor", 2000)
lista_profesores.append(profesor2)

programa_principal()