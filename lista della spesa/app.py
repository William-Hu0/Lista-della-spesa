from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

x="ciao"
lista=[1,2,3,4,5]
@app.route('/')
def home():
    return render_template('index.html', paperino=x, lista=lista)

@app.route('/aggiungi', methods=["POST"])
def aggiungi():
    elemento= request.form["elemento"]
    if elemento:
        lista.append(elemento)
    return redirect (url_for("home"))

@app.route('/rimuovi/<int:indice>', methods=['POST'])
def rimuovi(indice):
    if 0 <= indice < len(lista):
        lista.pop(indice)
    return redirect(url_for('home'))

@app.route('/svuota', methods=['POST'])
def svuota():
    lista.clear()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)