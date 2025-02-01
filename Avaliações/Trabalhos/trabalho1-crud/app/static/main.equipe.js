// CRUD++ (CREATE, READ+FULLREAD, )
const CREATE = async (matricula,nome) => {
    return fetch("/v1/equipe/", {
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
    return fetch("/v1/equipes/"+matricula, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }
    })
    .then(resposta => resposta.json())
    .then(data =>{
        if(matricula == ""){
            return data.Equipes;
        }else{
            return data;
        }
    })
    .catch(err => console.error("Erro :", err));
};
const UPDATE = async (matricula, nome="", cargo="", senha="") => { //função dupla PUT(Full) e PATCH(Partial)
    console.log(matricula, nome, cargo, senha);
    if( nome=="" && cargo=="" && senha=="" ){
        console.log("nada a atualizar");
        return 0;
    }else{
        if((nome && cargo && senha )){
            return fetch("/v1/equipe/", {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify({
                    matricula: matricula,
                    nome: nome,
                    cargo: cargo,
                    senha: senha
                })
            })
            .then(resultado => resultado.json())
            .then(data => {
                return data;
            })
            .catch(err => console.error("Erro:", "PUT "+err));
        }else{
            const json_equipe_dados={};
            json_equipe_dados.matricula=matricula;
            (nome ? json_equipe_dados.nome=nome : 0);
            (cargo ? json_equipe_dados.cargo=cargo : 0);
            (senha ? json_equipe_dados.senha=senha : 0);
            return fetch("/v1/equipe/", {
                method: 'PATCH',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify(json_equipe_dados)
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
    return fetch("/v1/equipe/", {
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

// ### Função para carregar os equipes na tela
function carregarEquipes() {
    const equipesTableBody = document.getElementById('equipes-table-body');
    equipesTableBody.innerHTML = '';
    READ()
    .then(Equipes =>{
        Equipes.forEach(equipe => {
            tr = document.createElement("tr");
            Object.entries(equipe).forEach(dado => {
                td = document.createElement("td");
                td.appendChild(document.createTextNode(dado[1]));
                tr.appendChild(td);
            })
            td = document.createElement("td");
            a = document.createElement("a");
            a.className="btn btn-warning";
            a.setAttribute("data-bs-toggle", 'modal');
            a.setAttribute("data-bs-target",'#EquipeEditar')
            a.addEventListener('click', function(){
                carregarEquipeEditar(equipe.matricula)
            })
            a.innerText="EDITAR";
            td.appendChild(a)
            tr.appendChild(td);
            equipesTableBody.appendChild(tr);


            // //manter paracomparação//
            // const row = `
            //     <tr>
            //         <td>${aluno.matricula}</td>
            //         <td>${aluno.turma}</td>
            //         <td>${aluno.nome}</td>
            //         <td>${aluno.nota}</td>
            //         <td>
            //             <a href="#" class="btn btn-warning" data-bs-toggle="modal" data-bs-target="modalAlunoEditar" onclick="abrirModalEditar(${aluno.matricula})">EDITAR</a>
            //         </td>
            //     </tr>
            // `;
            // alunosTableBody.innerHTML += row;

        })
    })
    .catch(error => console.error('Erro ao carregar equipes:', error));
}

function carregarEquipeEditar(matricula) { // Faz uma requisição para obter os dados do equipe a ser editado
    READ(matricula)
    .then(equipe => {
        // Preenche os campos do modal com os dados do equipe
        document.getElementById('EquipeEditarMatricula').value = equipe.matricula;
        document.getElementById('EquipeEditarCargo').value = equipe.cargo;
        document.getElementById('EquipeEditarNome').value = equipe.nome;
        document.getElementById('EquipeEditarSenha').value = equipe.senha;
    })
}

function fechar_modal(idDoElementoModal) {
    const modalElement = document.getElementById(idDoElementoModal);
    const modalInstance = bootstrap.Modal.getInstance(modalElement);
    modalInstance.hide();  // Fecha o modal
}

document.addEventListener("DOMContentLoaded", function () {
    // CONFIGURA MODAL DE EXCLUIR ALUNO
    document.getElementById("btnExcluirEquipe").addEventListener('click', function(){
        const modalEquipeExcluir_checkout=document.getElementById('modalEquipeExcluirCheckout');
        const modalEquipeExcluir_submit=document.getElementById('modalEquipeExcluirSubmit');
        modalEquipeExcluir_checkout.addEventListener('click', function (){
            if(this.checked){
                modalEquipeExcluir_submit.disabled=false;
            }else{
                modalEquipeExcluir_submit.disabled=true;
            }
        });
    });

    // EXECUTA INSERÇÃO E FECHA MODAL DE INSERIR ALUNO
    const inserirForm = document.getElementById('inserirEquipeModalForm');
    inserirForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const matricula = document.getElementById('inserirEquipeModalMatricula').value;
        const nome = document.getElementById('inserirEquipeModalNome').value;
        CREATE(matricula, nome)
        .then(data => {
            fechar_modal("inserirEquipeModal"); //importante
            if (data.status == 201) {
                carregarEquipes();
            } else if(data.status == 409){
                alert('Matricula já existente.');
            }else{
                alert('Erro ao inserir equipe.');
            }
        })
        .catch(error => console.error('Erro:', error));
    });

    // EXECUTA ATUALIZAÇÃO E FECHA MODAL DE EDITAR ALUNO
    const formEditEquipe = document.getElementById('EquipeEditarForm');
    formEditEquipe.addEventListener('submit', function (e) {
        e.preventDefault();
        const matricula = document.getElementById('EquipeEditarMatricula').value;
        const nome = document.getElementById('EquipeEditarNome').value;
        const cargo = document.getElementById('EquipeEditarCargo').value;
        const senha = document.getElementById('EquipeEditarSenha').value;
        UPDATE(matricula,nome,cargo,senha)
        .then(data =>{
            fechar_modal("EquipeEditar");
            if(data.status== 200){
                carregarEquipes();
            } else {
                alert('Erro ao editar equipe.');
            }
        })
        .catch(error => console.error('Erro:', error));
    });

    // EXECUTA EXCLUSÃO E FECHA MODAL DE EXCLUIR ALUNO
    const formExcluiEquipe = document.getElementById('modalEquipeExcluirForm');
    formExcluiEquipe.addEventListener('submit', function (e) {
        e.preventDefault();
        const matricula = document.getElementById('modalEquipeExcluirMatricula').value;
        DELETE(matricula)
        .then(response => {
            if (response.ok){
                fechar_modal("modalEquipeExcluir");
                carregarEquipes();
            }else{
                console.log('Problemas');
            }
        })
        .catch(error => console.error('Erro:', error));
    });

    // POR ÚLTIMO O PRINCIPAL
    carregarEquipes();
});

// Executando um "fetch()" com método DELETE, não ha corpo da resposta, como executar um trecho de código com ".then()" após o "fetch()" ?
