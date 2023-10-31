from abc import ABC, abstractmethod
from contrasenia import generar_contrasenia
from datetime import date

#- DECLARACION DE VARIABLES GLOBALES
lista_alumnos = []  
lista_profesores = []
mis_cursos = {}
lista_carreras = []
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
    def __init__(self, nombre, apellido, email, contrasenia, legajo, anio_inscripcion_carrera, carrera):
        super().__init__(nombre, apellido, email, contrasenia)
        self._legajo = legajo 
        self._anio_inscripcion_carrera = anio_inscripcion_carrera
        self.cursos = []
        self._carrera = carrera
        
    def __str__(self):
        return super().__str__() + f" \n- Legajo: {self._legajo}"
    
    def matricular_en_curso (self, curso):
        self.cursos.append(curso)
        print(f"\nEstudiante {self._nombre} matriculado en el {curso}")

    def desmatricular_curso(self,curso):
        self.cursos.remove(curso)
        print(f"\nSe ha desmatriculado del {curso}")

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
    prox_cod = 1 
    def __init__(self, nombre, carrera):
        self._nombre = nombre
        self._codigo = Curso.prox_cod
        Curso.prox_cod +=1
        self._contrasenia_matriculacion = generar_contrasenia()
        self._carrera = carrera
        self.archivos = []

    
    def __str__(self):
        return f"Curso: {self._nombre}"
    
    def nuevo_archivo(self,archivo):
        self.archivos.append(archivo)


class Carrera:
    def __init__(self, nombre,cant_anios):
        self._nombre = nombre
        self._cant_anios = cant_anios
        self.cursos_carrera = []
        self.estudiante_carrera = []
    
    def __str__(self):
        pass

    def get_cantidad_materias() -> int:
        pass

class Archivo:
    def __init__(self, nombre, fecha, formato, cursos):
        self._nombre = nombre 
        self._fecha = fecha
        self._formato = formato
        self._cursos = cursos
    
    def __str__():
        pass



#----CIERRE DECLARACION DE CLASES ------------------------------------

#---INICIO SUBMENU ALUMNOS Y OPCIONES ------------------------------------
def submenu_alumno():
    print ("\n1- Matricularse a un curso.")
    print ("2- Desmatricularse de un curso.")
    print ("3- Ver curso.")
    print ("4- Volver al menu principal.")
    opcion_alumno = int(input("\nSeleccione una opcion: "))
    print("")
    return opcion_alumno

def opcion1_submenu_alumno(alumno):
    print("Lista de cursos disponibles de la carrera:")
    if len(mis_cursos) == 0:
        print("\nNo hay cursos disponibles de momento en la carrera.")
        return

    curso_seleccionado = list(mis_cursos.values())

    cursos_de_carrera = []

    for curso in curso_seleccionado:
        if curso._carrera == alumno._carrera:
            cursos_de_carrera.append(curso)

    for i, curso in enumerate(cursos_de_carrera, 1):
        print(f"{i}. {curso._nombre.title()}")

    opcion_curso = int(input("\nSeleccione el curso al que desea matricularse: "))

    if opcion_curso < 1 or opcion_curso > len(mis_cursos):
        print("Opcion invalida. Por favor, elija un curso valido.")
        return

    curso_seleccionado = cursos_de_carrera[opcion_curso - 1]

    if curso_seleccionado in alumno.cursos:
        print(f"Ya esta matriculado en el curso '{curso_seleccionado._nombre.title()}'.")
    else:
        contrasenia_ingresada = input(f"Ingrese la contraseña de matriculación para '{curso_seleccionado._nombre.title()}': ")

        if contrasenia_ingresada == curso_seleccionado._contrasenia_matriculacion:
            alumno.matricular_en_curso(curso_seleccionado)
        else:
            print("Contraseña de matriculación incorrecta. No se pudo matricular en el curso.")

def opcion2_submenu_alumno(alumno):
    if not alumno.cursos:
        print("No esta inscrito en ningun curso.")
    else:
        for i, curso in enumerate(alumno.cursos, 1):
            print(f"{i} - {curso._nombre.title()}")
    desmatriculacion = int(input("\nSeleccione el curso del que desea desmatricularse: "))
    if desmatriculacion < 1 or desmatriculacion > len(mis_cursos):
        print("Opcion invalida. Por favor, elija un curso valido.")
        return
    else:
        opcion_curso_desmatriculado = alumno.cursos[desmatriculacion - 1]
        alumno.desmatricular_curso(opcion_curso_desmatriculado)
    
    
