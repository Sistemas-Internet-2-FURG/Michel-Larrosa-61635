document.addEventListener("DOMContentLoaded", function () {
function alunosGET(){
    fetch('alunos') // GET AUTOMÁTICO
            .then(response => response.json())
            .then(data => {

                const alunosTableBody = document.getElementById('alunos-table-body');
                alunosTableBody.innerHTML = '';
                data.forEach(aluno => {
                    const row = `
                        <tr>
                            <td>${aluno.matricula}</td>
                            <td>${aluno.turma}</td>
                            <td>${aluno.nome}</td>
                            <td>${aluno.nota}</td>
                            <td>
                                <a href="#" class="btn btn-warning" data-bs-toggle="modal" data-bs-target="modalAlunoEditar" onclick="abrirModalEditar(${aluno.matricula})">EDITAR</a>
                                <a href="#" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#excluirModal" onclick="confirmarExclusao(${aluno.matricula})">EXCLUIR</a>
                            </td>
                        </tr>
                    `;
                    alunosTableBody.innerHTML += row;
                });
            })
            .catch(error => console.error('Erro ao carregar alunos:', error));
    }
}
function alunoGET(){}
function alunoPOST(){}
function alunoPUT(){}
function alunoPATCH(){}
function alunoDELETE(){}

const alunos = {
    uri: "/v1/alunos",
    request: (method, uri, dados = {}) => {
        return fetch(uri, {
            method: method,
            headers: { "Content-Type": "application/json" },
            body: method !== "GET" ? JSON.stringify(dados) : undefined,
        }).then(response => response.json());
    },
    POST: (dados) => alunos.request("POST", uri, dados),
    GET: () => alunos.request("GET", uri, dados),
    PUT: (dados) => alunos.request("PUT", uri, dados),
    DELETE: (dados) => alunos.request("DELETE", uri, dados),
};

// Exemplos de uso:
// alunos.GET("/v1/alunos").then(console.log);
// alunos.POST("/v1/alunos", { nome: "João" }).then(console.log);

// ### Função para carregar os alunos na tabela

    function carregarAlunos(alunosDados) {

        const alunosTableBody = document.getElementById('alunos-table-body');
        alunosTableBody.innerHTML = '';
        alunosDados.forEach(aluno => {
            const row = `
                <tr>
                    <td>${aluno.matricula}</td>
                    <td>${aluno.turma}</td>
                    <td>${aluno.nome}</td>
                    <td>${aluno.nota}</td>
                    <td>
                        <a href="#" class="btn btn-warning" data-bs-toggle="modal" data-bs-target="modalAlunoEditar" onclick="abrirModalEditar(${aluno.matricula})">EDITAR</a>
                        <a href="#" class="btn btn-danger" data-bs-toggle="modal" data-bs-target="#excluirModal" onclick="confirmarExclusao(${aluno.matricula})">EXCLUIR</a>
                    </td>
                </tr>
            `;
            alunosTableBody.innerHTML += row;
        });
    }

});

