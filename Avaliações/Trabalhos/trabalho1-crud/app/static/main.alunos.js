// CRUD++ (CREATE, READ+FULLREAD, )
const CREATE = async (matricula,nome) => {
    return fetch("/v1/aluno/", {
        method: 'POST',
        headers: {
            'Content-Type':'application/json',
            'Accept':'application/json'
        },
        body: JSON.stringify({
            "matricula":matricula,
            "nome":nome
        })
    })
    .then(resultado => resultado.json())
    .then(data =>{
        return data;
    })
    .catch(err => console.error("Erro:", err));
};
const READ = async (matricula="") => { // função dupla GET e GETCollection
    return fetch("/v1/alunos/"+matricula, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    })
    .then(resposta => resposta.json())
    .then(data =>{
        if(matricula == ""){
            return data.Alunos;
        }else{
            return data;
        }
    })
    .catch(err => console.error("Erro :", err));
};
const UPDATE = async (matricula, nome="", turma="", nota="") => { //função dupla PUT(Full) e PATCH(Partial)
    console.log(matricula, nome, turma, nota);
    if( nome=="" && turma=="" && nota=="" ){
        console.log("nada a atualizar");
        return 0;
    }else{
        if((nome && turma && nota )){
            return fetch("/v1/aluno/", {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    matricula: matricula,
                    nome: nome,
                    turma: turma,
                    nota: nota
                })
            })
            .then(resultado => resultado.json())
            .then(data => {
                return data;
            })
            .catch(err => console.error("Erro:", "PUT "+err));
        }else{
            const json_aluno_dados={};
            json_aluno_dados.matricula=matricula;
            (nome ? json_aluno_dados.nome=nome : 0);
            (turma ? json_aluno_dados.turma=turma : 0);
            (nota ? json_aluno_dados.nota=nota : 0);
            return fetch("/v1/aluno/", {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify(json_aluno_dados)
            })
            .then(resultado => resultado.json())
            .then(data => {
                return data;
            })
            .catch(err => console.error("Erro:", "PATCH "+err));
        }
    }
};
const DELETE = async (matricula) => {
    return fetch("/v1/aluno/", {
        method: 'DELETE',
        headers: {
            'Content-Type': 'application/json',
                'Accept': 'application/json'
        },
        body: JSON.stringify({
                matricula:matricula
        })
    })
    .catch(err => console.error("Erro :", err));
};

function carregarAlunos() { //Função para carregar os alunos na tela
    const alunosTableBody = document.getElementById('alunos-table-body');
    alunosTableBody.innerHTML = '';
    READ()
    .then(Alunos =>{
        Alunos.forEach(aluno => {
            tr = document.createElement("tr");
            Object.entries(aluno).forEach(dado => {
                td = document.createElement("td");
                td.appendChild(document.createTextNode(dado[1]));
                tr.appendChild(td);
            })
            td = document.createElement("td");
            a = document.createElement("a");
            a.className="btn btn-warning";
            a.setAttribute("data-bs-toggle", 'modal');
            a.setAttribute("data-bs-target",'#AlunoEditar')
            a.addEventListener('click', function(){
                carregarAlunoEditar(aluno.matricula)
            })
            a.innerText="EDITAR";
            td.appendChild(a)
            tr.appendChild(td);
            alunosTableBody.appendChild(tr);
        })
    })
    .catch(error => console.error('Erro ao carregar alunos:', error));
}

function carregarAlunoEditar(matricula) { // Faz uma requisição para obter os dados do aluno a ser editado
    READ(matricula)
    .then(aluno => {
        // Preenche os campos do modal com os dados do aluno
        document.getElementById('AlunoEditarMatricula').value = aluno.matricula;
        document.getElementById('AlunoEditarTurma').value = aluno.turma;
        document.getElementById('AlunoEditarNome').value = aluno.nome;
        document.getElementById('AlunoEditarNota').value = aluno.nota;
    })
}

function fechar_modal(idDoElementoModal) {
    const modalElement = document.getElementById(idDoElementoModal);
    const modalInstance = bootstrap.Modal.getInstance(modalElement);
    modalInstance.hide();  // Fecha o modal
}

document.addEventListener("DOMContentLoaded", function () {
    // CONFIGURA FUNÇÃO CHECAR PARA MODAL DE EXCLUIR ALUNO
    document.getElementById("btnExcluirAluno").addEventListener('click', function(){
        const modalAlunoExcluir_checkout=document.getElementById('modalAlunoExcluirCheckout');
        const modalAlunoExcluir_submit=document.getElementById('modalAlunoExcluirSubmit');
        modalAlunoExcluir_checkout.addEventListener('click', function (){
            if(this.checked){
                modalAlunoExcluir_submit.disabled=false;
            }else{
                modalAlunoExcluir_submit.disabled=true;
            }
        });
    });

    // EXECUTA INSERÇÃO E FECHA MODAL DE INSERIR ALUNO
    const inserirForm = document.getElementById('inserirAlunoModalForm');
    inserirForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const matricula = document.getElementById('inserirAlunoModalMatricula').value;
        const nome = document.getElementById('inserirAlunoModalNome').value;
        CREATE(matricula, nome)
        .then(data => {
            fechar_modal("inserirAlunoModal"); //importante
            if (data.status == 201) {
                carregarAlunos();
            } else if(data.status == 409){
                alert('Matricula já existente.');
            }else{
                alert('Erro ao inserir aluno.');
            }
        })
        .catch(error => console.error('Erro:', error));
    });

    // EXECUTA ATUALIZAÇÃO E FECHA MODAL DE EDITAR ALUNO
    const formEditAluno = document.getElementById('AlunoEditarForm');
    formEditAluno.addEventListener('submit', function (e) {
        e.preventDefault();
        const matricula = document.getElementById('AlunoEditarMatricula').value;
        const nome = document.getElementById('AlunoEditarNome').value;
        const turma = document.getElementById('AlunoEditarTurma').value;
        const nota = document.getElementById('AlunoEditarNota').value;
        UPDATE(matricula,nome,turma,nota)
        .then(data =>{
            fechar_modal("AlunoEditar");
            if(data.status== 200){
                carregarAlunos();
            } else {
                alert('Erro ao editar aluno.');
            }
        })
        .catch(error => console.error('Erro:', error));
    });

    // EXECUTA EXCLUSÃO E FECHA MODAL DE EXCLUIR ALUNO
    const formExcluiAluno = document.getElementById('modalAlunoExcluirForm');
    formExcluiAluno.addEventListener('submit', function (e) {
        e.preventDefault();
        const matricula = document.getElementById('modalAlunoExcluirMatricula').value;
        DELETE(matricula)
        .then(response => {
            if (response.ok){
                fechar_modal("modalAlunoExcluir");
                carregarAlunos();
            }else{
                console.log('Problemas');
            }
        })
        .catch(error => console.error('Erro:', error));
    });

    // POR ÚLTIMO O PRINCIPAL
    carregarAlunos();
});
