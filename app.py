from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# ===============================
# CARREGAR MODELO E DADOS
# ===============================
model = joblib.load("modelo.pkl")
df_final = pd.read_csv("df_final.csv")

# ===============================
# FUNÇÃO DE PREVISÃO
# ===============================
def prever(codigo=None, nome=None):

    if codigo:
        df = df_final[df_final["codigo"] == int(codigo)]
    elif nome:
        df = df_final[df_final["produto"].str.contains(nome, case=False, na=False)]
    else:
        return []

    resultados = []

    for _, row in df.iterrows():
        consumo_2024 = row["consumo_2024"]

        previsao = float(model.predict([[consumo_2024]])[0])

        resultados.append({
            "codigo": row["codigo"],
            "produto": row["produto"],
            "previsao": round(previsao, 2)
        })

    return resultados

# ===============================
# ROTA PRINCIPAL
# ===============================
@app.route("/", methods=["GET", "POST"])
def index():
    resultados = []

    if request.method == "POST":
        codigo = request.form.get("codigo")
        nome = request.form.get("nome")

        resultados = prever(codigo, nome)

    return render_template("index.html", resultados=resultados)

# ===============================
# RODAR SERVIDOR
# ===============================
if __name__ == "__main__":
    app.run(debug=True)