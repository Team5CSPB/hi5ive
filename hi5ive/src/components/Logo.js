import React from 'react';
import logo from './assets/images/logo.png';
function Logo(){
  return (
    <img src={logo} alt="logo" style = {{ width:"200px", height: "200px"}} />
  );
}
export default Logo;