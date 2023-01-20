import React, {useState} from 'react'

export default function Form(props) {
    const changeUpper= ()=>{
        let newText = text.toUpperCase();
        // console.log("Hi How are You" + text)
        setText(newText);
    }
    
    const ChangeTo = (event)=>{
        // console.log("I am Find And You")
        setText(event.target.value)

    }

    const changeLower = () =>{
        let Newtext = text.toLowerCase();
        setText(Newtext);
    }

    const ClearText=()=>{
        setText(' ')
    }

    const [text,setText]= useState("")
    
    return (
    
    <div>
      <>
      <div className="container2">
        <textarea name="" id="" cols="30" rows="8" onChange={ChangeTo} value={text}></textarea>
      </div>
      <div>
        <button onClick={changeUpper}>Conver Upper Case</button>
        <button onClick={changeLower} className="btn">Conver Lower Case</button>
        <button onClick={ClearText} className="btn2">Clear Text</button>
      </div>
      <div className="container2">
        <h1>Your Text Summary</h1>
        <p>{text.split(" ").length} world and {text.length} characters</p>
        <p>{0.580*text.split(" ").length}  Mints Need To Read</p>
        <h2>Preview</h2>
        <p>{text}</p>
      </div>
      </>
    </div>
  )
}
