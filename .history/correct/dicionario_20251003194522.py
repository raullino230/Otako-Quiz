from flask import Flask, request, jsonify
from correct.dicionario import gabarito   # importa o dicionário

app = Flask(__name__)

@app.route("/verificar", methods=["POST"])
def verificar():
    data = request.json
    questao = data.get("questao")
    resposta = data.get("resposta")

    if questao