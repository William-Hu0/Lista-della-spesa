from flask import Flask, render_template

app = Flask(__name__)

x="ciao"

@app.route('/')
def home():
    return render_template('index.html', paperino=x)

if __name__ == '__main__':
    app.run(debug=True)