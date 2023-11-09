const CheckBoxes = ({ visible, setVisible }) => {

  const onClick = (name) => {
    if (visible.includes(name)) {
      var removedValue = visible.filter(item => item !== name)
      setVisible(removedValue)
    }

    else {
      setVisible([...visible, name])
    }

  }

  return (
    <div className="checkbox-container">
      <div className="row">
        <input type="checkbox" checked={visible.includes("module")} onClick={() => onClick("module")} />
        <label className="checkbox-label" style={{ color: "#EE9949" }}>Module</label>
        <input type="checkbox" checked={visible.includes("imports")} onClick={() => onClick("imports")} />
        <label className="checkbox-label" style={{ color: "#FF8AE6" }}>Imports</label>
      </div>

      <div className="row">
        <input type="checkbox" checked={visible.includes("class")} onClick={() => onClick("class")} />
        <label className="checkbox-label" style={{ color: "#FF4747" }} onClick={() => onClick("module")}>Class</label>
        <input type="checkbox" checked={visible.includes("inherits")} onClick={() => onClick("inherits")} />
        <label className="checkbox-label">Inherits</label>
        <input type="checkbox" checked={visible.includes("class variables")} onClick={() => onClick("class variables")} />
        <label className="checkbox-label" style={{ color: "#A8A8FF" }}>Class Variables</label>
        <input type="checkbox" checked={visible.includes("instance variables")} onClick={() => onClick("instance variables")} />
        <label className="checkbox-label" style={{ color: "#A8A8FF" }}>Instance Variables</label>
      </div>
      <div className="row">
        <input type="checkbox" checked={visible.includes("function")} onClick={() => onClick("function")} />
        <label className="checkbox-label" style={{ color: "#39DB49" }}>Function</label>
        <input type="checkbox" checked={visible.includes("parameters")} onClick={() => onClick("parameters")} />
        <label className="checkbox-label" style={{ color: "#CF4DFF" }}>Parameters</label>
      </div>
    </div>
  )
}

export default CheckBoxes
