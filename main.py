from flask import Flask, request
from flask_restful import Resource, Api
from flask_mail import Mail, Message
from flask_cors import CORS
import os

email = os.environ.get('EMAIL')
senha = os.environ.get('SENHA')

app = Flask(__name__)
CORS(app)
api = Api(app)

# Configuração do Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = email
app.config['MAIL_PASSWORD'] = senha

mail = Mail(app)


class EnviarEmail(Resource):

  def post(self):
    email = request.json['email']
    if not email:
      return { 'mensagem': 'O parametro email é obrigatório.' }, 500
    conteudo = request.json['conteudo']
    if not conteudo:
      return { 'mensagem': 'O parametro conteudo é obrigatório.' }, 500
    titulo = request.json['titulo']
    if not titulo:
      return { 'mensagem': 'O parametro titulo é obrigatório.' }, 500

    msg = Message(titulo,
                  sender='storesumbrella@gmail.com',
                  recipients=[email])
    msg.body = conteudo
    mail.send(msg)

    return { 'mensagem': 'Email enviado com sucesso' }, 200


api.add_resource(EnviarEmail, '/enviar-email')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
