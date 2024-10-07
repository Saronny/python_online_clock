import os
from flask import Flask, render_template
from flask_socketio import SocketIO
import favicon
import datetime

app = Flask(__name__)
sock = SocketIO(app)

# Global variable to store active connections
clients = set()

@app.route('/')
def index():
    return render_template('index.html')

@sock.on('connect')
def handle_connect():
    print('Client connected')
    clients.add(sock)

@sock.on('disconnect')
def handle_disconnect():
    print('Client disconnected')
    clients.remove(sock)

def background_time_update():
    while True:
        # Broadcast time updates to all connected clients
        sock.emit('update', {'time': datetime.datetime.now().isoformat()})
        sock.sleep(1)  # Non-blocking sleep provided by Flask-SocketIO

# Start the background task
sock.start_background_task(target=background_time_update)

def checkFavoriteIcon():
    try:
        with open('static', 'r') as f:
            pass
    except FileNotFoundError:
        print("Static folder not found, creating new one")
        os.mkdir('static')
    try:
        with open('static/favicon.ico', 'rb') as f:
            pass
    except FileNotFoundError:
        print("Favicon not found, creating new one")
        favicon.create_favicon()

if __name__ == '__main__':
    checkFavoriteIcon()
    sock.run(app)
