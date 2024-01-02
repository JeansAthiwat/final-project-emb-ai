"""
API server endpoint for the web app
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """Render the HTML index home page."""
    return render_template("index.html")

@app.route("/emotionDetector")
def emotion_detector_route():
    """Endpoint to analyze emotion."""
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    if response is None:
        return "Invalid text! Please try again!"
    emotion_keys = ['anger', 'disgust', 'fear', 'joy', 'sadness']
    emotion_values = ', '.join(f"'{key}': {response.get(key, 0)}" for key in emotion_keys)
    dominant_emotion = response.get('dominant_emotion', 'N/A')
    return f"""For the given statement, the system response is:
    {emotion_values}. The dominant emotion is {dominant_emotion}."""

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
