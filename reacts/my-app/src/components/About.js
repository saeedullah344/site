import React, { useState } from 'react'

export default function About(props) {

  const [myStyle, mystyle] = useState({
    color: 'black',
    backgroundColor: 'white'

  })

  const changecolor = () => {
    if (myStyle.color === 'white') {
      mystyle({
        color: 'green',
        backgroundColor: 'red'
      })
    }
    else {
      mystyle({
        color: 'red',
        backgroundColor: 'green'
      })
    }
  }
  return (
    <div>
      <>
        <div className="container3" style={myStyle}>
          <h1>WELLCOME TO MY CONTACT PAGE</h1>
          <p>Lorem ipsum dolor, sit amet consectetur adipisicing elit. Nemo eveniet nobis odit, natus, eligendi, molestiae debitis itaque quis doloribus ea eos tenetur totam consequuntur voluptatum assumenda architecto nisi rerum cumque?</p>
        </div>
        <button onClick={changecolor}>Enable Dark Mode</button>
      </>
    </div>
  )
}
