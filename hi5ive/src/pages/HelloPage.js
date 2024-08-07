import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Logo from '../components/Logo.js';
import ImageSlider from '../components/ImageSlider.js';
import '../styles/HelloPage.css'
import {Button} from 'semantic-ui-react';
// PLANNING:
// an about div
  // a logo in the top left corner
// a slideshow div
  // scrollable pictures
// call to action div
  // one button that takes the user to /login
  // one button that directs the user to /signup

function HelloPage(){
  const navigate = useNavigate();
  //login handler
const loginClick = () =>{
  navigate("/login"); // navigate to the login page
  console.log("login button clicked");
}
//signup handler
const signupClick = () => {
  navigate("/signup");
  console.log("Signup button clicked");
}


return (
  <div>
    <div className="About">
      <div className="Logo Container">
        <Logo/>
        </div>
    <div className="Info">
  <h1>About HI5IVE</h1>
  <p>Have you ever felt isolated and secluded when trying to enjoy your favorite activities?
    Now you can reach out and simply Hi5ive’d someone with the same interests.
    With Hi5ive, we aim to connect users on a deeper level based on their common interests and hobbies.
    Before the popularity of technology,making friends was just by a matter of convenience.
     Most of our friends either went to the same school or grew up in the same neighborhood.
      Times have changed and the more we connect with our devices the harder it is to find actual human interaction.
      We want to leverage these devices to encourage face to face human interaction with the Hi5ive application.

</p>
    </div>
  </div>

  <div className="Scrollshow">
  <h1>CREATE MEMORIES TOGETHER</h1>
  {/* should have some sort of scrollable pictures with a nav bar  */}
   <ImageSlider/>
  </div>


  <div className="calltoaction">
  <h1>BECOME A 5IVER</h1>
  {/* Buttons here */}
  <Button primary onClick={signupClick} className="authButton">
    SIGNUP
  </Button>
  <Button  secondary onClick={loginClick} className="authButton">
    LOGIN
  </Button>
  </div>
</div>
  );
}





export default HelloPage;