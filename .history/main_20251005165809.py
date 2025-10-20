from flask import Flask, request, jsonify, render_template
from correct.dicionario import gabarito   # importa o dicionário

app = Flask(__name__)


#rotas

@app.route('/')
def index():
    return render_template('tempsite.html')

@app.route("/verificar", methods=["POST"])
def verificar():
    data = request.json
    questao = data.get("questao")
    resposta = data.get("resposta")

    if gabarito.get(questao) == resposta:
        return jsonify({"status": "correto", "mensagem": "Está certa! Parabéns, vá para a próxima questão."})
    else:
        return jsonify({"status": "errado", "mensagem": "Está errado! Tente novamente."}) 
    
  

#inialização

if __name__ == "__main__":
    app.run(debug=True)
