import React, { useEffect, useState } from 'react';
// import "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css";
// import "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js";
// import "./bootstrap.bundle.min.js";
import './bootstrap.min.css';
import './style.css';

// MODAIS
import ModalInserir from "./ModalInserir";
import ModalEditar from "./ModalEditar";
import ModalExcluir from "./ModalExcluir";

const Alunos = () => {
  const [alunos, setAlunos] = useState([]);  
  const [novoAluno, setNovoAluno] = useState({ matricula: '', nome: '' });
  const [deleteMatricula, setDeleteMatricula] = useState("");
  
// MODAIS
  const [showInserirModal, setShowInserirModal] = useState(false);
  const [showExcluirModal, setShowExcluirModal] = useState(false);
  // const [alunoSelecionado, setAlunoSelecionado] = useState({});
  // funções para abrir os modais
  const handleOpenInserir = () => setShowInserirModal(true);
  const handleOpenExcluir = (aluno) => {
    // setAlunoSelecionado(aluno);
    setShowExcluirModal(true);
  };
  // funções para fechar os modais
  const handleCloseInserir = () => setShowInserirModal(false);
  const handleCloseExcluir = () => setShowExcluirModal(false);

  // a respeito do ModalEditar
  const [showEditarModal, setShowEditarModal] = useState(false);
  const [selectedAluno, setSelectedAluno] = useState(null);
  const [selectedMatricula, setSelectedMatricula] = useState(null);
  const handleOpenEditar = (matricula) => {
    setSelectedMatricula(matricula);
    setShowEditarModal(true);
  };
  const handleCloseEditar = () => {
    setShowEditarModal(false);
    setSelectedAluno(null);
  };
  useEffect(() => { // Carregar aluno selecionado para edição
    if (selectedMatricula) {
      const fetchAluno = async () => {
        const alunoData = await READ(selectedMatricula);
        setSelectedAluno(alunoData);
      };
      fetchAluno();
    }
  }, [selectedMatricula]);
  const handleEditAluno = async (selectedAluno) => {
    const { matricula, nome, turma, nota } = selectedAluno;
    const data = await UPDATE(matricula, nome, turma, nota);
    if (data.status === 200) carregarAlunos();
    setSelectedAluno(null);
    setShowEditarModal(false);
  };

  // CRUD Functions
  const CREATE = async (matricula, nome) => {
    const response = await fetch('/v1/aluno/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify({ matricula, nome}), 
    });
    return response.json();
  };
  const READ = async (matricula = '') => {
    const response = await fetch(`http://localhost:5000/v1/alunos/${matricula}`, {
      method: 'GET',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
    });
    return response.json();
  };
  const UPDATE = async (matricula, nome, turma, nota) => {
    const method = nome && turma && nota ? 'PUT' : 'PATCH';
    const body = { matricula, ...(nome && { nome }), ...(turma && { turma }), ...(nota && { nota }) };

    const response = await fetch('/v1/aluno/', {
      method,
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify(body),
    });
    return response.json();
  };
  const DELETE = async (matricula) => {
    const response = await fetch('/v1/aluno/', {
      method: 'DELETE',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify({ matricula }),
    });
    return response.ok;
  };

  // Load alunos
  const carregarAlunos = async () => {
    const data = await READ();
    setAlunos(data.Alunos);
  };

  useEffect(() => { // Carregar alunos ao carregar a página
    carregarAlunos();
  }, []);

  

  // funções para manipular os dados
  const handleInsertAluno = async (novoAluno) => {
    console.log("Novo aluno a ser inserido:", novoAluno);
    const data = await CREATE(novoAluno.matricula, novoAluno.nome);
    if (data.status === 201) carregarAlunos();
    setNovoAluno({ matricula: '', nome: '' });
  };
  const handleDelete = async (deleteMatricula) => {
    console.dir("Matrícula a ser deletada:", deleteMatricula);
    if (await DELETE(deleteMatricula)) carregarAlunos();
    setDeleteMatricula("");
  };
  
  return (
    <>

      <nav className="navbar navbar-expand-lg navbar-dark bg-primary fixed-top">
        <div className="container">
          <a className="navbar-brand" href="#">Akademiq</a>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav me-auto">
              <li className="nav-item">
                <a className="nav-link" href="/">Relatórios</a>
              </li>
              <li className="nav-item">
                <a className="nav-link active" href="alunos">Alunos</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="turmas">Turmas</a>
              </li>
              <li className="nav-item">
                <a className="nav-link" href="equipe">Equipe</a>
              </li>
            </ul>
            <form className="d-flex">
              <span className="navbar-text me-3">LOGADO</span>
              <a className="logout" href="logout">LOGOUT</a>
            </form>
          </div>
        </div>
      </nav>

      <div className="container mt-4 p-5 border border-dark rounded">
        <div className="row">
          <div id='coluna-principal' className="col-md-8">
            <table className="table table-striped">
              <thead>
                <tr>
                  <th>Matrícula</th>
                  <th>Nome</th>
                  <th>Nota</th>
                  <th>Turma</th>
                </tr>
              </thead>
              <tbody>
                {alunos.map((aluno) => (
                  <tr key={aluno.matricula}>
                    <td>{aluno.matricula}</td>
                    <td>{aluno.nome}</td>
                    <td>{aluno.nota}</td>
                    <td>{aluno.turma}</td>
                    <td>
                      <button
                        className="btn btn-warning"
                        name='btnEditarAluno'
                        onClick={() => handleOpenEditar(aluno.matricula)}
                      >
                        EDITAR
                      </button>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <div id='coluna-botoes' className="col-md-4">
            <div className="container">
              <button className="btn btn-success" onClick={handleOpenInserir}>
                Abrir Modal de Inserir Aluno
              </button>

              <button className="btn btn-danger" onClick={handleOpenExcluir}>
                Abrir Modal de Exclusão de Aluno
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* Modals */}
            <ModalInserir
              show={showInserirModal}
              onClose={handleCloseInserir}
              onInsert={handleInsertAluno}
            />
            <ModalEditar
              show={showEditarModal}
              onClose={handleCloseEditar}
              onEditar={handleEditAluno}
              aluno={selectedAluno}
            />
            <ModalExcluir
              show={showExcluirModal}
              onClose={handleCloseExcluir}
              onDelete={handleDelete}
            />
      {/* Insert, Edit, Delete modals would follow a similar structure */}

      <footer className="footer mt-auto py-3 bg-light">
        <div className="container">
          <span className="text-muted">&copy; 2024 Todos os direitos reservados.</span>
        </div>
      </footer>
    </>
  );
};

export default Alunos;
