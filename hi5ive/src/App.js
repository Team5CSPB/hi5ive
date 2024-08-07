import React, { useState, useEffect } from 'react'
import {
	BrowserRouter as Router,
	Routes,
	Route,
	Navigate,
} from 'react-router-dom'
import 'semantic-ui-css/semantic.min.css'
import SignUp from './components/SignUp.js'
import './App.css'
import { Profile } from './components/Profile'
import { UserGrid } from './components/UserGrid'
import Navbar from './components/Navbar'
import Logo from './components/Logo'
import LoginPage from './pages/LoginPage'
import HelloPage from './pages/HelloPage'
import axios from 'axios';
import DummyData from './DummyData.json';

const user = {
	id: 6,
	status: 'active',
	name: 'Hedy Lamar',
	hobbies: ['singing', 'dancing'],
	matches: ['trekking', 'cooking'],
	interests: ['movies', 'sports'],
	about: 'I am a singer and dancer',
	imageUrl: 'https://i.imgur.com/yXOvdOSs.jpg',
}

function App() {

	const handleAddMatch = (user) => {
    setLoggedInUser(prevState => ({
      ...prevState,
      matches: [...prevState.matches, user.firstname + ' ' + user.lastname],
    }));
  };


	const [loggedInUser, setLoggedInUser] = useState(null)

	// EXAMPLE Get the user object from the backend
	// should change localhost:5000 to the actual backend URL if we deploy the backend

	// const [users, setUsers] = useState([])

	// useEffect(() => {
	// 	// Function to fetch data from the backend
	// 	const fetchUser = async () => {
	// 		try {
	// 			const response = await fetch('http://localhost:5000/users')
	// 			const text = await response.text() // Get the response as text
	// 			if (text) {
	// 				const data = JSON.parse(text) // Parse the text to JSON if it's not empty
	// 				setUsers(data) // Assuming the response is the user object
	// 			} else {
	// 				console.error('Error fetching user: Response is empty')
	// 			}
	// 		} catch (error) {
	// 			console.error('Error fetching user:', error)
	// 		}
	// 	}

	// 	fetchUser()
	// }, []) // Empty dependency array means this effect runs once when the component mounts

	// EXAMPLE Get users by interest
	const [searchTerm, setSearchTerm] = useState('');
	const [usersByInterest, setUsersByInterest] = useState([])

	const handleSearch = (term) =>{
		setSearchTerm(term);
	}

	// const fetchUsersByInterest = async (interest) => {
	// 	try {
	// 		console.log("called fetchusers by interest");
	// 		const response = await fetch(
	// 			`http://localhost:5000/users/interests/${interest}`
	// 		)
	// 		const text = await response.text() // Get the response as text
	// 		if (text) {
	// 			const data = JSON.parse(text) // Parse the text to JSON if it's not empty
	// 			setUsersByInterest(data) // Assuming the response is the user object
	// 		} else {
	// 			console.error('Error fetching users by interest: Response is empty')
	// 		}
	// 	} catch (error) {
	// 		console.error('Error fetching users by interest:', error)
	// 	}
	// }

	// FETCH USERS USING AXIOS
	// const fetchUsersByInterest = async (interest) => {
  //   const response = await axios.get(`http://localhost:5000/users/interests/${interest}`);
  //   console.log('RESPONSE DATA FOR INTEREST: HIKING: ', response.data);
  //   setUsersByInterest(response.data);
  // };


	// Dummy Data using JSON

// handlesearch  take the given interest
	// const handleSearch = (interest) => {
	// 	setSearchTerm(interest)
	// 	if (searchTerm) {
	// 		fetchUsersByInterest(searchTerm)
	// 	}
	// }

   // logout handler sets the user login to null, logs them out -
	const handleLogout = () => {
		setLoggedInUser(null);
	}


	// render
	return (
		<div className="App">
			<div className="container">
				<Router>
					{loggedInUser && (
						<Navbar
							user={loggedInUser}
							onLogout={handleLogout}
							handleSearch={handleSearch}
						/>
					)}
					{/* Conditionally render Navbar */}
					<Routes>
						<Route
							path="/"
							element={<HelloPage />}
						/>
						<Route
							path="/login"
							element={<LoginPage setLoggedInUser={setLoggedInUser} />}
						/>
						<Route
							path="/users"
							element={loggedInUser ? <UserGrid searchTerm={searchTerm} onAddMatch={handleAddMatch}  /> : <Navigate to="/login" />}
						/>
						<Route
							path="/SignUp"
							element={<SignUp />}
						/>
						<Route
							path="/my-profile"
							element={
								loggedInUser ? (
									<Profile user={loggedInUser} />
								) : (
									<Navigate to="/login" />
								)
							}
						/>
						<Route
							path="*"
							// !!!!!!!!!!!!!!!!!!!! copy and paste when finsihed with profile !!!!!!!!!!!!!!!!!!!!
							// {loggedInUser ? '/users' : '/'}
							element={<Navigate to={loggedInUser ? '/users' : '/'} />}
						/>
					</Routes>
				</Router>
			</div>
		</div>
	)
}

export default App
