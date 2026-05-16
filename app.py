
from flask import Flask, render_template, request
from emotion_detection import emotion_detector


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_route():
    user_text = request.args.get("textToAnalyze", "")
    if user_text:
        emotions = emotion_detector(user_text)
        return emotions
    return "No text provided"


if __name__ == "__main__":
    app.run(debug=True);