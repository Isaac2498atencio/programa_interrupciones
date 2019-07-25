from prettytable import PrettyTable


# Objeto de las funciones
class controlador:
    def __init__(self, nombre, prioridad):
        self.nombre = nombre
        self.prioridad = prioridad


# class que guarda el momento y cuanto dura la interrupción
class interrupciones(controlador):
    def __init__(self, nombre, prioridad, cuando, duracion):
        super().__init__(nombre, prioridad)
        self.cuando = cuando
        self.duracion = duracion

    def resta(self):
        self.duracion = self.duracion - 1


# generar tablas
def generar_tabla(tiempo, diferencia, duracion, nombre, funciones):
    subtabla = []
    retornar = []
    indice = 0

    if duracion == 0:
        for r in range(2):
            if r == 0:
                tiempo_entrada = tiempo - diferencia
                for u in range(len(funciones)):
                    if nombre == funciones[u].nombre:
                        indice = u
                        break

                for r in range(len(funciones)):
                    subtabla.append("******")

                subtabla.pop(indice)
                subtabla.insert(indice, tiempo_entrada)
                retornar.append(subtabla)
                subtabla = []
            else:
                tiempo_salida = tiempo
                for o in range(len(funciones)):
                    if nombre == funciones[o].nombre:
                        indice = o
                        break

                for r in range(len(funciones)):
                    subtabla.append("******")

                subtabla.pop(indice)
                subtabla.insert(indice, tiempo_salida)
                retornar.append(subtabla)
                subtabla = []

        return retornar
    else:
        for r in range(2):
            if r == 0:
                tiempo_entrada = tiempo - diferencia - 1
                for r in range(len(funciones)):
                    if nombre == funciones[r].nombre:
                        indice = r
                        break

                for r in range(len(funciones)):
                    subtabla.append("******")

                subtabla.pop(indice)
                subtabla.insert(indice, tiempo_entrada)
                retornar.append(subtabla)
                subtabla = []
            else:
                tiempo_salida = tiempo
                for r in range(len(funciones)):
                    if nombre == funciones[r].nombre:
                        indice = r
                        break

                for r in range(len(funciones)):
                    subtabla.append("******")

                subtabla.pop(indice)
                subtabla.insert(indice, tiempo_salida)
                retornar.append(subtabla)
                subtabla = []

        return retornar


# Iniciar programa de interrupciones
def iniciar_programa(a, funciones):
    tabla_retornar = []  # tabla que se retorna al main
    cola = []
    acciones = a  # copia de las acciones mandadas del main
    tiempo = 0  # contado de tiempo
    tiempo_total = duracion_de_programas(acciones)
    diferencia = 0  # la duración de una acción sin interrupción
    # generar las interrupciones iniciales
    interrupcion_actual = acciones[0]
    acciones.pop(0)
    interrupcion_siguiente = acciones[0]
    acciones.pop(0)

    # inicia tiempo
    while tiempo <= tiempo_total:
        tiempo = tiempo+1
        if interrupcion_actual.duracion == 0:
            tiempo = tiempo - 1
            # generar las filas
            subtabla = generar_tabla(tiempo, diferencia, interrupcion_actual.duracion, interrupcion_actual.nombre,
                                     funciones)
            for k in range(2):
                    tabla_retornar.append(subtabla[k])

            subtabla.clear()

            if len(cola) == 0:
                interrupcion_actual = interrupcion_siguiente
            else:
                interrupcion_actual = cola[0]
                cola.pop(0)


            if tiempo == tiempo_total:
                tiempo = tiempo_total+100
            # reiniciar diferencia
            diferencia = 0
        elif tiempo == interrupcion_siguiente.cuando:
            if interrupcion_actual.prioridad > interrupcion_siguiente.prioridad:
                interrupcion_actual.resta()

                # generar las filas
                subtabla = generar_tabla(tiempo, diferencia, interrupcion_actual.duracion, interrupcion_actual.nombre,
                                         funciones)
                for k in range(2):
                    tabla_retornar.append(subtabla[k])

                subtabla .clear()

                cola.append(interrupcion_actual)  # guardar interrupción actual en cola
                cola.sort(key=lambda x: x.prioridad)  # orsenar cola por prioridad

                interrupcion_actual = interrupcion_siguiente
                if len(acciones) == 0:
                    if len(cola) == 0:
                        pass
                    else:
                        interrupcion_siguiente = cola[0]
                        cola.pop(0)
                else:
                    interrupcion_siguiente = acciones[0]
                    acciones.pop(0)

                diferencia = 0
            elif interrupcion_actual.prioridad <= interrupcion_siguiente.prioridad:
                cola.append(interrupcion_siguiente)
                interrupcion_siguiente = acciones[0]
                if len(acciones) == 0:
                    pass
                else:
                    acciones.pop(0)
                cola.sort(key=lambda x: x.prioridad)  # orsenar cola por prioridad
                interrupcion_actual.resta()
                diferencia = diferencia + 1
        else:
            interrupcion_actual.resta()
            diferencia = diferencia + 1


    return tabla_retornar


# Generar titulos
def gen_titulos(funciones):
    titulos = []
    for x in range(len(funciones)):
        titulos.append(funciones[x].nombre)

    return titulos


