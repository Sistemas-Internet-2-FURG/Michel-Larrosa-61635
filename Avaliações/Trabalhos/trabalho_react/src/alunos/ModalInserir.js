import React, { useState } from "react";

const ModalInserir = ({ show, onClose, onInsert }) => {
  const [novoAluno, setNovoAluno] = useState({
    matricula: "",
    nome: "",
  });

  const handleInputChange = (e) => {
    const { id, value } = e.target;
    setNovoAluno({ ...novoAluno, [id]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Submitting novoAluno:", novoAluno); // Adicionado este log
    onInsert(novoAluno);
    setNovoAluno({ matricula: "", nome: "" }); // Limpa o formulário
    onClose(); // Fecha o modal
  };

  if (!show) return null;

  return (
    <div className="modal show d-block" tabIndex="-1">
      <div className="modal-dialog">
        <div className="modal-content">
          <div className="modal-header">
            <h5 className="modal-title">Inserir Aluno</h5>
            <button type="button" className="btn-close" onClick={onClose}></button>
          </div>
          <div className="modal-body">
            <form id="inserirAlunoModalForm" onSubmit={handleSubmit}>
              <div className="mb-3" id="inserirAlunoModalFormDivMatricula">
                <label htmlFor="matricula" className="form-label">
                  Matrícula
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="matricula"
                  value={novoAluno.matricula}
                  onChange={handleInputChange}
                  required
                />
              </div>
              <div className="mb-3" id="inserirAlunoModalFormDivNome">
                <label htmlFor="nome" className="form-label">
                  Nome
                </label>
                <input
                  type="text"
                  className="form-control"
                  id="nome"
                  value={novoAluno.nome}
                  onChange={handleInputChange}
                  required
                />
              </div>
              <button type="submit" className="btn btn-primary">
                Inserir
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ModalInserir;
