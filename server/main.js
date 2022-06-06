/* Importación del módulo express y creación de una aplicación express. */
var express = require('express');
var app = express();
var server = require('http').Server(app);

/* Creando dos arrays, uno para los clientesEmisores y otro para los nombresUsuarios. */
var clientesEmisores = [];
var nombresUsuarios = [];

/* Diciéndole al servidor que use la carpeta pública como la carpeta raíz. */
app.use("/",express.static('public'));

/* Escuchando el puerto 80. */
server.listen(80, function(){
	console.log("Servidor corriendo en http://localhost:80");
});

/* Importando el módulo socket.io y luego creando un servidor socket.io. */
const socketIo = require('socket.io');
const io = socketIo(server);

//websockets
io.on('connection', (socket)=>{
    /* Escuchando el evento 'id' y luego emitiendo el evento 'id' a todos los clientes. */
    socket.on('id', (id) => {
      console.log("ID cliente: ",id);
      io.emit('id', id);
      clientesEmisores.push(socket.id);
    });
    /* Escuchando el evento de nombre y luego empujando el nombre a la matriz nombresUsuarios. */
    socket.on('name', (nombre) => {
        console.log("Usuario: ",nombre);
        io.emit('name', nombre);
        nombresUsuarios.push(nombre);
    });
    /* Escuchar el evento 'msg' y luego emitir el evento 'msg' a todos los clientes. */
    socket.on('msg', (msg) => {
		  io.emit('msg', msg);
    });
    /* Quitar el cliente de la matriz de clientes. */
    socket.on('disconnect', function() {
      console.log('client disconnected');
      var index = clientesEmisores.indexOf(socket.id);
      clientesEmisores.splice(index,1);
      //io.emit('borrar',index);
      nombresUsuarios.splice(index,1);
   });
})