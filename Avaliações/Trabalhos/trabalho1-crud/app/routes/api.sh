# testes de rotas da API

dominio="http://127.0.0.1:5000";
# -i , -include, inclui cabeçaho para análise
# -I , -head, somente o cabeçaho para análise
# -H , "campo: valor", adicionar/editar campos do cabeçalho
# -d payload de dados (POST)
# -X , request, verbo da requisição (POST, GET, PUT, PATCH, DELETE)
#

# ### ### ### ### ### ### EQUIPE ### ### ### ### ### ###

# ### POST
curl -X "POST" "http://127.0.0.1:5000/v1/turma/" -H "Content-Type:application/json" -d '{"identificador":"2208","disciplina":"Calculo Diferencal","professor":"3"}'


# ### GET
curl -X "GET" $dominio"/v1/turmas/"
#
curl -X "GET" $dominio"/v1/turmas/2105"


# ### PUT
curl -X "PUT" $dominio"/v1/turma/" -H "Content-Type:application/json" -d '{"identificador":"2208","disciplina":"Fisica Geral 2","professor":"4"}'


# ### PATCH
curl -X "PATCH" $dominio"/v1/turma/" -H "Content-Type:application/json" -d '{"identificador":"2208","professor":"1"}'
#
curl -X "PATCH" $dominio"/v1/turma/" -H "Content-Type:application/json" -d '{"identificador":"2208","disciplina":"Sistemas Inteligentes"}'


# ### DELETE
curl -X "DELETE" $dominio"/v1/turma/"  -H "Content-Type:application/json" -d '{"identificador":"1103"}'
#


# ### ### ### ### ### ### EQUIPE ### ### ### ### ### ###

# ### POST
curl -X "POST" "http://127.0.0.1:5000/v1/equipe/" -H "Content-Type:application/json" -d '{"matricula":"12345","nome":"Amarildo","cargo":"PÚBLCO"}'
curl -X "POST" "http://127.0.0.1:5000/v1/equipe/" -H "Content-Type:application/json" -d '{"matricula":"12345","nome":"Amarildo","cargo":"PÚBLCO","senha":"5"}'


# ### GET
curl -X "GET" $dominio"/v1/equipes/"
#
curl -X "GET" $dominio"/v1/equipes/12345"


# ### PUT
curl -X "PUT" $dominio"/v1/equipe/" -H "Content-Type:application/json" -d '{"matricula":"12345","nome":"Zilmar","cargo":"1101","senha":"555238764_xzy"}'


# ### PATCH
curl -X "PATCH" $dominio"/v1/equipe/" -H "Content-Type:application/json" -d '{"matricula":"12345","cargo":"PÚBLCO"}'

curl -X "PATCH" $dominio"/v1/equipe/" -H "Content-Type:application/json" -d '{"matricula":"12345","nome":"Zilmar","cargo":"PÚBLCO","senha":"5"}'
#
curl -X "PATCH" $dominio"/v1/equipe/" -H "Content-Type:application/json" -d '{"matricula":"12345","nome":"Zilmar","cargo":"1101"}'
#
curl -X "PATCH" $dominio"/v1/equipe/" -H "Content-Type:application/json" -d '{"matricula":"12345","nome":"Zilmar","senha":"5"}'
#
curl -X "PATCH" $dominio"/v1/equipe/" -H "Content-Type:application/json" -d '{"matricula":"12345","cargo":"1101","senha":"5"}'


# ### DELETE
curl -X "DELETE" $dominio"/v1/equipe/"  -H "Content-Type:application/json" -d '{"matricula":"12345"}'
#


# ### ### ### ### ### ### ALUNOS ### ### ### ### ### ###

# ### POST
curl -X "POST" "http://127.0.0.1:5000/v1/aluno/" -H "Content-Type:application/json" -d '{"matricula":"12345","nome":"Amarildo"}'
curl -X "POST" "http://127.0.0.1:5000/v1/aluno/" -H "Content-Type:application/json" -d '{"matricula":"12345","nome":"Amarildo","turma":"1101","nota":"5"}'


# ### GET
curl -X "GET" $dominio"/v1/alunos/"
#
curl -X "GET" $dominio"/v1/alunos/12345"


# ### PUT
curl -X "PUT" $dominio"/v1/aluno/" -H "Content-Type:application/json" -d '{"matricula":"12345","nome":"Zilmar","turma":"1101","nota":"5"}'


# ### PATCH
curl -X "PATCH" $dominio"/v1/aluno/" -H "Content-Type:application/json" -d '{"matricula":"12345","nome":"Zilmar","turma":"1101","nota":"5"}'
#
curl -X "PATCH" $dominio"/v1/aluno/" -H "Content-Type:application/json" -d '{"matricula":"12345","nome":"Zilmar","turma":"1101"}'
#
curl -X "PATCH" $dominio"/v1/aluno/" -H "Content-Type:application/json" -d '{"matricula":"12345","nome":"Zilmar","nota":"5"}'
#
curl -X "PATCH" $dominio"/v1/aluno/" -H "Content-Type:application/json" -d '{"matricula":"12345","turma":"1101","nota":"5"}'


# ### DELETE
curl -X "DELETE" $dominio"/v1/aluno/"  -H "Content-Type:application/json" -d '{"matricula":"12345"}'
#

