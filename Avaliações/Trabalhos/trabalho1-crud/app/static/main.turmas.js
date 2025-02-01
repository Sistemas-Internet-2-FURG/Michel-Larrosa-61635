// CRUD++ (CREATE, READ+FULLREAD, )
const CREATE = async (identificador,disciplina, professor) => {
    return fetch("/v1/turma/", {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'Accept':'application/json'
        },
        body: JSON.stringify({
            "identificador":identificador,
            "disciplina":disciplina,
            "professor":professor
        })
    })
    .then(resultado => resultado.json())
    .then(data =>{
        return data;
    })
    .catch(err => console.error("Erro:", err));
};
const READ = async (identificador="") => { // função dupla GET e GETCollection
    return fetch("/v1/turmas/"+identificador, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    })
    .then(resposta => resposta.json())
    .then(data =>{
        if(identificador == ""){
            return data.Turmas;
        }else{
            return data;
        }
    })
    .catch(err => console.error("Erro :", err));
};
const UPDATE = async (identificador, disciplina="", professor="") => { //função dupla PUT(Full) e PATCH(Partial)
    console.log(identificador, disciplina, professor);
    if( disciplina=="" && professor==""){
        console.log("nada a atualizar");
        return 0;
    }else{
        if((disciplina && professor )){
            return fetch("/v1/turma/", {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    identificador: identificador,
                    disciplina: disciplina,
                    professor: professor
                })
            })
            .then(resultado => resultado.json())
            .then(data => {
                return data;
            })
            .catch(err => console.error("Erro:", "PUT "+err));
        }else{
            const json_turma_dados={};
            json_turma_dados.identificador=identificador;
            (disciplina ? json_turma_dados.disciplina=disciplina : 0);
            (professor ? json_turma_dados.professor=professor : 0);
            return fetch("/v1/turma/", {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify(json_turma_dados)
            })
            .then(resultado => resultado.json())
            .then(data => {
                return data;
            })
            .catch(err => console.error("Erro:", "PATCH "+err));
        }
    }
};
const DELETE = async (identificador) => {
    return fetch("/v1/turma/", {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
                'Accept': 'application/json'
        },
        body: JSON.stringify({
                identificador:identificador
        })
    })
    .catch(err => console.error("Erro :", err));
};

// ### Função para carregar os turmas na tela
function carregarTurmas() {
    const turmasTableBody = document.getElementById('turmas-table-body');
    turmasTableBody.innerHTML = '';
    READ()
    .then(Turmas =>{
        Turmas.forEach(turma => {
            tr = document.createElement("tr");
            Object.entries(turma).forEach(dado => {
                td = document.createElement("td");
                td.appendChild(document.createTextNode(dado[1]));
                tr.appendChild(td);
            })
            td = document.createElement("td");
            a = document.createElement("a");
            a.className="btn btn-warning";
            a.setAttribute("data-bs-toggle", 'modal');
            a.setAttribute("data-bs-target",'#TurmaEditar')
            a.addEventListener('click', function(){
                carregarTurmaEditar(turma.identificador)
            })
            a.innerText="EDITAR";
            td.appendChild(a)
            tr.appendChild(td);
            turmasTableBody.appendChild(tr);

        })
    })
    .catch(error => console.error('Erro ao carregar turmas:', error));
}

function carregarTurmaEditar(identificador) { // Faz uma requisição para obter os dados do turma a ser editado
    READ(identificador)
    .then(turma => {
        // Preenche os campos do modal com os dados do turma
        document.getElementById('TurmaEditarIdentificador').value = turma.identificador;
        document.getElementById('TurmaEditarProfessor').value = turma.professor;
        document.getElementById('TurmaEditarDisciplina').value = turma.disciplina;
    })
}

function fechar_modal(idDoElementoModal) {
    const modalElement = document.getElementById(idDoElementoModal);
    const modalInstance = bootstrap.Modal.getInstance(modalElement);
    modalInstance.hide();  // Fecha o modal
}

document.addEventListener("DOMContentLoaded", function () {
    // CONFIGURA MODAL DE EXCLUIR ALUNO
    document.getElementById("btnExcluirTurma").addEventListener('click', function(){
        const modalTurmaExcluir_checkout=document.getElementById('modalTurmaExcluirCheckout');
        const modalTurmaExcluir_submit=document.getElementById('modalTurmaExcluirSubmit');
        modalTurmaExcluir_checkout.addEventListener('click', function (){
            if(this.checked){
                modalTurmaExcluir_submit.disabled=false;
            }else{
                modalTurmaExcluir_submit.disabled=true;
            }
        });
    });

    // EXECUTA INSERÇÃO E FECHA MODAL DE INSERIR ALUNO
    const inserirForm = document.getElementById('inserirTurmaModalForm');
    inserirForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const identificador = document.getElementById('inserirTurmaModalIdentificador').value;
        const disciplina = document.getElementById('inserirTurmaModalDisciplina').value;
        const professor = document.getElementById('inserirTurmaModalProfessor').value;
        CREATE(identificador, disciplina, professor)
        .then(data => {
            fechar_modal("inserirTurmaModal"); //importante
            if (data.status == 201) {
                carregarTurmas();
            } else if(data.status == 409){
                alert('Identificador já existente.');
            }else{
                alert('Erro ao inserir turma.'+'status:'+data.status);
            }
        })
        .catch(error => console.error('Erro:', error));
    });

    // EXECUTA ATUALIZAÇÃO E FECHA MODAL DE EDITAR ALUNO
    const formEditTurma = document.getElementById('TurmaEditarForm');
    formEditTurma.addEventListener('submit', function (e) {
        e.preventDefault();
        const identificador = document.getElementById('TurmaEditarIdentificador').value;
        const disciplina = document.getElementById('TurmaEditarDisciplina').value;
        const professor = document.getElementById('TurmaEditarProfessor').value;
        UPDATE(identificador,disciplina,professor)
        .then(data =>{
            fechar_modal("TurmaEditar");
            if(data.status== 200){
                carregarTurmas();
            } else {
                alert('Erro ao editar turma.');
            }
        })
        .catch(error => console.error('Erro:', error));
    });

    // EXECUTA EXCLUSÃO E FECHA MODAL DE EXCLUIR ALUNO
    const formExcluiTurma = document.getElementById('modalTurmaExcluirForm');
    formExcluiTurma.addEventListener('submit', function (e) {
        e.preventDefault();
        const identificador = document.getElementById('modalTurmaExcluirIdentificador').value;
        DELETE(identificador)
        .then(response => {
            if (response.ok){
                fechar_modal("modalTurmaExcluir");
                carregarTurmas();
            }else{
                console.log('Problemas');
            }
        })
        .catch(error => console.error('Erro:', error));
    });

    // POR ÚLTIMO O PRINCIPAL
    carregarTurmas();
});

// Executando um "fetch()" com método DELETE, não ha corpo da resposta, como executar um trecho de código com ".then()" após o "fetch()" ?
