import React, { useState } from 'react';
import Logo from './Logo.js';
import Navbar from './Navbar.js';
import ImageSlider from './ImageSlider.js';
// PLANNING:
// an about div
  // a logo in the top left corner
// a slideshow div
  // scrollable pictures
// call to action div
  // one button that takes the user to /login
  // one button that directs the user to /signup

function HelloPage(){

// intilaize variables :
//login
const loginClick = () => {
  window.location.href = '/login';
}
//signup
const signupClick = () =>{
window.location.href = '/signup';
}

return (
  <div>
    <div className="About">
  <h1>About HI5IVE</h1>
  <Logo/>
  <p>desc/summary about our business message</p>
  </div>

  <div className="Scrollshow">
  <h1>CREATE MEMORIES TOGETHER</h1>
  {/* should have some sort of scrollable pictures with a nav bar  */}
   <ImageSlider/>
  </div>


  <div className="calltoaction">
  <h1>BECOME A 5IVER</h1>
  {/* Buttons here */}
  <button onClick={signupClick} className="authButton">
    SIGNUP
  </button>
  <button onClick={loginClick} className="authButton">
    LOGIN
  </button>
  </div>
</div>
  );
}





export default HelloPage;