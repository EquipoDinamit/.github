# Examen #2 Conexión Pagina Web
_Se realizo un Servidor que maneja el protocolo TCP y permite la conexión de un cliente emisor y uno receptor._
![tcpserver](https://github.com/DanielAtondo/Examen2/blob/main/Imagenes/Conexi%C3%B3nTCP.png "Diagrama del modelo TCP Cliente-Servidor")
## Configuración de los microcontroladores
* **Emisor:** 
  * Descargar el Archivo "CodigoEmisor.ino".
  * Abrir el archivo en el IDE de Arduino.
  * En la pestaña de Herramientas/Tools seleccionamos la Placa en la que se desea subir el codigo y tambien seleccionamos el Puerto al que este conectado el microocontrolador.
  * Darle al boton de "Subir/Upload".
* **Receptor:**
  * Descargar el Archivo "CodigoReceptor.ino".
  * Abrir el archivo en el IDE de Arduino.
  * En la pestaña de Herramientas/Tools seleccionamos la Placa en la que se desea subir el codigo y tambien seleccionamos el Puerto al que este conectado el microocontrolador.
  * Darle al boton de "Subir/Upload".
## Configuración del Servidor
En caso de tener un modem de INFINITUM ingresar a http://192.168.1.254/login.html y buscar el apartado "DMZ" (Demilitarized Zone ó Zona desmilitarizada) y activamos la función DMZ.<br>
Buscar el apartado "Mapeo de Puertos/Port Mapping" y una vez ahí en la sección "Reenvió de Puertos" definimos un puerto nuevo y especificamos que se trata de un Protocolo TCP.<br>
<strong>Nota:</strong> Es importante guardar los datos de la Dirección IP Pública.
## Circuitos
<ul>
 <li><strong>Emisor: </strong>Los materiales que se ocupan son una resistencia en el rango de 220&Omega; a 1k&Omega; y un Push Button.</li>
 <img src="https://github.com/DanielAtondo/Examen2/blob/main/Imagenes/CircuitoEmisor.png" alt="Circuito Emisor" style="height: 100%; width:100%;"/>
 <li><strong>Receptor: </strong>Los materiales que se ocupan son una resistencia en el rango de 220&Omega; a 1k&Omega; y un LED.</li>
 <img src="https://github.com/DanielAtondo/Examen2/blob/main/Imagenes/CircuitoReceptor.png" alt="Circuito Emisor" style="height: 100%; width:100%;"/>
</ul>
<h2>Instrucciones</h2>
<ul>
 <li>Instalar Python</li>
 <li>Instalar LABVIEW</li>
 <li>Instalar IDE Arduino</li>
 <li>Abrir el codigo con "Python"</li>
 <ul>
  <li>En caso de ser el Servidor abrimos el archivo "ServidorTCP.py" con Python.</li>
  <li>En caso de ser el Receptor abrimos el archivo "ClienteTCP.pu" con nuestro editor de codigo favorito modificamos el valor de la variable "puertoCOM" con el Puerto al que este conectado el arduino previamente cargado con el codigo del microcontrolador.</li>
  <li>En caso de ser el Emisor abrimos el VI "Emisor.vi" en el IDE Labview
 </ul>
</ul>
# Cosas Pendientes
actualizar la configuracion del micro para el emisor y el circuito del emisor