def opcion3_submenu_alumno(alumno):
    if not alumno.cursos:
        print("No está inscrito en ningún curso.")
    else:
        print("Cursos en los que está matriculado:")
        for curso in alumno.cursos:
            print(f"{curso._codigo} - {curso._nombre.title()}")

        seleccion_curso = int(input("Seleccione el curso para ver los archivos: "))

        if seleccion_curso < 1 or seleccion_curso > len(alumno.cursos):
            print("Opción inválida. Por favor, elija un curso válido.")
            return

        curso_seleccionado = alumno.cursos[seleccion_curso - 1]

        print(f"\nArchivos para el curso '{curso_seleccionado._nombre.title()}':")
        archivos_ordenados = sorted(curso_seleccionado.archivos, key=lambda archivo: archivo._fecha)

        if len(archivos_ordenados) == 0:
            print("No hay archivos disponibles para este curso.")
        else:
            for archivo in archivos_ordenados:
                print(archivo._nombre + archivo._formato)

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
    x = 1 
    for seleccion in lista_carreras:
        print(x,"- ",seleccion)
        x += 1
    carrera_seleccionada = int(input("\nIngrese carrera a la que se dara de alta el curso: "))
    
    if carrera_seleccionada < 1 or carrera_seleccionada > len(lista_carreras):
        print("\nOpción inválida. Por favor, elija una carrera válida.")
        return

    nombre_carrera_seleccionada = lista_carreras[carrera_seleccionada - 1]
    nombre_curso_principal = input("Ingrese el nombre del curso: ")
    nombre_curso = nombre_curso_principal.lower()
    if nombre_curso in mis_cursos:
        print("\nEste curso ya fue dado de alta.")
    else:
        curso = Curso(nombre_curso, nombre_carrera_seleccionada)  
        profesor.dictar_curso(curso)
        mis_cursos[nombre_curso] = curso  
        print(f"Nombre: {nombre_curso.title()} \nCódigo: {curso._codigo} \nContraseña: {curso._contrasenia_matriculacion}")


def opcion2_submenu_profe(profesor):
    for i, curso in enumerate(profesor.cursos, 1):
        print(f"{i}- {curso._nombre.title()}.")

    if len(profesor.cursos) != 0:
        curso_seleccion = int(input("\nIngrese el número de curso a revisar: "))

        if curso_seleccion < 1 or curso_seleccion > len(profesor.cursos):
            print("\nOpción inválida. Por favor, elija un curso válido.")
            return
        else:
            curso_revisado = profesor.cursos[curso_seleccion - 1]
            print(f"\nNombre del curso: {curso_revisado._nombre.title()}")
            print(f"Código de curso: {curso_revisado._codigo}")
            print(f"Contraseña: {curso_revisado._contrasenia_matriculacion}")
            print(f"Cantidad de archivos: {len(curso_revisado.archivos)}")

            archivos_agregados = input("\n¿Desea agregar un archivo? 1-Si 2-No \nRespuesta: ")
            if archivos_agregados == "1":
                nombre_archivo = input("\nIngrese nombre del archivo: ")
                formato_archivo = input("Ingrese el formato del archivo: ")
                crear_archivo = Archivo(nombre_archivo, date.today(), formato_archivo, curso_revisado)
                #curso_revisado.archivos.append(nuevo_archivo) 
                curso_revisado.nuevo_archivo(crear_archivo)
            elif archivos_agregados == "2":
                return None
            else:
                print ("\nOpcion incorrecta, vuelva a intentarlo.")
                return submenu_profe

    else:
        print ("No hay cursos disponibles.")

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
                        opcion3_submenu_alumno(alumno_encontrado)
                    elif opcion_alumno == 4: 
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
                curso_ordenado = sorted(profe_encontrado.cursos, key=lambda curso: curso._nombre)
                for curso in curso_ordenado:
                    print(f"Materia: {curso._nombre.title()} - Carrera: {curso._carrera.title()}")
        
        elif opcion == 4:
            print("Hasta luego!!\n")
            break
        else:
            print("Ingrese una opcion correcta! (1-4)")

#------ CIERRE PROGRAMA PRINCIPAL ------------------------------------------------------------

#DECLARACION DE ALUMNOS Y PROFESORES ------------------------------------------------------------
carrera1 = Carrera("Tecnicatura Universitaria en Programacion",2)
lista_carreras.append(carrera1._nombre)

carrera2 = Carrera("Medicina", 6)
lista_carreras.append(carrera2._nombre)

alumno1 = Estudiante("Mauro", "Brizio", "mauro@gmail.com", "123", 123, 2023, carrera1._nombre)
lista_alumnos.append(alumno1)

alumno2 = Estudiante("Matias", "D'Anunzio", "mati@gmail.com", "123", 456, 2023, carrera2._nombre)
lista_alumnos.append(alumno2)

profesor1 = Profesor("Mateo", "Caranta", "mateo@gmail.com", "123", "Licenciado", 1990)
lista_profesores.append(profesor1)

profesor2 = Profesor("Valentin", "Cura", "cura@gmail.com", "123", "Doctor", 2000)
lista_profesores.append(profesor2)

programa_principal()