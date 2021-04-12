"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var SocketConnection_1 = require("./lib/SocketConnection");
var game_1 = require("./lib/game");
var React = require("react");
var ReactDOM = require("react-dom");
function App() {
    return (React.createElement("h1", null, "Hello from react!"));
}
ReactDOM.render(React.createElement(App, null), document.getElementById('react-app'));
console.log('Hello from ts!');
var game = new game_1.Game();
var socket = new SocketConnection_1.SocketConnection('ws://localhost:5000');
