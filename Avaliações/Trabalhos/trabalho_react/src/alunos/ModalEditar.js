import React, { useState, useEffect } from "react";

const ModalEditar = ({ show, onClose, onEditar, aluno }) => {
  const [selectedAluno, setSelectedAluno] = useState({
    matricula: "",
    nome: "",
    turma: "",
    nota: ""
  });

  useEffect(() => {
    if (aluno) {
      setSelectedAluno(aluno);
    }
  }, [aluno]);

  const handleInputChange = (e) => {
    const { id, value } = e.target;
    setSelectedAluno({ ...selectedAluno, [id]: value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onEditar(selectedAluno);
    setSelectedAluno({ matricula: "", nome: "", turma: "", nota: "" });
    onClose();
  };

  if (!show) return null;

  return (
    <div className="modal show d-block" tabIndex="-1">
      <div className="modal-dialog">
        <div className="modal-content">
          <div className="modal-header">
            <h5 className="modal-title">Editar Aluno</h5>
            <button type="button" className="btn-close" onClick={onClose}></button>
          </div>
          <div className="modal-body">
            <form id="AlunoEditarForm" onSubmit={handleSubmit}>
              <input type="hidden" id="matricula" value={selectedAluno.matricula || ""} readOnly />

              <div className="mb-3">
                <label htmlFor="turma" className="form-label">Turma</label>
                <input
                  type="text"
                  className="form-control"
                  id="turma"
                  value={selectedAluno.turma || ""}
                  onChange={handleInputChange}
                />
              </div>
              <div className="mb-3">
                <label htmlFor="nome" className="form-label">Nome</label>
                <input
                  type="text"
                  className="form-control"
                  id="nome"
                  value={selectedAluno.nome || ""}
                  onChange={handleInputChange}
                />
              </div>
              <div className="mb-3">
                <label htmlFor="nota" className="form-label">Nota</label>
                <input
                  type="number"
                  className="form-control"
                  id="nota"
                  value={selectedAluno.nota || ""}
                  onChange={handleInputChange}
                />
              </div>
              <button type="submit" className="btn btn-primary">
                Atualizar Aluno
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ModalEditar;
