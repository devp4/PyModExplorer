import React, { useState } from 'react';
import { Treebeard, decorators  } from 'react-treebeard';
import { BsCaretRightFill, BsCaretDownFill } from 'react-icons/bs'
import treeData from "./data.json"

const CustomHeader = ({ node, style, onToggle }) => {
    const colorPalette = {
        "module": "#EE9949",
        "varaible": "#A8A8FF",
        "class": "#FF4747",
        "function": "#04EB00",
        "parameter": "#CF4DFF",
        "import": "#1DFCCF"
    }

    const getColor = (node) => {
        if ("attributes" in node) {
            if ("type" in node.attributes) {
                return colorPalette[node.attributes.type]
            }
        }

        return null
    }

    return (
        <div style={style.base}>
        <div onclick={onToggle} style={{ ...style.title, display: "flex", alignItems: "center", gap:"3px"}}>
            {node.children ? node.toggled ? <BsCaretDownFill size={15}/> : <BsCaretRightFill size={15}/> : null}
            <div style={{marginLeft: !node.children ? "10px" : null, color: getColor(node)}}>
                {`${node.name} `}
            </div>
        </div>
        </div>
    );
};

const CustomToggle = ({ node, style }) => {
    return (
        <div/>
    );
};

const Tree = () => {
    const [data, setData] = useState(treeData);
    const [cursor, setCursor] = useState(false);

    const onToggle = (node, toggled) => {
        if (cursor) {
            cursor.active = false;
        }
        node.active = true;
        if (node.children) {
            node.toggled = toggled;
        }
        setCursor(node);
        setData(Object.assign({}, data))
    }
    
    return (
       <Treebeard data={data} decorators={{...decorators, Header:CustomHeader, Toggle:CustomToggle}} onToggle={onToggle}/>
    )
}

export default Tree