import sqlite3
from flask import Flask, request, jsonify
from flask_cors import CORS

"""
DONNT FORGET ATIVAR O AMBIENTE VIRTUAL!!!
python -m venv venv para criar o ambiente virtual
.venv\Scripts\activate.ps1 para ativar o ambiente virtual
pip install flask para instalar o flask
python app.py para rodar o servidor
deactivate para desativar o ambiente virtual
"""


# criando a aplicação flask
app = Flask(__name__)
CORS(app)  # habilitando o CORS para a aplicação

@app.route("/")
def menu_inicial():
    return "<h1>Biblioteca Vai na Web!</h1>"

# criando a estrutura do banco de dados
def init_db():
    with sqlite3.connect("database.db") as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS LIVROS(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                categoria TEXT NOT NULL,
                autor TEXT NOT NULL,
                image_url TEXT NOT NULL
            )"""
        )


# inicializando o banco de dados
init_db()


# Meu endpoint da atividade lá atrás
@app.route("/quero-doar", methods=["POST"])
def doar():
    # recebendo os dados do enviados pelo cliente
    dados = request.get_json()

    titulo = dados.get("titulo")
    categoria = dados.get("categoria")
    autor = dados.get("autor")
    image_url = dados.get("image_url")

    if not titulo or not categoria or not autor or not image_url:
        # retornando uma mensagem de erro caso algum campo esteja vazio
        return jsonify({"erro": "Todos os campos são obrigatórios"}), 400

    # abrindo a conexão com o banco de dados
    with sqlite3.connect("database.db") as conn:
        conn.execute(f"""
            INSERT INTO LIVROS (titulo, categoria, autor, image_url) 
            VALUES("{titulo}","{categoria}","{autor}","{image_url}")
            """
        )
        conn.commit()  # salvando as alterações no banco de dados
    return jsonify({"Mensagem": "Livro cadastrado com sucesso!"}), 201


# Livros cadastrados
@app.route("/livro-doados", methods=["GET"])
def livros():
    with sqlite3.connect("database.db") as conn:
        livros = conn.execute("SELECT * FROM LIVROS").fetchall()

        livros_formatados = []  # lista para armazenar os livros formatados

        for item in livros:
            # criando um dicionário para os livros
            dicionario_livro = {
                "id": item[0],
                "titulo": item[1],
                "categoria": item[2],
                "autor": item[3],
                "image_url": item[4],
            }

            livros_formatados.append(dicionario_livro)

        return jsonify(livros_formatados), 200


if __name__ == "__main__":
    app.run(debug=True)