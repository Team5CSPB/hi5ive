import React, { useState } from 'react';
import Logo from './Logo'; // Import the Logo component
import '../styles/SignUp.css'; // Ensure correct path to your CSS

function SignUp() {
    const [email, setEmail] = useState('');
    const [firstName, setFirstName] = useState('');
    const [lastName, setLastName] = useState('');
    const [username, setUsername] = useState('');
    const [birthday, setBirthday] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [error, setError] = useState('');

    const validateEmail = (email) => {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    };

    const validatePasswords = () => {
        if (!password || !confirmPassword) {
            setError('Please enter both password fields.');
            return false;
        }
        if (password !== confirmPassword) {
            setError('Passwords do not match.');
            return false;
        }
        if (password.length < 8) {
            setError('Password must be at least 8 characters long.');
            return false;
        }
        if (!/[A-Z]/.test(password)) {
            setError('Password must contain at least one uppercase letter.');
            return false;
        }
        if (!/\d/.test(password)) {
            setError('Password must contain at least one number.');
            return false;
        }
        if (!/[!@#$%^&*(),.?":{}|<>]/.test(password)) {
            setError('Password must contain at least one special character.');
            return false;
        }
        return true;
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        setError('');
        if (!validateEmail(email)) {
            setError('Please enter a valid email address.');
            return;
        }

        if (validatePasswords()) {
            // Submit the form 
            console.log('Form submitted');
        }
    };

    const LogoClick = () => {
        window.location.href = '/';
    };

    const loginClick = () => {
        window.location.href = '/login';
    };

    return (
        <div className="SignUpPage">
            <header className="App-header">
                <Logo onClick={LogoClick} /> {/* Use Logo component */}
                <h1>Sign up to hi5ive someone with the same interests as you and connect on a deeper level</h1>
                <hr className="App-hr" />
            </header>
            <div className='SignUp'>
                <input
                    type="text"
                    name="email"
                    placeholder='Email'
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                />
                <input
                    type="text"
                    name="firstName"
                    placeholder='First Name'
                    value={firstName}
                    onChange={(e) => setFirstName(e.target.value)}
                />
                <input
                    type="text"
                    name="lastName"
                    placeholder='Last Name'
                    value={lastName}
                    onChange={(e) => setLastName(e.target.value)}
                />
                <input
                    type="text"
                    name="username"
                    placeholder='Username'
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                />
                <input
                    type="date"
                    id="birthday"
                    name="birthday"
                    value={birthday}
                    onChange={(e) => setBirthday(e.target.value)}
                />
                <input
                    type="password"
                    name="password"
                    placeholder='Password'
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                />
                <input
                    type="password"
                    name="confirmPassword"
                    placeholder='Confirm Password'
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                />
                <button onClick={handleSubmit} className="submitButton">Sign Up</button>
                {error && <div className="Error">{error}</div>}
            </div>
            <div className='Member'>
                <h1>Already a member?</h1>
                <button onClick={loginClick} className="authButton">
                    Login
                </button>
            </div>
        </div>
    );
}

export default SignUp;
