from vidstream import StreamingServer
import threading
''' Instalar e importar Libreria vidstream '''

''' Entrgando la IP del Server'''
receiver = StreamingServer('192.168.1.81', 9999)

''' Guardo e Inicializo el SV'''

t = threading.Thread(target=receiver.start_server)
t.start()

''' Mientras condición no sea STOP no se apaga el stream '''

while input("") != 'STOP':
    continue

receiver.stop.server()