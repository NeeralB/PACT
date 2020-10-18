from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():    
    msg1 = ''
    import speech_recognition
    import time
    import string
    for i in range(1):
        recognizer = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            print("Say Something")
            audio = recognizer.listen(source)

        time.sleep(0.2)
        print("Google Speech Recognition thinks you said:")
        time.sleep(0.1)

        msg1 = (recognizer.recognize_google(audio))
        print(msg1)
            
    colorslist = ["black"]
    words = msg1.split(" ")
    newarray = []
    for word in words:
        if word.lower() in colorslist:
            newarray.append(word)
    print(newarray)


    return render_template("heatmaps.html")

@app.route('/results', methods=['POST'])
def results():


    return render_template('home_form copy.html')

@app.route('/covid', methods = ['POST'])
def covid():
    return render_template('home_formcopy.html')

if __name__ == "__main__":
    app.run(port=5000, debug=True)