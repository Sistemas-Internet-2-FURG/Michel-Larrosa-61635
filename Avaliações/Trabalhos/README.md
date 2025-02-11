### Projeto Avaliado de Sistemas para Internet II – 2024
- Universidade Federal do Rio Grande 
- Centro de Ciências Computacionais
- Engenharia da Computação

#### Requisitos
* Primeira Fase:
1. Um sistema Web que contemple um CRUD de pelo menos duas tabelas com dependência de 1-N ou de N-N;
2. O sistema deve conter cadastro de usuário e senha e deve ter acesso restrito a usuário logado;
3. O sistema deve gerenciar a sessão do usuário através de cookies;
4. O sistema deve apresentar um front-end mínimo, sendo o foco o back end.
5. O sistema ~~pode~~ *deve* ser feito em ~~qualquer linguagem/framework, tendo como sugestão~~
Python/Flask;
6. Pode ser usado qualquer SGBD relacional, tendo como sugestão **PostgreSQL**

* Segunda Fase:
7. Todo o back end deve ser estruturado na forma de uma API construída
especificamente para este sistema;
8. O front end deve basicamente apresentar os dados e consumir os dados da API. Qualquer tecnologia front end pode ser usada, tendo como sugestão ~~JS puro~~ *REACT*;
9. A sessão deve ser feita através de tokens, JWT;
10. O modelo e a lógica do sistema pode permanecer a mesma.

#### Requisitos do Sistema
- Python:
	+ `python3`
	+ `python3-flask `(framework web)
	+ `python3-dotenv `(para proteger senhas)
	+ `python3-flask-sqlalchemy` (ORM)
	+ `python3-psycopg2 `(conexão flask-postgresql)
	+ `python3-flask-cors` (para aceitar requisições externas como API e REACT)
- PostgreSQL
- Node
	+ `apt-get install nodejs npm -y`
	+ `npm install create-react-app`
	+ `npm install web-vitals`
	+ `npm install http-proxy-middleware --save` (proxy)
	+ `npm install react-router-dom`
	+ `npm install bootstrap`
	+ `npm audit fix --force`
	+ `npx create-react-app`
	+ `npm start`

Configure o `package.json` do React para incluir o proxy:
```
{
  "proxy": "http://localhost:5000"
}
```
