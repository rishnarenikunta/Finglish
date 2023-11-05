import logo from './logo.svg';
import './App.css';
import { BrowserRouter as Router, Route } from "react-router-dom";
import { Routes } from "react-router-dom";
import React, { useState } from 'react';
import Upload from "./Upload";
import Uploaded from "./Uploaded";
import Document from "./Document";
import Par from "./Par";
// import { FileProvider } from './FileContext';

function App() {

  const [selectedFile, setSelectedFile] = useState(null);

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Upload />} />
        <Route path="/uploaded" element={<Uploaded />} />
        <Route path="/document" element={<Document />} />
        <Route path="/par" element={<Par />} />
      </Routes>
    </Router>
    // <Router>
    //   <div>
    //     <section>
    //       <Routes>
    //         <Route path="/" element={<Upload />} />
    //         <Route path="/uploaded" element={<Uploaded />} />
    //         <Route path="/document" element={<Document />} />
    //         {/* <Route path="/parent" element={<Parentt />} /> */}
    //       </Routes>
    //     </section>
    //   </div>
    // </Router>
  );
}

export default App;
