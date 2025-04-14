import time
import random
from opcua import Server
import socket
import threading
from threading import Thread
import asyncio

# Obtener la IP local para configurar el endpoint
local_ip = socket.gethostbyname(socket.gethostname())

# Crear una instancia del servidor OPC UA
server = Server()

# Configurar el servidor
server.set_endpoint(f"opc.tcp://{local_ip}:4841")
server.set_server_name("Servidor OPC UA - Datos Dinámicos")

# Registrar un espacio de nombres para las variables
uri = "http://example.org/opcua/server/"
idx = server.register_namespace(uri)

objects = server.nodes.objects
server_interfaces = objects.add_object(idx, "ServerInterfaces")
receta_obj = server_interfaces.add_object(idx, "Server interface_1")
datos_enviar = receta_obj.add_object(idx, "DATOS OPC A ENVIAR")

lista_alarmas = datos_enviar.add_object(idx, "Alarmas")

grupo_alarmas = [
    "CANCELACION",
    "FALLAS CILINDROS",
    "GENERALES",
    "INICIO DE CICLO",
    "POSICIONADOR",
    "PULSADORES",
    "ROBOT",
    "SDDA",
    "SERVOS"
]

# Crear subnodos y sus arrays
for grupo in grupo_alarmas:
    nodo_grupo = lista_alarmas.add_variable(idx, grupo, 0)
    
    # Crear 20 variables (tipo bool) dentro de cada grupo
    for i in range(20):
        var = nodo_grupo.add_variable(idx, f"[{i}]", False)
        var.set_writable() 

Comprobacion_datos = datos_enviar.add_variable(idx, "Confirmacion_envio", True)

variables = []

variables += [
    Comprobacion_datos.add_variable(idx, "confirmacion_envio",True),
    Comprobacion_datos.add_variable(idx, "receta_obtenido", 1),
    Comprobacion_datos.add_variable(idx, "torre_obtenido", 1) 
]

nivelesHN = datos_enviar.add_variable(idx, "DatosNivelesHN", 0)  # Se crea solo una vez
variables = [
    nivelesHN.add_variable(idx, "Correccion_hN1", "1"),
    nivelesHN.add_variable(idx, "Correccion_hN2", "2"),
    nivelesHN.add_variable(idx, "Correccion_hN3", "3"),
    nivelesHN.add_variable(idx, "Correccion_hN4", "4"),
    nivelesHN.add_variable(idx, "Correccion_hN5", "5"),
    nivelesHN.add_variable(idx, "Correccion_hN6", "6"),
    nivelesHN.add_variable(idx, "Correccion_hN7", "7"),
    nivelesHN.add_variable(idx, "Correccion_hN8", "8"),
    nivelesHN.add_variable(idx, "Correccion_hN9", "9"),
    nivelesHN.add_variable(idx, "Correccion_hN10", "10"),
    nivelesHN.add_variable(idx, "Correccion_hN11", "11"),
]

nivelesuHN = datos_enviar.add_variable(idx, "DatosNivelesuHN", 0)  # Se crea solo una vez
variables = [
    nivelesuHN.add_variable(idx, "ultimo_hNivel1", "1"),
    nivelesuHN.add_variable(idx, "ultimo_hNivel2", "2"),
    nivelesuHN.add_variable(idx, "ultimo_hNivel3", "3"),
    nivelesuHN.add_variable(idx, "ultimo_hNivel4", "4"),
    nivelesuHN.add_variable(idx, "ultimo_hNivel5", "5"),
    nivelesuHN.add_variable(idx, "ultimo_hNivel6", "6"),
    nivelesuHN.add_variable(idx, "ultimo_hNivel7", "7"),
    nivelesuHN.add_variable(idx, "ultimo_hNivel8", "8"),
    nivelesuHN.add_variable(idx, "ultimo_hNivel9", "9"),
    nivelesuHN.add_variable(idx, "ultimo_hNivel10", "10"),
    nivelesuHN.add_variable(idx, "ultimo_hNivel11", "11"),
]

