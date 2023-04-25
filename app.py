'''
Carregue a extensão no Google Chrome. Para fazer isso, 
acesse chrome://extensions/ na barra de endereços do navegador, 
ative o modo de desenvolvedor e clique em "Carregar sem compactação". 
Selecione a pasta do projeto criada na Etapa


Após carregar a extensão do Google Chrome feita em Flask, 
abra uma página da web no navegador e clique no ícone da extensão na barra 
de ferramentas do Chrome. A página da extensão será aberta e exibirá a 
mensagem "A URL da página atual é:" seguida da URL da página que você está 
visualizando.

'''

import requests
from flask import Flask, request, render_template

global vez
vez = 0
global dados_recebidos

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    url = request.args.get('url')
    requests.post("http://192.168.0.24:8000/", data = url)
    nota_fake = dados_recebidos
    nota_true = dados_recebidos
    result = "fake"
    return render_template('teste.html', nota_fake=nota_fake, nota_true=nota_true, result=result)

@app.route('/resultados', methods=['GET'])
def resultados():
    return render_template("paginaResult.html")

@app.route('/upload', methods=['POST'])
def upload():
    global vez
    if vez == 0:
        arquivo = request.files['paginaResult']
        nome_do_arquivo = arquivo.name
        arquivo.save(f"templates\\{nome_do_arquivo}.html")
        vez += 1
    if vez == 1:
        arquivo = request.files['imagemResult']
        nome_do_arquivo = arquivo.name
        arquivo.save(f"templates\\{nome_do_arquivo}.png")
        vez = 0
    return print("Arquivo recebida com sucesso")

@app.route("/data", methods=['POST'])
def dados():
    global dados_recebidos
    dados_recebidos = request.get_data()
    dados_recebidos = str(dados_recebidos)[2:-1]
    dados_recebidos = float(dados_recebidos)*100
    dados_recebidos = round(dados_recebidos, 2)
    print(dados_recebidos)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
