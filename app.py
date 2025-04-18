from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/parcours')
def parcours():
    return render_template('parcours.html')

@app.route('/projets')
def projets():
    return render_template('projets.html')

if __name__ == '__main__':
    app.run(debug=True)
