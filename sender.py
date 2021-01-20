from vidstream import ScreenShareClient
import threading
''' Instalar e importar Libreria vidstream,
    importar threading'''


''' Entrgando la IP del Cliente'''
sender = ScreenShareClient('192.168.1.81', 9999)

''' Inicio Stream '''
sender.start_stream()

t = threading.Thread(target=sender.start_stream)
t.start()

''' Mientras condición no sea STOP no se apaga el stream '''

while input("") != 'STOP':
    continue

sender.stop_stream()