from flask import Blueprint, jsonify

api = Blueprint('api', __name__)

# ROTAS PARA SOLICITAR/INSERIR DADOS ### ### ROTAS API ### ### ### ### ### ### ### ### ### ###
# NOVAS ROTAS ALUNOS
@api.route('/obter-alunos/', methods=['GET'])
def obter_alunos_api():
    alunos = obter_alunos()
    return alunos


@api.route('/obter-aluno/<int:matricula>', methods=['GET'])
def obter_aluno_api(matricula):
    aluno = read_aluno(matricula)
    if aluno:
        aluno_dict = {
            "matricula": aluno[0],
            "turma": aluno[1],
            "nome": aluno[2],
            "nota": aluno[3]
        }
        return jsonify(aluno_dict)
    else:
        return jsonify({"error": "Aluno não encontrado"}), 404


@api.route('/editar-aluno/<int:matricula>/<int:turma>/<string:nome>/<int:nota>', methods=['POST', 'PUT'])
def editar_aluno_api(matricula, turma, nome, nota):
    aluno = editar_aluno(matricula, turma, nome, nota)
    if aluno:
        # current_app.logger.info("OK")
        return jsonify(aluno)
    else:
        return jsonify({"error": "Aluno não encontrado"}), 404


@api.route('/inserir-aluno/<int:matricula>/<int:turma>/<string:nome>/<int:nota>', methods=['POST','GET']) # GET somente para teste
def inserir_aluno_api(matricula, turma, nome, nota):
    resultado = inserir_aluno(matricula, turma, nome, nota)
    if isinstance(resultado, int):
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'error': resultado})


@api.route('/excluir-aluno/<int:matricula>', methods=['GET', 'DELETE',]) # GET somente para teste
def excluir_aluno_api(matricula):
    resultado = delete_aluno(matricula)

    if resultado is True:
        return jsonify({"success": True, "message": "Aluno excluído com sucesso"})
    elif isinstance(resultado, str):  # Se houver um erro retornado
        return jsonify({"success": False, "error": resultado}), 500
    else:
        return jsonify({"success": False, "message": "Aluno não encontrado"}), 404
