import pickle
from flask import Flask, render_template, request

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    temperature = float(request.form['temperature'])
    prediction = model.predict([[temperature]])[0]
    output = round(prediction, 2)
    return render_template('index.html', prediction=f'Total revenue generated is Rs. {output}')

if __name__ == '__main__':
    app.run()

