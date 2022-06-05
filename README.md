# Examen #3 Examen Práctico (Editando...)
_Por medio de hardware realizar acciones en una página web utilizando un servidor con WebSockets._

![tcpserver](https://github.com/EquipoDinamit/Examen3/blob/main/imagenes/indicaciones.png "Diagrama del modelo TCP Cliente-Servidor")

El sistema se compone de tres módulos o bloques independientes que interactúan entre sí. Dos de los tres módulos son clientes, un cliente emisor (controlado por hardware), un cliente receptor (página web con html) y el servidor que permite la comunicación entre los dos clientes para que sea posible mover objetos o realizar diferentes acciones en la página web con la información que envía el emisor.

# Cliente emisor

### Circuito
Los materiales que se utilizaron son: <br>
<ul>
 <li>Arduino uno.</li>
 <li>8 resistenciias de 1k ohms.</li>
 <li>1 Protoboard.</li>
 <li>Push buttos.</li>
</ul>

A continuacion armar el circuito de la imagen.

<img src="https://github.com/EquipoDinamit/Examen3/blob/main/imagenes/Circuito%20emisor.png" alt="Circuito Emisor" style="height: 100%; width:100%;"/>

Los botones tienen asignados los números del 1 al 7 de izquierda a derecha.

### Código

<strong>Emisor.ino:</strong> 
<ul>
 <li>Descargar el Archivo "CodigoEmisor.ino".</li>
 <li>Abrir el archivo en el IDE de Arduino.</li>
 <li>En la pestaña de Herramientas/Tools seleccionamos la Placa en la que se desea subir el codigo y tambien seleccionamos el Puerto al que este conectado el microocontrolador.</li>
 <li>Darle al boton de "Subir/Upload".</li>
</ul>

Lo que se espera del código "CodigoEmisor.ino" es que cada botón nos regrese un valor del 1 al 7 que será leído por el código "ClienteEmisor.py" y enviado al servidor. 

<strong>ClienteEmisor.py: (Instrucciones del codigo de python)</strong>


# Servidor
(Explicacion del servidor)<br>
En caso de tener un modem de INFINITUM ingresar a http://192.168.1.254/login.html y buscar el apartado "DMZ" (Demilitarized Zone ó Zona desmilitarizada) y activamos la función DMZ.<br>
Buscar el apartado "Mapeo de Puertos/Port Mapping" y una vez ahí en la sección "Reenvió de Puertos" definimos un puerto nuevo y especificamos que se trata de un Protocolo TCP.<br>
<strong>Nota:</strong> Es importante guardar los datos de la Dirección IP Pública.

# Cliente receptor 
(Explicacion del html)

## Instrucciones 
(Instrucciones para ejecutar el sistema)
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
