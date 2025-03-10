from flask import Flask

app = Flask(__name__)

#python -m venv venv para criar o ambiente virtual
#venv\Scripts\activate para ativar o ambiente virtual
#pip install flask para instalar o flask
#python app.py para rodar o servidor
#ctrl + c para parar o servidor
#deactivate para desativar o ambiente virtual

@app.route("/pagar")
def exibir_mensagem_pagar():
    return "<h1> Pagar as pessoas faz bem </h1>"

@app.route("/receber")
def exibir_mensagem_receber():
    return "<h2> Receber as pessoas faz bem </h2>"

@app.route("/comidas")
def exibir_mensagem_comidas():
    return "<h2> Tomate à milanesa </h2>"

#se o arquivo app.py for o arquivo prinpripal da nossa aplicação, rode a api no modo de depuração
if __name__ == "__main__":
    app.run(debug=True)
