document.addEventListener("DOMContentLoaded", function () {

    // ### Função para carregar os alunos na tabela
    // ### ### ###
    function carregarAlunos() {
        fetch('/obter-alunos')
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

    function abrirModalEditar(matricula) { // Faz uma requisição para obter os dados do aluno a ser editado
    fetch(`/obter-aluno/${matricula}`)
        .then(response => response.json())
        .then(aluno => {
            // Preenche o modal de edição com os dados do aluno
            document.getElementById('matricula').value = aluno.matricula;
            document.getElementById('turma').value = aluno.turma;
            document.getElementById('nome').value = aluno.nome;
            document.getElementById('nota').value = aluno.nota;

            // Mostra o modal de edição
            const modalEditar = new bootstrap.Modal(document.getElementById('modalAlunoEditar'));
            modalEditar.show();
        })
        .catch(error => {
            console.error('Erro ao carregar dados do aluno:', error);
        });
    }



    //### CONSTRÓI Formulário de ### EDIÇÃO ### de ALUNO
    function editarAluno(matricula) {
        console.log("EDITAR ALUNO " + matricula)
        fetch(`/obter-aluno/${matricula}`)
        .then(response => response.json())
        .then(aluno => {
            // Preenche os campos do modal com os dados do aluno
            document.getElementById('matricula').value = aluno.matricula;
            document.getElementById('turma').value = aluno.turma;
            document.getElementById('nome').value = aluno.nome;
            document.getElementById('nota').value = aluno.nota;

            // Desabilita o campo de matrícula para edição, se necessário
            document.getElementById('matricula').disabled = true;
        })
        .catch(error => {
            console.error('Erro ao carregar dados do aluno:', error);
        });
    }

    //### CONSTRÓI Formulário de ### EXCLUSÃO ### de ALUNO ### ### ### ###
    function abrirModalExcluir(matricula) {
        // Preenche o campo oculto no modal com o ID do aluno a ser excluído
        document.getElementById('matricula-excluir').value = matricula;

        // Mostra o modal de confirmação de exclusão
        const modalExcluir = new bootstrap.Modal(document.getElementById('modalAlunoExcluir'));
        modalExcluir.show();
    }


    //### CONSTRÓI Formulário de ### INSERÇÃO ### de ALUNO ##
    const inserirForm = document.getElementById('inserir-form');
    inserirForm.addEventListener('submit', function (e) {
        e.preventDefault();

        const matricula = document.getElementById('matricula').value;
        const turma = document.getElementById('turma').value;
        const nome = document.getElementById('nome').value;
        const nota = document.getElementById('nota').value;

        fetch('/inserir-aluno', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ matricula, turma, nome, nota })
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Fecha o modal manualmente
                    const modalElement = document.getElementById("inserirModal");
                    const modalInstance = bootstrap.Modal.getInstance(modalElement);
                    modalInstance.hide();  // Fecha o modal

                    carregarAlunos();

                    //var inserirModal = new bootstrap.Modal(document.getElementById('inserirModal'));
                    //inserirModal.hide();

                } else {
                    alert('Erro ao inserir aluno.');
                }
            })
            .catch(error => console.error('Erro:', error));
    });


    carregarAlunos();
});

