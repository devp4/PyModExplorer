import './App.css';
import CheckBoxes from './Checkboxes';
import Tree from './Tree';

function App() {
  return (
    <div className="container">
      <div className="left-container">
        <h1>PyModExplorer</h1>
        <div className="options">
          <CheckBoxes/>
        </div>
      </div> 
      <div className="tree-container">
        <div className="tree">
          <Tree/>
        </div>
      </div>   
    </div>
  );
}

export default App;