# Menu 1 para inicializar las funciones y su prioridad
def crear_prioridades(prioridades, IQR):
    if IQR == 0:
        return controlador("Reloj del sistema", prioridades[IQR])
    elif IQR == 1:
        return controlador("Teclado", prioridades[IQR])
    elif IQR == 2:
        return controlador("PIC", prioridades[IQR])
    elif IQR == 3:
        opcion = int(input("1 para COM 2 o 2 para COM 4 "))
        if opcion == 1:
            return controlador("COM 2", prioridades[IQR])
        if opcion == 2:
            return controlador("COM 4", prioridades[IQR])
    elif IQR == 4:
        opcion = int(input("1 para COM 1 o 2 para COM 3 "))
        if opcion == 1:
            return controlador("COM 1", prioridades[IQR])
        elif opcion == 2:
            return controlador("COM 3", prioridades[IQR])
    elif IQR == 5:
        return controlador("Libre", prioridades[IQR])
    elif IQR == 6:
        return controlador("Floppy Disk", prioridades[IQR])
    elif IQR == 7:
        return controlador("Impresora", prioridades[IQR])
    elif IQR == 8:
        return controlador("CMOS", prioridades[IQR])
    elif IQR == 9:
        opcion = int(input("1 para Red o 2 para Sonido o 3 para SCS "))
        if opcion == 1:
            return controlador("Red", prioridades[IQR])
        elif opcion == 2:
            return controlador("Sonido", prioridades[IQR])
        elif opcion == 3:
            return controlador("SCS", prioridades[IQR])
    elif IQR == 10:
        return controlador("Libre", prioridades[IQR])
    elif IQR == 11:
        return controlador("Libre", prioridades[IQR])
    elif IQR == 12:
        return controlador("PS-mouse", prioridades[IQR])
    elif IQR == 13:
        return controlador("CO-procesador matemático", prioridades[IQR])
    elif IQR == 14:
        return controlador("Disco", prioridades[IQR])
    elif IQR == 15:
        return controlador("Libre", prioridades[IQR])


# La duración de las funciones
def duracion_de_programas(datos):
    x = 0
    for r in range(len(datos)):
        x = x + datos[r].duracion

    return x


# Main
prioridades = [1, 2, 100, 11, 12, 13, 14, 15, 3, 4, 5, 6, 7, 8, 9, 10]
objFunciones = []
acciones = []
titulos = []
tabla_procesos = PrettyTable()
IQR = 0
cont = 0
menu = 0
while cont == 0:
    try:
        print("1 para cargar las funciones a utilizar")
        print("2 para ver las funciones que participan")
        print("3 para asignar la interrupción y duración")
        print("4 para ver las funciones que participan con su tiempo de interrupción y su momento")
        print("5 para Correr programa de interrupciones")
        print("6 para salir del programa")
        menu = int(input("Introduce aqui: "))
    except ValueError:
        print("Error lógico")

    if menu == 1:
        i = 0
        while i == 0:
            try:
                IQR = int(
                    input("Introduzca el IQR de la funcion que va a utilizar o 999 si ya no hay mas controladores"))
                if 15 >= IQR >= 0:
                    intermedio = crear_prioridades(prioridades, IQR)
                    objFunciones.append(intermedio)
                    i = 0
                elif IQR == 999:
                    i = 1
                else:
                    print("Opción no valida")
                    i = 0
            except TypeError:
                print("Error al seleccionar")

        # verificar si pci esta en el arreglo
        for x in range(len(objFunciones)):
            if objFunciones[x].nombre == "PIC":
                bandera = 0
                break
            else:
                bandera = 1

        # agregar PIC si no se agrego en el programa
        if bandera == 1:
            intermedio = crear_prioridades(prioridades, 2)
            objFunciones.append(intermedio)

        objFunciones.sort(key=lambda x: x.prioridad)

    elif menu == 2:
        for r in range(len(objFunciones)):
            print("\n")
            print(objFunciones[r].nombre)
            print(objFunciones[r].prioridad)
            print("\n")


    elif menu == 3:
        x = 0
        while x == 0:
            print("De las siguientes funciones cual realiza interrupción ... (999 para ninguna)")
            for r in range(len(objFunciones) - 1):
                print("\n")
                print(r, ". ", objFunciones[r].nombre)

            try:
                valor = int(input("Introducir numero de funcion: "))
                if 0 <= valor < (len(objFunciones) - 1):
                    momento = int(input("Introduzca el momento de la interrupción en segundos: "))
                    duracion = int(input("Introduzca la duración de la interrupción en segundos: "))
                    acciones.append(
                        interrupciones(objFunciones[valor].nombre, objFunciones[valor].prioridad, momento, duracion))
                    x = 0
                elif valor == 999:
                    print("Listo")
                    x = 1
                else:
                    print("Valor no correcto")
                    x = 0
            except TypeError:
                print("Error")

        try:
            duracion = int(input("Introduzca la duración del programa"))
            acciones.append(
                interrupciones(objFunciones[-1].nombre, objFunciones[-1].prioridad, 0, duracion))
        except TypeError:
            print("Error")

        acciones.sort(key=lambda x: x.cuando)

    elif menu == 4:
        for r in range(len(acciones)):
            print("\n")
            print(acciones[r].cuando)
            print(acciones[r].nombre)
            print(acciones[r].prioridad)
            print(acciones[r].duracion)
            print("\n")

    elif menu == 5:
        titulos = gen_titulos(objFunciones)
        tabla_procesos.field_names = titulos
        tabla_retornada = iniciar_programa(acciones, objFunciones)

        for x in range(len(tabla_retornada)):
            tabla_procesos.add_row(tabla_retornada[x])

        print(tabla_procesos)


    elif menu == 6:
        print("The end")
        cont = 1
    else:
        print("Error al introducir opción")
