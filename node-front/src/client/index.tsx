import { SocketConnection } from './lib/SocketConnection';
import { Game } from './lib/game';
import * as React from "react";
import * as ReactDOM from 'react-dom';

function App() {
    return (
      <h1>Hello from react!</h1>
    );
}

ReactDOM.render(
    <App />,
    document.getElementById('react-app')
  );





console.log('Hello from ts!');

var game = new Game();
var socket = new SocketConnection('ws://localhost:5000');