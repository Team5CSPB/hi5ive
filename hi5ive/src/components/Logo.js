import React from 'react';
import logo from './assets/images/logo.png';
import '../styles/HelloPage.css'
function Logo(){
  return (
    <img
      src={logo}
      alt="logo"
      style={{ width: '200px', height: '200px', cursor: 'pointer' }}

    />
  );
}
export default Logo;