import socketio
import serial
from time import sleep

sio=socketio.Client()
@sio.event
def connect():
	print('Conexión establecida')
def send_msg(msg):
	sio.emit('msg', msg)
@sio.event
def disconnect():
	print('Desconectado del WebSocket')
sio.connect('http://josuegregorio.duckdns.org/')

#Parametros para la configuracion de arduino
portArduino = 'COM6'
baudios = 9600

#Se crea el objeto arduino asginandole el puerto COM y la velocidad en baudios
try:
	arduino = serial.Serial(portArduino, baudios)
except:
	print('Cannot conect to the port')

#El siguiente ciclo While repite la lectura de arduino y lo envia 
#al servidor, ademas recibe el mensaje del servidor 
while True:
	#Realiza la lectura de arduino
	lectura = arduino.readline().decode(encoding="ascii", errors="ignore")
	send_msg(lectura)
	print(lectura)
	sleep(0.1)
	#Finaliza la conexion a arduino
sio.disconnect()