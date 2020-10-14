"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.SocketServer = void 0;
var SocketServer = /** @class */ (function () {
    function SocketServer(io) {
        io.on('connection', function (connection) {
            console.log(connection.id);
            connection.on('hello', function (data) {
                console.log(data);
                connection.emit('hello from server');
            });
        });
    }
    return SocketServer;
}());
exports.SocketServer = SocketServer;
