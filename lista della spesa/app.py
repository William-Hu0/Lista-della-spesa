from flask import Flask, render_template

app = Flask(__name__)

x="ciao"
lista=[1,2,3,4,5]
@app.route('/')
def home():
    return render_template('index.html', paperino=x, lista=lista)

if __name__ == '__main__':
    app.run(debug=True)