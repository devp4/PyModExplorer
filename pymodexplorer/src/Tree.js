import React, { useState } from 'react';
import { Treebeard, decorators  } from 'react-treebeard';
import { BsCaretRightFill, BsCaretDownFill } from 'react-icons/bs'

const CustomHeader = ({ node, style, onToggle }) => {
    const colorPalette = {
        "module": "#EE9949",
        "variable": "#A8A8FF",
        "class": "#FF4747",
        "function": "#39DB49",
        "parameter": "#CF4DFF",
        "import": "#FF8AE6  "
    }

    const getColor = (node) => {
        if ("attributes" in node) {
            if ("type" in node.attributes) {
                return colorPalette[node.attributes.type]
            }
        }

        return "#BFBFBF"
    }

    return (
        <div style={style.base}>
        <div onclick={onToggle} style={{ ...style.title, display: "flex", alignItems: "center", gap:"3px"}}>
            {node.children ? node.toggled ? <BsCaretDownFill size={14}/> : <BsCaretRightFill size={14}/> : null}
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

const customStyles = {
    tree: {
        base: {
          listStyle: 'none',
          backgroundColor: '#303030',
          margin: 0,
          color: '#9DA5AB',
          fontFamily: 'lucida grande ,tahoma,verdana,arial,sans-serif',
          fontSize: '20px'
        },

        node: {
            base: {
                marginTop: 17,
                marginBottom: 17,
                marginLeft: 15
            },
            activeLink: {
                background: '#424242'
            }
        }
    }
}

const Tree = ({ file, setFile }) => {
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
        setFile(Object.assign({}, file))
    }
		
    return (
       <Treebeard data={file} decorators={{...decorators, Header:CustomHeader, Toggle:CustomToggle}} onToggle={onToggle} style={customStyles}/>
    )
}

export default Tree