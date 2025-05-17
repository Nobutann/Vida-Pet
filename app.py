from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")

def tela_inicial():
    return render_template("index.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/adicionar", methods=["GET", "POST"])
def adicionar():
    if request.method == "POST":
        pets = {
        "Nome": request.form.get("nome"),
        "Espécie": request.form.get("especie"),
        "Raça": request.form.get("raca"),
        "Data de nascimento": request.form.get("data_nascimento"),
        "Peso": request.form.get("peso")
        }
        
        with open("dados pet.txt", 'a', encoding="utf-8") as file:
            for key, value in pets.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")

        return redirect(url_for("menu"))
    
    return render_template("adicionar.html")

if __name__ == "__main__":
    app.run(debug=True)