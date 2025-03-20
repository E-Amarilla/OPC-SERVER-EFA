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

# Crear objetos y variables
receta_obj = server_interfaces.add_object(idx, "Server interface_1")
variables = [
    receta_obj.add_variable(idx, "Nombre actual", "Jamon"),
    receta_obj.add_variable(idx, "PesoProducto", 10.0),  # Peso X FILA de Torre
    receta_obj.add_variable(idx, "TipoMolde", 1),
    receta_obj.add_variable(idx, "TotalNiveles", 2.0),
    receta_obj.add_variable(idx, "idRecetaActual", 1),
    receta_obj.add_variable(idx, "idRecetaProxima", 1),  
]

variables += [
    receta_obj.add_variable(idx, "NGripperActual", 2),
    receta_obj.add_variable(idx, "NGripperProximo", 3),
]

variables += [
    receta_obj.add_variable(idx, "posicionX", 20),
    receta_obj.add_variable(idx, "posicionY", 40),
    receta_obj.add_variable(idx, "posicionZ", 0),
]

#datosTorre = server.nodes.objects.add_object(idx, "datosTorre")
variables += [
    receta_obj.add_variable(idx, "torreActual", 1),
    receta_obj.add_variable(idx, "torreProxima", 2),
]
#datosSdda = server.nodes.objects.add_object(idx, "datosSdda")
variables += [
    receta_obj.add_variable(idx, "nivel_fin",1),
    receta_obj.add_variable(idx, "sdda_long_mm", 1),
    receta_obj.add_variable(idx, "sdda_nivel_actual", 1),
    receta_obj.add_variable(idx, "sdda_vertical_mm", 1),
]

# Datos adicionales para las alarmas y máquina
#sector_IO = server.nodes.objects.add_object(idx, "sector_IO")
variables += [
    receta_obj.add_variable(idx, "estadoMaquina", 1),
]
#ciclo = server.nodes.objects.add_object(idx, "ciclo")
variables+= [
    receta_obj.add_variable(idx, "finalizado", True),
    receta_obj.add_variable(idx, "iniciado", True),
]
#desmoldeo = server.nodes.objects.add_object(idx, "desmoldeo")
variables+= [
    receta_obj.add_variable(idx, "cicloTiempoTotal", 1),
    receta_obj.add_variable(idx, "cicloTipoFin", 1),
    receta_obj.add_variable(idx, "desmoldeobanda",1)
]



def crear_variables_nulas(count=11):
    return []  # Lista vacía, pero con la intención de no superar `count`

server_interface_2 = server_interfaces.add_object(idx, "Server interface_2")
alarma = server_interface_2.add_object(idx, "Alarma")
config_obj = server_interface_2.add_object(idx, "Configuraciones")

receta_obj = server_interface_2.add_object(idx, "Receta")  # Se crea solo una vez
variablesReceta = [
    receta_obj.add_variable(idx, "NOMBRE", "RECETA MODIFICADA AA"),
    receta_obj.add_variable(idx, "NUMERO_DE_GRIPPER", 2),
    receta_obj.add_variable(idx, "TIPO_DE_MOLDE", "Tipo C"),
    receta_obj.add_variable(idx, "ANCHO_PRODUCTO", 4),
    receta_obj.add_variable(idx, "ALTO_DE_PRODUCTO", 5),
    receta_obj.add_variable(idx, "LARGO_DE_PRODUCTO", 6),
    receta_obj.add_variable(idx, "PESO_DEL_PRODUCTO", 7),
    receta_obj.add_variable(idx, "MOLDES_POR_NIVEL", 8),
    receta_obj.add_variable(idx, "ALTO_DE_MOLDE", 9),
    receta_obj.add_variable(idx, "LARGO_DE_MOLDE", 10),
    receta_obj.add_variable(idx, "ALTURA_AJUSTE", 11),
    receta_obj.add_variable(idx, "CANTIDAD_NIVELES", 12),
    receta_obj.add_variable(idx, "DELTA_ENTRE_NIVELES", 13),
    receta_obj.add_variable(idx, "ALTURA_N1", 14),
    receta_obj.add_variable(idx, "ALTURA_DE_BASTIDOR", 15),
    receta_obj.add_variable(idx, "ALTURA_AJUSTE_N1", 16),
    receta_obj.add_variable(idx, "torre_proxima", 1),
    receta_obj.add_variable(idx, "receta_proxima", 21),
]