nivelesChG = datos_enviar.add_variable(idx, "DatosNivelesChG",0)  # Se crea solo una vez
variables = [
    nivelesChG.add_variable(idx, "Correccion_hguardado_N1", "1"),
    nivelesChG.add_variable(idx, "Correccion_hguardado_N2", "2"),
    nivelesChG.add_variable(idx, "Correccion_hguardado_N3", "3"),
    nivelesChG.add_variable(idx, "Correccion_hguardado_N4", "4"),
    nivelesChG.add_variable(idx, "Correccion_hguardado_N5", "5"),
    nivelesChG.add_variable(idx, "Correccion_hguardado_N6", "6"),
    nivelesChG.add_variable(idx, "Correccion_hguardado_N7", "7"),
    nivelesChG.add_variable(idx, "Correccion_hguardado_N8", "8"),
    nivelesChG.add_variable(idx, "Correccion_hguardado_N9", "9"),
    nivelesChG.add_variable(idx, "Correccion_hguardado_N10", "10"),
    nivelesChG.add_variable(idx, "Correccion_hguardado_N11", "11"),
]

nivelesChB = datos_enviar.add_variable(idx, "DatosNivelesChB",0)  # Se crea solo una vez
variables = [
    nivelesChB.add_variable(idx, "Correccion_hbusqueda_N1", "1"),
    nivelesChB.add_variable(idx, "Correccion_hbusqueda_N2", "2"),
    nivelesChB.add_variable(idx, "Correccion_hbusqueda_N3", "3"),
    nivelesChB.add_variable(idx, "Correccion_hbusqueda_N4", "4"),
    nivelesChB.add_variable(idx, "Correccion_hbusqueda_N5", "5"),
    nivelesChB.add_variable(idx, "Correccion_hbusqueda_N6", "6"),
    nivelesChB.add_variable(idx, "Correccion_hbusqueda_N7", "7"),
    nivelesChB.add_variable(idx, "Correccion_hbusqueda_N8", "8"),
    nivelesChB.add_variable(idx, "Correccion_hbusqueda_N9", "9"),
    nivelesChB.add_variable(idx, "Correccion_hbusqueda_N10", "10"),
    nivelesChB.add_variable(idx, "Correccion_hbusqueda_N11", "11"),
]

nivelesFA = datos_enviar.add_variable(idx, "DatosNivelesFA",0)  # Se crea solo una vez
variables = [
    nivelesFA.add_variable(idx, "FallasN1", "1"),
    nivelesFA.add_variable(idx, "FallasN2", "2"),
    nivelesFA.add_variable(idx, "FallasN3", "3"),
    nivelesFA.add_variable(idx, "FallasN4", "4"),
    nivelesFA.add_variable(idx, "FallasN5", "5"),
    nivelesFA.add_variable(idx, "FallasN6", "6"),
    nivelesFA.add_variable(idx, "FallasN7", "7"),
    nivelesFA.add_variable(idx, "FallasN8", "8"),
    nivelesFA.add_variable(idx, "FallasN9", "9"),
    nivelesFA.add_variable(idx, "FallasN10", "10"),
    nivelesFA.add_variable(idx, "FallasN11", "11"),
]


estado_equipo = datos_enviar.add_variable(idx, "Estado_equipo", True)
variables+= [
    estado_equipo.add_variable(idx, "Ciclo_iniciado", True),
    estado_equipo.add_variable(idx, "Estado_actual", 1),
    estado_equipo.add_variable(idx, "Nivel_finalizado", 0)
]

datos_gripper = datos_enviar.add_variable(idx, "datosGripper", True)
variables += [
    datos_gripper.add_variable(idx, "NGripperActual", 2),
    datos_gripper.add_variable(idx, "NGripperProximo", 3),
]

datos_robot = datos_enviar.add_variable(idx, "datosRobot", True)
variables += [
    datos_robot.add_variable(idx, "posicionX", 20),
    datos_robot.add_variable(idx, "posicionY", 40),
    datos_robot.add_variable(idx, "posicionZ", 0),
]

datos_sdda = datos_enviar.add_variable(idx, "datosSdda", True)
variables += [
    datos_sdda.add_variable(idx, "sdda_long_mm", 0),
    datos_sdda.add_variable(idx, "sdda_nivel_actual", 0),
    datos_sdda.add_variable(idx, "sdda_vertical_mm", 0)
]

datos_seleccionados = datos_enviar.add_variable(idx, "datosSeleccionados", True)
variables += [
    datos_seleccionados.add_variable(idx, "N_receta_actual", 0),
    datos_seleccionados.add_variable(idx, "N_receta_proxima", 0),
    datos_seleccionados.add_variable(idx, "N_torre_actual", 0),
    datos_seleccionados.add_variable(idx, "N_torre_proxima", 0),
    datos_seleccionados.add_variable(idx, "pantalla_receta", True),
] 

