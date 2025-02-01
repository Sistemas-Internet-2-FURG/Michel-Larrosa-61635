import React, { useState, useEffect } from "react";

const ModalExcluir = ({ show, onClose, onDelete, matricula }) => {
  const [confirmChecked, setConfirmChecked] = useState(false);
  const [deleteMatricula, setDeleteMatricula] = useState("");

  useEffect(() => {
    if (matricula) {
      setDeleteMatricula(matricula);
    }
  }, [matricula]);

  const handleInputChange = (e) => {
    setDeleteMatricula(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Matrícula a ser deletada:", deleteMatricula);
    onDelete(deleteMatricula);
    setDeleteMatricula("");
    onClose();
  };

  if (!show) return null;

  return (
    <div className="modal show d-block" tabIndex="-1">
      <div className="modal-dialog">
        <div className="modal-content">
          <div className="modal-header">
            <h5 className="modal-title">Excluir Aluno</h5>
            <button type="button" className="btn-close" onClick={onClose}></button>
          </div>
          <div className="modal-body">
            <form id="AlunoExcluirForm" onSubmit={handleSubmit}>
              <div className="mb-3">
                <label htmlFor="matricula" className="form-label">Matrícula</label>
                <input
                  type="text"
                  className="form-control"
                  id="matricula"
                  value={deleteMatricula}
                  onChange={handleInputChange}
                />
              </div>
              <div className="mb-3 form-check">
                <input
                  type="checkbox"
                  className="form-check-input"
                  id="modalAlunoExcluirCheckout"
                  onChange={(e) => setConfirmChecked(e.target.checked)}
                />
                <label htmlFor="modalAlunoExcluirCheckout" className="form-check-label">
                  Tenho certeza da exclusão
                </label>
              </div>
            </form>
          </div>
          <div className="modal-footer">
            <button type="button" className="btn btn-secondary" onClick={onClose}>
              Cancelar
            </button>
            <button
              type="submit"
              className="btn btn-danger"
              disabled={!confirmChecked}
              onClick={handleSubmit}
            >
              Excluir
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ModalExcluir;
