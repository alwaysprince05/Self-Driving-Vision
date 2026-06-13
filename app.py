from flask import Flask, render_template, Response
from segmentation_model import load_segmentation_model
from video_processor import generate_frames
import os

app = Flask(__name__)

# Load model once at startup
model, class_names = load_segmentation_model()
VIDEO_PATH = "input_video.mp4"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(VIDEO_PATH, model, class_names),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
