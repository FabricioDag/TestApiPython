import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
  return "A api está no ar"

@app.route('/data')
def datavendas():
  tabela = pd.read_csv('Advertising.csv')
  total_vendas = tabela['Vendas'].sum()
  resposta = {'total_vendas':total_vendas}
  return jsonify(resposta)




app.run(host='0.0.0.0')