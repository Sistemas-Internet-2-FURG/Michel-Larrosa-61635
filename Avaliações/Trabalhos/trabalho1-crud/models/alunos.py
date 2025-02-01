from flask import current_app, jsonify
from app.models import db

# ### ### ### ### ### ### DEFINIÇÃO DA CLASSE ALUNOS ### ### ### ### ### ###
# ### file:///home/michel/Estudos/PYTHON/sqlalchemy_20/orm/mapping_styles.html#declarative-mapping

class Aluno(db.Model):
    __tablename__ = 'alunos'
    matricula = db.Column(db.Integer, primary_key=True)
    turma = db.Column(db.String(100), db.ForeignKey('turmas.identificador'), nullable=True)
    nome = db.Column(db.String(100), nullable=False)
    nota = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return f"<Aluno {self.matricula}: {self.nome}, Turma: {self.turma}, Nota: {self.nota}>"


# ### ### ### ### ### ### GERENCIAMENTO DE ALUNOS ### ### ### ### ### ###
# from models.alunos import Aluno # descomentar caso as funções ñ fiquem no arquivo da classe

def inserir_aluno(matricula, nome):
    try:
        aluno = db.session.query(Aluno).filter_by(matricula=matricula).first()
        if aluno:
            return {"message": "Aluno Já existente", "status":409}, 409
        # o banco PSQL foi criado com nenhum nulo, gambiarra
        # novo_aluno = Aluno(matricula=matricula, turma='1101', nome=nome, nota=0)
        novo_aluno = Aluno(matricula=matricula, nome=nome)
        db.session.add(novo_aluno)
        db.session.commit()
        return {"message": "Aluno criado com sucesso", "status":201}, 201
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 400


def obter_alunos():
    try:
        # ### QUERYs
        # result = db.session.execute("SELECT matricula, nome, turma, nota FROM alunos ORDER BY matricula")
        result = db.session.query(Aluno).with_entities(Aluno.matricula, Aluno.nome, Aluno.turma, Aluno.nota).order_by(Aluno.matricula)
        #
        #
        # ### ESTRUTURA PREGUIÇOSA
        ## como alguns campos vêm como inteiros, jsonify ñ funcionará, deixarei como dicioário
        # dicionario é Array(), então o requisitor deve usar data.Alunos.forEach()
        alunos = [dict(row) for row  in result]
        #
        #
        # ### ESTRUTURA TRABALHOSA
        ##Essa função onverte uma linha SQLAlchemy para um dicionário posteriormente JSON serializável.
        # def row_to_dict(row):
        #     return {key: (value if not hasattr(value, 'isoformat') else value.isoformat()) for key, value in row.items()}
        # alunos = [row_to_dict(row) for row in result]
        # alunos = jsonify(alunos)
        #
        #
        return {"Alunos":alunos}, 200
    except Exception as e:
        return {"message": f"Erro ao buscar alunos: {str(e)}"}, 500


def ler_aluno(matricula):
    try:
        ## Modo 1, extenso demais
        # query = "SELECT matricula, nome, turma, nota FROM alunos WHERE matricula = :matricula"
        # aluno = db.session.execute(query, {"matricula": matricula}).fetchone()
        ## Modo 2, simples porém lógica não reutilizável, .get deprecated no futuro
        # aluno = db.session.get(Aluno, matricula)
        # ### Modo 3, Usar db.session.METHOD() para tudo me parece mais rentável/produtivo
        aluno = db.session.query(Aluno).filter_by(matricula=matricula).first()
        if aluno:
            return jsonify({
                "matricula": aluno.matricula,
                "nome": aluno.nome,
                "turma": aluno.turma,
                "nota": aluno.nota
            }), 200
        return {"error": "Aluno não encontrado"}, 404
    except Exception as e:
        return {"error": str(e)}, 500


def editar_aluno(matricula, nome, turma, nota):
    if not (turma and nome and nota):
        return {"Bad Request": "Todos os campos devem ser fornecidos para PUT"}, 400
    try:
        aluno = db.session.query(Aluno).filter_by(matricula=matricula).first()
        if aluno:
            if turma:
                aluno.turma = turma
            if nome:
                aluno.nome = nome
            if nota:
                aluno.nota = nota
            db.session.commit()
            return {"message": "Aluno editado com sucesso", "status":200}, 200
        return {"error": "Aluno não encontrado"}, 404
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500

def editar_parcialmente_aluno(matricula, nome=False, turma=False, nota=False):
    if not (turma or nome or nota):
        return {"Bad Request": "Pelo menos um campo opcional deve ser fornecido para PATCH"}, 400
    try:
        aluno = db.session.query(Aluno).filter_by(matricula=matricula).first()
        if aluno:
            if turma:
                aluno.turma = turma
            if nome:
                aluno.nome = nome
            if nota:
                aluno.nota = nota
            db.session.commit()
            return {"message": "Aluno editado com sucesso", "status":200}, 200
        return {"error": "Aluno não encontrado"}, 404
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}, 500

def delete_aluno(matricula):
    try:
        aluno = db.session.query(Aluno).filter_by(matricula=matricula).first()
        if aluno:
            db.session.delete(aluno)
            db.session.commit()
            # obs: com 204 o 'body' não é enviado
            # return {"message": "Aluno deletado com sucesso"}, 204
            return {}, 204
        return {"error": "Aluno não encontrado", "status":404}, 404
    except Exception as e:
        db.session.rollback()
        return {"error": str(e), "status":500}, 500
