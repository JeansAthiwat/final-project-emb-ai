from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("__name__")

@app.route("/")
def home():
    '''Render the HTML index home page'''
    return render_template("index.html")

@app.route("/emotionDetector")
def emotionDetector():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    
    if response:
        anger = response['anger']
        disgust = response['disgust']
        fear = response['fear']
        joy = response['joy']
        sadness = response['sadness']
        dominant_emotion = response['dominant_emotion']

        return f"""For the given statement, the system response is: 
        'anger': {anger}, 
        'disgust': {disgust}, 
        'fear': {fear}, 
        'joy': {joy},
        'sadness': {sadness}.
        The dominant emotion is {dominant_emotion}."""
    
    else:
        return "Error processing the request."


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)