const CheckBoxes = () => {
    const colorPalette = {
        "module": "#EE9949",
        "varaible": "#A8A8FF",
        "class": "#FF4747",
        "function": "#39DB49",
        "parameter": "#CF4DFF",
        "import": "#FF8AE6"
    }
    
    return (
      <div className="checkbox-container">
        <div className="row">
          <input type="checkbox" id="1" checked="true"/>
          <label className="checkbox-label" style={{color: "#EE9949"}}>Module</label>
          <input type="checkbox" id="2" checked="true"/>
          <label className="checkbox-label" style={{color: "#FF8AE6"}}>Imports</label>
        </div>
  
        <div className="row">
            <input type="checkbox" id="4" name="Option 4" checked="true"/>
            <label className="checkbox-label" style={{color: "#FF4747"}}>Class</label>
            <input type="checkbox" id="5" name="Option 5" checked="true"/>
            <label className="checkbox-label">Inherits</label>
            <input type="checkbox" id="6" name="Option 6" checked="true"/>
            <label className="checkbox-label" style={{color: "#A8A8FF"}}>Class Variables</label>
            <input type="checkbox" id="6" name="Option 6" checked/>
            <label className="checkbox-label" style={{color: "#A8A8FF"}}>Instance Variables</label>
        </div>
        <div className="row">
            <input type="checkbox" id="7" name="Option 7" checked="true"/>
            <label className="checkbox-label" style={{color: "#39DB49"}}>Function</label>
            <input type="checkbox" id="8" name="Option 8" checked="true"/>
            <label className="checkbox-label" style={{color: "#CF4DFF"}}>Parameters</label>
        </div>
      </div>
    )
}

export default CheckBoxes
