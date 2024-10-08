from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Avaliação contínua: Aula 030</h1><ul><li><a href="/">Home</a></li><li><a href="/user/Fabio%20Teixeira/PT23820X/IFSP">Identificação</a></li><li><a href="/contextorequisicao">Contexto da requisição</a></li></ul>'

@app.route('/user/<name>/<register>/<institution>')
def user(name, register, institution):
    return '<h1>Avaliação contínua: Aula 030</h1><h2>Aluno: {}</h2><h2>Prontuário: {}</h2><h2>Instituição: {}</h2><a href="/">Voltar</a>'.format(name, register, institution)

@app.route('/contextorequisicao')
def contexto_requisicao():
    user_agent = request.headers.get('User-Agent')
    ip = request.remote_addr
    host = request.headers.get('Host')
    return '<h1>Avaliação contínua: Aula 030</h1><h2>Seu navegador é: {}</h2><h2>O IP do cumputador remoto é: {}</h2><h2>O host da aplicação é: {}</h2><a href="/">Voltar</a>'.format(user_agent, ip, host)