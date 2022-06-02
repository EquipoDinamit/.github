var express = require('express');
var app = express();
var server = require('http').Server(app);

var clientesEmisores = [];

//static files
app.use("/",express.static('public'));
//app.use("/",express.static('public'));

//start server
server.listen(80, function(){
	console.log("Servidor corriendo en http://localhost:80");
});

const socketIo = require('socket.io');
const io = socketIo(server);

//websockets
io.on('connection', (socket)=>{

	socket.on('id', (id) => {
        console.log("ID cliente: ",id);
		io.emit('id', id);
		io.emit('idObjeto', socket.id);

		clientesEmisores.push(socket.id);
    });

	socket.on('msg', (msg) => {
        console.log(msg);
		io.emit('msg', msg);
    });

    socket.on('disconnect', function() {
      console.log('client disconnected');
      var index = clientesEmisores.indexOf(socket.id);
      clientesEmisores.splice(index,1);
     // console.log(clientesEmisores.length);
   });
	console.log('new connection', socket.id);
	//console.log(clientesEmisores.length);
})
