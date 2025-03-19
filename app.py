from flask import Flask, resquest

app = Flask(__name__)

import sqlite3

#python -m venv venv para criar o ambiente virtual
#venv/Scripts/activate para ativar o ambiente virtual
#pip install flask para instalar o flask
#python app.py para rodar o servidor
#ctrl + c para parar o servidor
#deactivate para desativar o ambiente virtual

"""
@app.route("/pagar")
def exibir_mensagem_pagar():
    return "<h1> Pagar as pessoas faz bem </h1>"

@app.route("/receber")
def exibir_mensagem_receber():
    return "<h2> Receber as pessoas faz bem </h2>"

@app.route("/comidas")
def exibir_mensagem_comidas():
    return "<h2> Tomate à milanesa </h2>"

"""
#criando a estrutura de banco de dados
def init_db():
    #sqlite3 crie o arquivo database.db e se conecte com a variável conn
    with sqlite3.connect("database.db") as conn:
        conn.execute("""
                CREATE TABLE IF NOT EXISTS LIVROS(
                     id INTEGER PRIMARY KEY AUTOINCREMENT
                     titulo TEXT NOT NULL,
                     categoria TEXT NOT NULL,
                     autor TEX NOT NULL,
                     imagem_url TEXT NOT NULL
                     )
    """)

init_db()

@app.route("/doar", methods=["POST"])
def doar():

    dados = request.get_json()
    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    imagem_url = dados.get("imagem_url")
    
#se o arquivo app.py for o arquivo prinpripal da nossa aplicação, rode a api no modo de depuração
if __name__ == "__main__":
    app.run(debug=True)