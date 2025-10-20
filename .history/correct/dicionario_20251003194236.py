from flask import Flask, request, jsonify
from correct.dicionario import gabarito   # importa o dicionário

app = Flask(__name__)

@app