datos_torre = datos_enviar.add_variable(idx, "datosTorre", True)
variables = [
    datos_torre.add_variable(idx, "TAG", "Cuadrado"),
    datos_torre.add_variable(idx, "Correccion_hBastidor", 1),
    datos_torre.add_variable(idx, "Correccion_hAjuste", 2),
    datos_torre.add_variable(idx, "Correccion_hAjusteN1", 3),
    datos_torre.add_variable(idx, "Correccion_DisteNivel", 4),
]

desmoldeo = datos_enviar.add_variable(idx, "desmoldeo", True)
variables+= [
    desmoldeo.add_variable(idx, "cicloTiempoTotal", 1),
    desmoldeo.add_variable(idx, "cicloTipoFin", 1),
    desmoldeo.add_variable(idx, "desmoldeobanda",1)
]


recetario = datos_enviar.add_variable(idx, "RECETARIO", 0)

# Lista de variables por receta
variables_receta = [
    "ALTO DE MOLDE",
    "ALTO DE PRODUCTO",
    "ALTURA AJUSTE",
    "ALTURA AJUSTE N1",
    "ALTURA DE BASTIDOR",
    "ALTURA N1",
    "ANCHO PRODUCTO",
    "CANTIDAD NIVELES",
    "DELTA ENTRE NIVELES",
    "LARGO DE MOLDE",
    "LARGO DE PRODUCTO",
    "MOLDES POR NIVEL",
    "NOMBRE",
    "NUMERO DE GRIPPER",
    "PESO DEL PRODUCTO",
    "PRODUCTOS POR MOLDE",
    "TIPO DE MOLDE"
]
RecetaNombres = [
    "(OV-A) OVALADO A OVA-000",
    "(OV-B) OVALADO B OVA-001",
    "(CU) CUADRADO",
    "(QP) QUESO PUERCO",
    "(7K) RECTANGULAR",
    "(6K) MANDOLINA",
    "(LU) LUNCH"
]


# Crear 20 recetas con las variables
for i in range(20):
    receta = recetario.add_variable(idx, f"[{i}]",0)
    for var_name in variables_receta:
        if var_name == "NOMBRE":
            nombre_valor = RecetaNombres[i] if i < len(RecetaNombres) else ""
            receta.add_variable(idx, var_name, nombre_valor)
        else:
            receta.add_variable(idx, var_name, 0)


