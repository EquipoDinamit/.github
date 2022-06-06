from cProfile import label
from concurrent.futures import thread
import socketio
import serial
from time import sleep
import serial.tools.list_ports
import tkinter.ttk as ttk
from tkinter import * 
import threading

ventana = Tk()
miFrame= Frame(ventana, width=300, height=200)
miFrame.pack()

comPort=StringVar()
uso=StringVar()
svr=StringVar()
lectura=int()


def serial_ports():
	"""
	Intenta abrir cada puerto de la lista y, si tiene éxito, lo agrega a la lista de puertos.
	:return: Una lista de puertos que están disponibles.
	"""
	ports = ['COM%s' % (i + 1) for i in range(20)]
	result = []
	for port in ports:
		try:
			s = serial.Serial(port)
			s.close()
			result.append(port)
		except (OSError, serial.SerialException):
			pass
	return result

def on_select(event=None):
	"""
	La función se llama cuando el usuario selecciona un nuevo puerto COM del menú desplegable.
	:param event: El evento que llamó a esta función
	"""
	COM = cb.get()
	#print(COM)

# Creación de un menú desplegable con los puertos serie disponibles.
cb = ttk.Combobox(miFrame, values=serial_ports(), width=19)
cb.place(x=78, y=10)
cb.bind('<<ComboboxSelected>>', on_select)

cuadroUsuario=Entry(miFrame, textvariable=uso, width=22)
cuadroUsuario.grid(row=1, column=1, padx=10, pady=10)

cuadroServidor=Entry(miFrame, textvariable=svr, width=22)
cuadroServidor.grid(row=2, column=1, padx=10, pady=10)

puertoLabel=Label(miFrame, text='Puerto')
puertoLabel.grid(row=0, column=0, sticky='e', padx=10, pady=10)

usuarioLabel=Label(miFrame, text='Usuario')
usuarioLabel.grid(row=1, column=0, sticky='e', padx=10, pady=10)

servidorLabel=Label(miFrame, text='Servidor')
servidorLabel.grid(row=2, column=0, sticky='e', padx=10, pady=10)

def codigoBoton():
	"""
	Lee el puerto serie, envía los datos al servidor y luego imprime los datos en la consola
	"""
	try:
		if (len(cb.get()) != 0) and (len(cuadroUsuario.get()) !=  0) and (len(cuadroServidor.get()) !=  0):
			comPort =cb.get()
			uso = cuadroUsuario.get()
			svr = cuadroServidor.get()
	except:
		print('Rectifica lo ingrsado')		
	cb['state']=DISABLED
	botonActualizar['state']=DISABLED
	cuadroUsuario['state']=DISABLED
	cuadroServidor['state']=DISABLED
	sio=socketio.Client()
	@sio.event
	def connect():
		print('Conexión establecida')
		sio.emit('id', 'emisor')
		sio.emit('name', uso)
	def send_msg(msg):
		sio.emit('msg', msg)
	@sio.event
	def disconnect():
		print('Desconectado del WebSocket')
	sio.connect(svr)
	# Configurando el portArduino al comPort y los baudios a 9600.
	portArduino = comPort
	baudios = 9600

	# Inicializando el puerto serie.
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
	
botonActualizar=Button(ventana, text='Conectar', command=codigoBoton)
botonActualizar.place(x=120, y=130)
#botonActualizar.pack()

ventana.title("Examen3")
ventana.call('wm','iconphoto', ventana._w, PhotoImage(file='logo.png'))
ventana.geometry("300x200")
ventana.mainloop()


