from flask import Flask, render_template, Response
from camera import Camera
import time

previousTime=time.time()
wait=1
currentTime=None
count=0
app = Flask(__name__)
@app.route('/')

def index():
    return render_template('stream.html')
def gen(camera):
    global count
    global previousTime
    global currentTime
    while True:
        currentTime=time.time()
        if currentTime-previousTime>=1:
            count=count+1
            previousTime=currentTime
        frame = camera.get_frame(count)
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()), mimetype='multipart/x-mixed-replace; boundary=frame')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

