# 💻 Portfólio API

[![Python](https://img.shields.io/badge/Python-3.9-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.1.1-red)](https://flask.palletsprojects.com/en/2.1.x/)

Este é o lado back-end do meu portfólio pessoal (disponível em https://lukasverso.lukasrocha.repl.co/). Consiste em apenas uma função para receber uma requisição do front-end e enviar um e-mail para mim.

A requisição `POST /enviar-email` recebe no corpo (`body`) as seguintes especificações:
- `conteudo`: conteúdo do e-mail.
- `email`: e-mail (apenas para caso tenha necessidade de enviar uma resposta).
- `titulo`: título do e-mail.
  
*todos obrigatórios

A API foi desenvolvida usando Flask.

## Executando o projeto

1. Clone este repositório: `git clone https://github.com/lkscomk/portifolio-api.git`
2. Entre na pasta do projeto: `cd portifolio-api`
3. Instale as dependências: `pip install -r requirements.txt`
4. Execute o projeto: `python main.py`

## Observações

- É necessário informar as credenciais de envio de e-mail, para isso crie um arquivo `.env` e coloque `EMAIL=o_email_que_vai_enviar` e `
SENHA=senha_do_email`
- Lembre-se de atualizar o endpoint da requisição do front-end no arquivo `main.py` para o seu endereço de hospedagem.


![Logo do Python](https://www.python.org/static/community_logos/python-logo-generic.svg)

![Logo do Flask](https://flask.palletsprojects.com/en/2.1.x/_images/flask-logo.png)

Autor: LUKAS