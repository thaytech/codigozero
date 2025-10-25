from flask import Flask, request, render_template

app = Flask(__name__)

@app.route ("/", methods = ["GET", "POST"])
def index(): 
    resultado = None 

    if request.method == "POST":
        try: 
            v1 = float(request.form.get("valor1", 0))
            v2 = float (request.form.get("valor2", 0))
            operacao = request.form.get("operacao")

            if operacao == "soma":
                resultado = v1 + v2

            elif operacao == "subtrair":
                resultado = v1 - v2

            elif operacao == "multiplicar":
                resultado = v1 * v2

            elif operacao == "dividir":
                if v2 == 0:
                    resultado = "Erro: divisão por zero"
                else:
                    resultado = v1/v2

        except ValueError:
            resultado = "Erro: digite apenas números"

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug = True)