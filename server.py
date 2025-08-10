"""Flask app to expose Watson Emotion Detection via /emotionDetector."""
from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """Render the home page with the input form."""
    return render_template("index.html")

@app.route("/emotionDetector")
def call_emotion_detector():
    """Run emotion detection on the query parameter 'textToAnalyze' and format the response.

    Returns:
        str: Formatted emotions summary, or an error message for blank/invalid input.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")
    result = emotion_detector(text_to_analyze)

    if not text_to_analyze or result.get("dominant_emotion") is None:
        return "Invalid text! Please Try again"

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
