from flask import Flask, request, jsonify
from correct.dicionario import gabarito   # importa o dicionário

app = Flask(__name__)

@app.route("/verificar", methods=["POST"])
def verificar():
    data = request.json
    questao = data.get("questao")
    resposta = data.get("resposta")

    if questao not in gabarito:
        return jsonify({"status": "erro", "mensagem": "questao invalida"}), 400
    
    if resposta == gabarito[questao]:
        return jsonify({"status": "correto", "mensagem": "Está certa! Parabéns, vá para a próxima questão."})
    
    else:
        return jsonify({"status": "errado", "mensagem": "Está errado, tente de novo."})
    
if__name