# Función para la simulación del ciclo de desmoldeo
def ciclo_de_desmoldeo():
    global variables

    # Configuraciones iniciales para las variables
    idReceta_actual = 1
    RecetaNombres = [
        "(OV-A) OVALADO A OVA-000 ", "(OV-B) OVALADO B OVA-001", "(CU) CUADRADO ", "(QP) QUESO PUERCO", "(7K) RECTANGULAR ", "(6K) MANDOLINA", "(LU) LUNCH "
    ]
    PesoPorProducto = {1: 5.5, 2: 6.3, 3: 7.0, 4: 6.5, 5: 5.8, 6: 6.1, 7: 7.3}
    PesoProducto = {1: 75.5, 2: 80.0, 3: 82.3, 4: 76.5, 5: 78.0, 6: 79.5, 7: 83.0}

    gripper_actual = 1
    gripper_proximo = 2
    torre_actual = 1
    torre_proxima = 1
    nivel_actual = 1
    estado_maquina = 1
    desmoldeo_banda = 1

    while True:
        idReceta_actual = (idReceta_actual % 7) + 1  # Cambiar al siguiente idReceta entre 1 y 7
        receta_nombre = RecetaNombres[idReceta_actual - 1]  # Obtener el nombre de la receta
        peso_por_producto = PesoPorProducto[idReceta_actual]
        peso_producto = PesoProducto[idReceta_actual]

        # Simulación de la falla de nivel cada 15 o 20 ciclos
        if random.randint(1, 20) == 1:  # Aproximadamente 1 falla cada 15-20 ciclos
            print("¡Falla de nivel detectada!")

        # Simular el ciclo de desmoldeo de niveles de torre
        while nivel_actual <= random.randint(10, 11):  # El nivel va hasta 9, 10 o 11
            print(f"Procesando torre {torre_actual}, nivel {nivel_actual}")
            estado_maquina = 1
            ciclo_inicio = True
            # Actualizar los valores de los nodos durante el ciclo
            for var in variables:
                if var.get_browse_name().Name == "N_receta_proxima":
                    var.set_value((idReceta_actual % 7) + 1)
                elif var.get_browse_name().Name == "NGripperActual":
                    var.set_value(gripper_actual)
                elif var.get_browse_name().Name == "NGripperProximo":
                    var.set_value(gripper_proximo)
                elif var.get_browse_name().Name == "N_torre_actual":
                    var.set_value(torre_actual)
                elif var.get_browse_name().Name == "N_torre_proxima":
                    var.set_value(torre_proxima)
                elif var.get_browse_name().Name == "sdda_nivel_actual":
                    var.set_value(nivel_actual)
                elif var.get_browse_name().Name == "Estado_actual":
                    var.set_value(estado_maquina)
                elif var.get_browse_name().Name == "desmoldeobanda":
                    var.set_value(desmoldeo_banda)
                elif var.get_browse_name().Name == "Ciclo_iniciado":
                    var.set_value(ciclo_inicio)
                
            print(f"Peso POR nivel: {peso_por_producto} - PesoProducto: {peso_producto} " )
            # Imprimir el estado actual
            print(f"  Receta: {receta_nombre}, Gripper: {gripper_actual}, Torre: {torre_actual}, Nivel: {nivel_actual}")
            
            # Incrementar nivel
            nivel_actual += 1
            time.sleep(5)  # Simular el tiempo de desmoldeo por nivel (1 minuto por nivel)
          # La máquina pasa a estado 2 cuando termina el ciclo
        print("Ciclo de desmoldeo finalizado. Estado de la máquina cambiado a 2.")

        gripper_actual = gripper_proximo
        gripper_proximo = (gripper_proximo % 4) + 1  # Cambiar gripper de 1 a 4

        # Actualizar receta para el próximo ciclo
        idReceta_actual = (idReceta_actual % 7) + 1  # Cambiar a la siguiente receta
        print(f"Receta para el próximo ciclo: {RecetaNombres[idReceta_actual - 1]}")
        torre_proxima+=1
        # Reajustar los niveles para el próximo ciclo
        torre_actual = torre_proxima
        if torre_actual == 6:
            torre_actual = 1
            torre_proxima = 2
        nivel_actual = 1
        estado_maquina = 2
        ciclo_inicio = False
        # variables[19].set_value(ciclo_inicio)

        # Desmoldeo banda cambia entre 1 y 2
        desmoldeo_banda = random.choice([1, 2])

        print("-" * 50)  # Separador para los ciclos
        print(f"ESTADO D EL MAQUINAAAA:   {estado_maquina == 2}")
        # Espera entre ciclos (simulando tiempo hasta el próximo ciclo)
        print(f"Esperando hasta el próximo ciclo de desmoldeo...")
        time.sleep(10)  # Espera entre 5 y 8 minutos hasta el siguiente ciclo

def actualizar_datos_robot():
    global variables
    while True:
        # Generar valores aleatorios para las posiciones
        nueva_posicion_x = random.uniform(0, 500)  # Valor aleatorio flotante entre 0 y 500
        nueva_posicion_y = random.uniform(0, 500)  # Valor aleatorio flotante entre 0 y 500
        nueva_posicion_z = random.uniform(0, 100)  # Valor aleatorio flotante entre 0 y 100

        nueva_posicion_vertical = random.uniform(0, 100) # Valor aleatorio
        nueva_posicion_horizontal = random.uniform(0, 100)

        # Acceder a las variables y actualizarlas
        try:
            for var in variables:
                if var.get_browse_name().Name == "posicionX":
                    var.set_value(nueva_posicion_x)
                elif var.get_browse_name().Name == "posicionY":
                    var.set_value(nueva_posicion_y)
                elif var.get_browse_name().Name == "posicionZ":
                    var.set_value(nueva_posicion_z)
                elif var.get_browse_name().Name == "sdda_vertical_mm":
                    var.set_value(nueva_posicion_vertical)
                elif var.get_browse_name().Name == "sdda_long_mm":
                    var.set_value(nueva_posicion_horizontal)
                    
        except Exception as e:
            print(f"Error al actualizar las variables: {e}")
        
        time.sleep(1)

def iniciar_actualizacion_robot():
    thread_actualizacion_robot = threading.Thread(target=actualizar_datos_robot)
    thread_actualizacion_robot.daemon = True  # Hacer que el hilo se termine cuando termine el programa principal
    print("🛠️ Hilo de actualización del robot iniciado.")
    thread_actualizacion_robot.start()

# Iniciar la rutina
if __name__ == "__main__":
    try:
        print("Servidor OPC UA iniciado en", server.endpoint)
        server.start()

        iniciar_actualizacion_robot()
        #thread1.start()
        #thread2.start()
        #thread3.start()
        ciclo_de_desmoldeo()
        
    except KeyboardInterrupt:
        print("\nServidor detenido por el usuario.")
    finally:
        server.stop()
        print("Servidor OPC UA apagado.")
