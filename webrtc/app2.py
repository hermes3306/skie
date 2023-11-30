from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('video_call.html')

@socketio.on('join')
def handle_join(data):
    socketio.emit('join', data)

@socketio.on('offer')
def handle_offer(data):
    socketio.emit('offer', data)

@socketio.on('answer')
def handle_answer(data):
    socketio.emit('answer', data)

@socketio.on('ice-candidate')
def handle_ice_candidate(data):
    socketio.emit('ice-candidate', data)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)


