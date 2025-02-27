''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    ''' This function returns the output of the emotion_detector
    function to the Flask app
    '''
    text_to_analyze = request.args.get('textToAnalyze')

    response = emotion_detector(str(text_to_analyze))

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return response

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
    page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
