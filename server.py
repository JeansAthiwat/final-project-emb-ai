from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("__main__")

@app.route("/")
def home():
    '''Render the HTML index home page'''
    return  render_template()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)