import React, { useState } from 'react';
import Logo from '../components/Logo.js';
import { useNavigate } from 'react-router-dom';
import Navbar from '../components/Navbar';
import '../styles/LoginPage.css';
import {Button} from 'semantic-ui-react';

// LOGIN PAGE
// two fields for username and password , and input error handling
// a login button
// if sucessful, will return the matches page
 // Brandname and Logo
function LoginPage({setLoggedInUser}){
  // hooks to use state in functional components
  // const [state,setState] = useState(initialValue)
  //state: The current state value.
  //setState: Function to update the state.
  //initialValue: The initial state value.

  const navigate = useNavigate();

  const [username,setUsername] =  useState('');
  const [password,setPassword] =  useState('');
  const [error, setError] = useState('');
  // Dummy user data from App.js
  const dummyUser = {
    id: 6,
    status: 'active',
    name: 'Hedy Lamar',
    hobbies: ['singing', 'dancing'],
    groups: ['trekking', 'cooking'],
    interests: ['movies', 'sports'],
    about: 'I am a singer and dancer',
    imageUrl: 'https://i.imgur.com/yXOvdOSs.jpg',
  };

  const onButtonClick = () => {
    // update this function later with more detailed login requirements
    // initial error condititons: if there is no username or password
    if (! username|| !password){
      setError("Please enter both a name and a password");
    }

    // login logic
      // correct login logic - can edit later - to integrate proper backend & db
      // JSON stringify username and password, send to backend login using DB info
      // initial login condition: admin username and password is just password
    if (username === "admin" && password === "password"){
      // window.location - gets current url and redirects user to a URL
      // set windown url to /matches
      // update to use the backend to return the users specific match  page
        setLoggedInUser(dummyUser);
        navigate("/users")
    }
    else {
      // sets the error variable to have a value
      setError("Invalid username or password")
    }
  }

  return (
    <div className="MainContainer">
      <div className="Hi5brandContainer">
      <h1>HI5IVE</h1>
        <div className="LogoContainer">
          <Logo />
        </div>
      </div>
      {/* state is used to
      */}
      <div className="InputContainer">
        <input
        value={username}
        placeholder="Username"
         onChange = {(e) => setUsername(e.target.value)}
         className="inputBox"/>
      </div>
      <br />
      <div className={"InputContainer"}>
        <input
        type="password"
        value={password}
        placeholder="Password"
        onChange ={(e) =>setPassword(e.target.value)}
        className ="inputBox"
        />
      </div>
      <br />
      {/* will conditionally render an error message if the 'error' state variable contains a value
      is a short circuit evaluation- if err is truthy, then the code following && will be rendered
      if error has a value the div will be rendered, which shows the error message
      */}
      {error && <div className="Error">{error}</div>}
      <br />
      <div className="InputContainer">
        <Button
        primary
        onClick={onButtonClick}
        >
          Login
        </Button>
        </div>
      </div>
  );
}

export default LoginPage;