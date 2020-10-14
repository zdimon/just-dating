export class SocketServer {
    constructor(io: any) {
        io.on('connection', (connection) => {
            console.log(connection.id);
            connection.on('hello',(data) => {
                console.log(data);
                connection.emit('hello from server');
            });
        });
    }
}