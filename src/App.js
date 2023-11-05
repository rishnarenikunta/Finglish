
import { BrowserRouter as Router, Route } from "react-router-dom";
import { Routes } from "react-router-dom";
import React, { useState } from 'react';
import Document from "./Document";

function App() {

  const [selectedFile, setSelectedFile] = useState(null);

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Document />} />
      </Routes>
    </Router>
  );
}

export default App;