receta_proxima = receta_obj.get_child(f"{idx}:receta_proxima")

def actualizar_receta():
    while True:
        nuevo_valor = random.randint(1, 25)
        receta_proxima.set_value(nuevo_valor)
        print(f"receta_proxima actualizado a: {nuevo_valor}")
        time.sleep(60)

thread = Thread(target=actualizar_receta, daemon=True)
thread.start()



nivelesHN = server_interface_2.add_object(idx, "DatosNivelesHN")  # Se crea solo una vez
variablesHN = [
    nivelesHN.add_variable(idx, "Correcion_hN1", "1"),
    nivelesHN.add_variable(idx, "Correcion_hN2", "2"),
    nivelesHN.add_variable(idx, "Correcion_hN3", "3"),
    nivelesHN.add_variable(idx, "Correcion_hN4", "4"),
    nivelesHN.add_variable(idx, "Correcion_hN5", "5"),
    nivelesHN.add_variable(idx, "Correcion_hN6", "6"),
    nivelesHN.add_variable(idx, "Correcion_hN7", "7"),
    nivelesHN.add_variable(idx, "Correcion_hN8", "8"),
    nivelesHN.add_variable(idx, "Correcion_hN9", "9"),
    nivelesHN.add_variable(idx, "Correcion_hN10", "10"),
    nivelesHN.add_variable(idx, "Correcion_hN11", "11"),
]

