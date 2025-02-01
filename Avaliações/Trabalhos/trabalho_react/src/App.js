import React from 'react';

import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Alunos from "./alunos/Alunos";
import Home from "./geral/home";
import NotFound from "./geral/404";

const App = () => {

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/alunos" element={<Alunos />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </Router>
  );

};

export default App;
