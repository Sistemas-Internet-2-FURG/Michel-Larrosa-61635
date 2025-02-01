from flask import Blueprint, jsonify, request
from app.models import check_db_connection
from models.alunos import *
from models.equipe import *
from models.turmas import *
api = Blueprint('api', __name__)

# ### ### ROTAS PARA SOLICITAR/INSERIR DADOS ### ### ROTAS API ### ### ### ### ### ### ###

# ### NOVAS ROTAS TURMA ### ### ### ### ### ### ### ###

@api.route('/v1/turma/', methods=['POST',"PUT","PATCH", "DELETE"])
def turma_api():
    if not (request.json.get('identificador')):
        # return request.son;
        return {"Bad Request": "Falta IDENTIFICADOR"}, 400
    identificador = request.json.get('identificador')

    match request.method:
        case "POST":
            if not (request.json.get('disciplina') and request.json.get('professor')):
                return {"Bad Request": "Faltam dados completos {Identificador, Disclna e Professor}"}, 400
            disciplina = request.json.get('disciplina')
            professor = request.json.get('professor')
            inserido = inserir_turma(identificador, disciplina, professor)
            return inserido
        case "PUT":
            if not ( request.json.get('disciplina') and request.json.get('professor')):
                return {"Bad Request": "Todos os campos devem ser fornecidos para PUT"}, 400
            disciplina = request.json.get('disciplina')
            professor = request.json.get('professor')
            editado = editar_turma(identificador, disciplina, professor)
            return editado
        case "PATCH":
            if not ( request.json.get('disciplina') or request.json.get('senha') or request.json.get('professor')):
                return {"Bad Request": "Pelo menos um campo opcional deve ser fornecido para PATCH"}, 400
            if not request.json.get('disciplina'):
                disciplina = False
            else:
                disciplina = request.json.get('disciplina')
            if not request.json.get('professor'):
                professor = False
            else:
                professor = request.json.get('professor')
            editado = editar_parcialmente_turma(identificador, disciplina, professor)
            return editado
        case "DELETE":
            deletado = delete_turma(request.json.get('identificador'))
            return deletado


@api.route('/v1/turmas/', methods=['GET'])
def obter_turmas_api():
    turmas = obter_turmas()
    return turmas


@api.route('/v1/turmas/<int:identificador>', methods=['GET'])
def obter_turma_api(identificador):
    turma_obtido = ler_turma(str(identificador))
    return turma_obtido

# ### NOVAS ROTAS EQUIPE ### ### ### ### ### ### ### ###

@api.route('/v1/equipe/', methods=['POST',"PUT","PATCH", "DELETE"])
def equipe_api():
    if not (request.json.get('matricula')):
        # return request.son;
        return {"Bad Request": "Falta MATRICULA"}, 400
    matricula = request.json.get('matricula')

    match request.method:
        case "POST":
            if not (request.json.get('nome')):
                return {"Bad Request": "Faltam dados completos {Matrícula e Nome}"}, 400
            nome = request.json.get('nome')
            inserido = inserir_equipe(matricula, nome)
            return inserido
        case "PUT":
            if not ( request.json.get('nome') and request.json.get('senha') and request.json.get('cargo')):
                return {"Bad Request": "Todos os campos devem ser fornecidos para PUT"}, 400
            nome = request.json.get('nome')
            senha = request.json.get('senha')
            cargo = request.json.get('cargo')
            editado = editar_equipe(matricula, nome, cargo, senha)
            return editado
        case "PATCH":
            if not ( request.json.get('nome') or request.json.get('senha') or request.json.get('cargo')):
                return {"Bad Request": "Pelo menos um campo opcional deve ser fornecido para PATCH"}, 400
            if not request.json.get('nome'):
                nome = False
            else:
                nome = request.json.get('nome')
            if not request.json.get('senha'):
                senha = False
            else:
                senha = request.json.get('senha')
            if not request.json.get('cargo'):
                cargo = False
            else:
                cargo = request.json.get('cargo')
            editado = editar_parcialmente_equipe(matricula, nome, cargo, senha)
            return editado
        case "DELETE":
            deletado = delete_equipe(request.json.get('matricula'))
            return deletado


@api.route('/v1/equipes/', methods=['GET'])
def obter_equipes_api():
    equipes = obter_equipes()
    return equipes


@api.route('/v1/equipes/<int:matricula>', methods=['GET'])
def obter_equipe_api(matricula):
    equipe_obtido = ler_equipe(matricula)
    return equipe_obtido


# ### NOVAS ROTAS ALUNOS ### ### ### ### ### ### ### ###

@api.route('/v1/aluno/', methods=['POST',"PUT","PATCH", "DELETE"])
def aluno_api():
    if not (request.json.get('matricula')):
        # return request.son;
        return {"Bad Request": "Falta MATRICULA"}, 400
    matricula = request.json.get('matricula')

    match request.method:
        case "POST":
            if not (request.json.get('nome')):
                return {"Bad Request": "Faltam dados completos {Matrícula e Nome}"}, 400
            nome = request.json.get('nome')
            inserido = inserir_aluno(matricula, nome)
            return inserido
        case "PUT":
            if not ( request.json.get('nome') and request.json.get('nota') and request.json.get('turma')):
                return {"Bad Request": "Todos os campos devem ser fornecidos para PUT"}, 400
            nome = request.json.get('nome')
            nota = request.json.get('nota')
            turma = request.json.get('turma')
            editado = editar_aluno(matricula, nome, turma, nota)
            return editado
        case "PATCH":
            if not ( request.json.get('nome') or request.json.get('nota') or request.json.get('turma')):
                return {"Bad Request": "Pelo menos um campo opcional deve ser fornecido para PATCH"}, 400
            if not request.json.get('nome'):
                nome = False
            else:
                nome = request.json.get('nome')
            if not request.json.get('nota'):
                nota = False
            else:
                nota = request.json.get('nota')
            if not request.json.get('turma'):
                turma = False
            else:
                turma = request.json.get('turma')
            editado = editar_parcialmente_aluno(matricula, nome, turma, nota)
            return editado
        case "DELETE":
            deletado = delete_aluno(request.json.get('matricula'))
            return deletado


@api.route('/v1/alunos/', methods=['GET'])
def obter_alunos_api():
    alunos = obter_alunos()
    return alunos


@api.route('/v1/alunos/<int:matricula>', methods=['GET'])
def obter_aluno_api(matricula):
    aluno_obtido = ler_aluno(matricula)
    return aluno_obtido


# ### ROTAS DE TESTE ### ### ### ### ### ### ### ###

@api.route('/v1/test-db', methods=['GET'])
def testar_db():
    try:
        teste = check_db_connection();
        if teste == 1:
            return jsonify({"success": True, "message": "Conexão com o banco de dados está funcionando!"}), 200
        else:
            return jsonify({"success": False, "message": "Falha na conexão com o banco de dados."}), 500
    except Exception as e:
        return jsonify({"success": False, "message": f"Erro: {str(e)}"}), 500
