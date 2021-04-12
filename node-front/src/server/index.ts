import { SocketServer } from './lib/SocketServer';

var express = require('express');
const app = require('express')();
const server = require('http').createServer(app);
const io = require('socket.io')(server, {});
const ws = new SocketServer(io);
var http = require('http');

app.use(express.static('.'));


// livereload  
const livereload = require("livereload");
const liveReloadServer = livereload.createServer();
liveReloadServer.watch(__dirname, '/../../src');      
const connectLivereload = require("connect-livereload");

liveReloadServer.server.once("connection", () => {
    setTimeout(() => {
      liveReloadServer.refresh("/");
    }, 1000);
  }); 

app.use(connectLivereload());

app.set('views', __dirname + '/../../src/server/tpl');
app.engine('html', require('swig').renderFile);
app.use("/", function(request, response){
  var options = {
    host: 'localhost',
    port: 7777,
    path: '/v1/account/user_list'
  };
  http.request(options, (res) => {
    
    res.on('data', d => {
      let data = JSON.parse(d);
      return response.render("index.html",{users: data.payload});
    })
    
  }).end();
      
});





server.listen(5000, () => {
    console.log('Listening 5000 port' )
});