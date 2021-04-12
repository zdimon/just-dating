"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.SocketConnection = void 0;
var io = require("socket.io");
var SocketConnection = /** @class */ (function () {
    function SocketConnection(url) {
        var _this = this;
        this.socket = io(url, { transports: ['websocket'] })
            .on('connect', function (connection) {
            _this.socket.emit('hello', { message: 'hello message' });
        });
    }
    return SocketConnection;
}());
exports.SocketConnection = SocketConnection;
