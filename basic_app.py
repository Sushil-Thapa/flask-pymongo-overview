from flask import Flask
app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def index():
    return "<h1>Hello World.</h1>"

@app.route("/predict", methods=['POST'])
def predict(image):
    result = predict_image(image)
    return jsonify(result),

if __name__ == '__main__':
    app.run()