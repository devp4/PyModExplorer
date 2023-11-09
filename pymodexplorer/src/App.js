import { useState } from 'react';
import './App.css';
import CheckBoxes from './Checkboxes';
import Tree from './Tree';
import example from "./data.json"

function App() {

  function handleFileUpload(event) {
    const file = event.target.files[0];

    if (!file) {
      return
    }

    if (file.name.slice(-2) !== "py") {
      alert("No a py file")
      return
    } 
  
    if (file) {
      readFileContents(file);
    }
  }
  
  function readFileContents(file) {
    const reader = new FileReader();
    reader.onload = (event) => {
      const fileContent = event.target.result
      
      if (reader.DONE) {
        sendFileContent(file.name, fileContent)
      }
    };

    reader.onerror = (event) => {
      console.log(event.target.error)
      return
    }
  
    reader.readAsText(file);
  }
  
  async function sendFileContent(filename, fileContent) {
    const response = await fetch("http://127.0.0.1:5000/parse", {
        method: "POST",
        mode: "cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({"name": filename, "content": fileContent})
      }
    );
    
    const data = await response.json();
    setFile(data)
    console.log(data)
  }

  const [file, setFile] = useState(example)

  return (
    <div className="container">
      <div className="left-container">
        <h1 className="logo">PyModExplorer</h1>
        <div className="options">
          <input className="file-selector" type="file" accept=".py" onChange={handleFileUpload}/>
        </div>
      </div> 
      <div className="tree-container">
        <div className="tree">
          <Tree file={file} setFile={setFile}/>
        </div>
      </div>   
    </div>
  );
}

export default App;
