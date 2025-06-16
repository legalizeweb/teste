from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    erro = None

    if request.method == "POST":
        try:
            numero = float(request.form["numero"])
            if numero < 0:
                erro = "Número não pode ser negativo."
            else:
                resultado = math.sqrt(numero)
        except ValueError:
            erro = "Entrada inválida. Digite um número válido."

    return render_template("index.html", resultado=resultado, erro=erro)

if __name__ == "__main__":
    app.run(debug=True)