nivelesuHN = server_interface_2.add_object(idx, "DatosNivelesuHN")  # Se crea solo una vez
variablesUHN = [
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

nivelesChG = server_interface_2.add_object(idx, "DatosNivelesChG")  # Se crea solo una vez
variablesHG = [
    nivelesChG.add_variable(idx, "Correcion_hguardado_N1", "1"),
    nivelesChG.add_variable(idx, "Correcion_hguardado_N2", "2"),
    nivelesChG.add_variable(idx, "Correcion_hguardado_N3", "3"),
    nivelesChG.add_variable(idx, "Correcion_hguardado_N4", "4"),
    nivelesChG.add_variable(idx, "Correcion_hguardado_N5", "5"),
    nivelesChG.add_variable(idx, "Correcion_hguardado_N6", "6"),
    nivelesChG.add_variable(idx, "Correcion_hguardado_N7", "7"),
    nivelesChG.add_variable(idx, "Correcion_hguardado_N8", "8"),
    nivelesChG.add_variable(idx, "Correcion_hguardado_N9", "9"),
    nivelesChG.add_variable(idx, "Correcion_hguardado_N10", "10"),
    nivelesChG.add_variable(idx, "Correcion_hguardado_N11", "11"),
]

nivelesChB = server_interface_2.add_object(idx, "DatosNivelesChB")  # Se crea solo una vez
variablesCH8 = [
    nivelesChB.add_variable(idx, "Correcion_hbusqueda_N1", "1"),
    nivelesChB.add_variable(idx, "Correcion_hbusqueda_N2", "2"),
    nivelesChB.add_variable(idx, "Correcion_hbusqueda_N3", "3"),
    nivelesChB.add_variable(idx, "Correcion_hbusqueda_N4", "4"),
    nivelesChB.add_variable(idx, "Correcion_hbusqueda_N5", "5"),
    nivelesChB.add_variable(idx, "Correcion_hbusqueda_N6", "6"),
    nivelesChB.add_variable(idx, "Correcion_hbusqueda_N7", "7"),
    nivelesChB.add_variable(idx, "Correcion_hbusqueda_N8", "8"),
    nivelesChB.add_variable(idx, "Correcion_hbusqueda_N9", "9"),
    nivelesChB.add_variable(idx, "Correcion_hbusqueda_N10", "10"),
    nivelesChB.add_variable(idx, "Correcion_hbusqueda_N11", "11"),
]

nivelesFA = server_interface_2.add_object(idx, "DatosNivelesFA")  # Se crea solo una vez
variablesFA = [
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

DatosTorre = server_interface_2.add_object(idx, "DatosTorre")  # Se crea solo una vez
variablesTRR = [
    DatosTorre.add_variable(idx, "TAG", "Cuadrado"),
    DatosTorre.add_variable(idx, "Coreccion_hBastidor", 1),
    DatosTorre.add_variable(idx, "Coreccion_hAjuste", 2),
    DatosTorre.add_variable(idx, "Coreccion_hAjusteN1", 3),
    DatosTorre.add_variable(idx, "Coreccion_DisteNivel", 4),
]

for var in receta_obj.get_variables():
    var.set_writable()

for var in DatosTorre.get_variables():
    var.set_writable()

for var in nivelesHN.get_variables():
    var.set_writable()

for var in nivelesuHN.get_variables():
    var.set_writable()

for var in nivelesChG.get_variables():
    var.set_writable()

for var in nivelesChB.get_variables():
    var.set_writable()

for var in nivelesFA.get_variables():
    var.set_writable()
# Crear listas vacías con capacidad de hasta 11 elementos
max_variables = 11
DatosNivelesHN = config_obj.add_object(idx, "DatosNivelesHN")
variables_HN = crear_variables_nulas(max_variables)

DatosNivelesChB = config_obj.add_object(idx, "DatosNivelesChB")
variables_ChB = crear_variables_nulas(max_variables)

DatosNivelesChG = config_obj.add_object(idx, "DatosNivelesChG")
variables_ChG = crear_variables_nulas(max_variables)

DatosNivelesFallas = config_obj.add_object(idx, "DatosNivelesFallas")
variables_Fallas = crear_variables_nulas(max_variables)

DatosNivelesuHN = config_obj.add_object(idx, "DatosNivelesuHN")
variables_uHN = crear_variables_nulas(max_variables)

alarm_nodes = []
for i in range(0, 50):
    node = alarma.add_variable(idx, f"[{i}]", False)
    node.set_writable()
    alarm_nodes.append(node)

def update_group(start, end, update_interval, hold_time):
    while True:
        for i in range(start, end):
            # Activar el elemento
            alarm_nodes[i].set_value(True)
            #print(f"Elemento {i} activado en grupo {start}-{end}")
            time.sleep(hold_time)

            # Desactivar el elemento
            alarm_nodes[i].set_value(False)
            #print(f"Elemento {i} desactivado en grupo {start}-{end}")

            sleep_time = update_interval - hold_time
            if sleep_time < 0:
                sleep_time = 0  # Ajustar el tiempo de espera a 0 si es negativo
            
            time.sleep(sleep_time)
# Crear hilos para cada grupo
thread1 = threading.Thread(target=update_group, args=(0, 15, 15, 3))  # Primeros 15 elementos
thread2 = threading.Thread(target=update_group, args=(15, 35, 5, 10))  # Siguientes 20 elementos
thread3 = threading.Thread(target=update_group, args=(35, len(alarm_nodes), 5, 2))  
            
# Configurar todas las variables para que sean accesibles desde el cliente
for var in variables:
    var.set_writable()

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
        while nivel_actual <= random.randint(9, 11):  # El nivel va hasta 9, 10 o 11
            print(f"Procesando torre {torre_actual}, nivel {nivel_actual}")
            estado_maquina = 1
            ciclo_inicio = True
            # Actualizar los valores de los nodos durante el ciclo
            for var in variables:
                if var.get_browse_name().Name == "Nombre actual":
                    var.set_value(receta_nombre)
                elif var.get_browse_name().Name == "RecetaProximaDesmolde":
                    var.set_value((idReceta_actual % 7) + 1)
                elif var.get_browse_name().Name == "PesoProducto":
                    var.set_value(peso_producto)
                elif var.get_browse_name().Name == "NGripperActual":
                    var.set_value(gripper_actual)
                elif var.get_browse_name().Name == "NGripperProximo":
                    var.set_value(gripper_proximo)
                elif var.get_browse_name().Name == "torreActual":
                    var.set_value(torre_actual)
                elif var.get_browse_name().Name == "torreProxima":
                    var.set_value(torre_proxima)
                elif var.get_browse_name().Name == "sdda_nivel_actual":
                    var.set_value(nivel_actual)
                elif var.get_browse_name().Name == "estadoMaquina":
                    var.set_value(estado_maquina)
                elif var.get_browse_name().Name == "desmoldeoBanda":
                    var.set_value(desmoldeo_banda)
                elif var.get_browse_name().Name == "iniciado":
                    var.set_value(ciclo_inicio)
                elif var.get_browse_name().Name == "finalizado":
                    var.set_value(False)
                
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
        thread1.start()
        thread2.start()
        thread3.start()
        ciclo_de_desmoldeo()
        
    except KeyboardInterrupt:
        print("\nServidor detenido por el usuario.")
    finally:
        server.stop()
        print("Servidor OPC UA apagado.")
