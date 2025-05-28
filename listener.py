from flask import Flask
import winsound
import threading

app = Flask(__name__)

def play_alarm():
    for _ in range(5):
        winsound.Beep(1000, 500)

@app.route('/trigger_alarm')
def trigger_alarm():
    threading.Thread(target=play_alarm).start()
    return 'Alarm triggered!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
