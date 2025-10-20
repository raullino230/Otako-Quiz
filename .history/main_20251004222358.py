from flask import Flask, request, jsonify, render_template
from correct.dicionario import gabarito   # importa o dicionário

app = Flask(__name__)


#rotas

@app.route('/')
def index():
    return render_template('site.html')

@app.route("/verificar", methods=["POST"])
def verificar():
    data = request.json
    questao = data.get("questao")
    resposta = data.get("resposta")

    
    
  

#inialização

if __name__ == "__main__":
    app.run(debug=True)
