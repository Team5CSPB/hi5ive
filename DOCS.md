# Hi 5ive

Hi 5ive is a social matching site designed to connect users with similar interests. The project is built with a focus on scalability, reliability, and an engaging user experience.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Architecture](#architecture)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)
6. [Database Schema](#database-schema)
7. [License](#license)

## Project Overview

Hi 5ive aims to create a platform where users can match with others who share similar interests, goals, or hobbies. The matching algorithm takes into account user preferences and activity to provide meaningful connections.

## Features

- **User Registration & Authentication**: Secure user sign-up and login process.
- **Profile Management**: Users can create and manage their profiles, including interests, preferences, and other personal details.
- **Matching Algorithm**: Sophisticated algorithm to match users based on their profiles and preferences.
- **PostgreSQL Database**: Reliable and scalable database management for storing user data and matches.

## Architecture

Hi 5ive is built using a modern web stack:

- **Frontend**: React.js
- **Backend**: Flask
- **Database**: PostgreSQL
- **Deployment**: Render

### High-Level Architecture

```plaintext
+----------------+        +---------------------+        +------------------+
|   Frontend     | <----> |    Backend API      | <----> |  PostgreSQL DB   |
| (React.js)     |        |   (Flask)           |                  |
+----------------+        +---------------------+        +------------------+
```

## Installation



## Usage
Once the application is running, you can access it at http://localhost:3000. Sign up or log in to start using the platform.


## API Endpoints

Here’s a list of the main API endpoints:

1. **Get All Users**
   - **Endpoint**: `/users`
   - **Method**: `GET`
   - **Description**: Fetches all users from the database.
   - **Response**: JSON list of all users.

2. **Get User by ID**
   - **Endpoint**: `/user/<int:user_id>`
   - **Method**: `GET`
   - **Description**: Fetches a specific user by their ID.
   - **Response**: JSON object of the user's details or 404 if not found.

3. **Create a Match**
   - **Endpoint**: `/create_match`
   - **Method**: `POST`
   - **Description**: Creates a match between two users.
   - **Response**: JSON object of the match details or appropriate error message.

4. **Get Matches for a User**
   - **Endpoint**: `/matches/<int:user_id>`
   - **Method**: `GET`
   - **Description**: Returns the profiles of users matched to the given user ID.
   - **Response**: JSON list of matched users or 404 if the user is not found.

5. **Get Users by Interest**
   - **Endpoint**: `/users/interest/<string:interest>`
   - **Method**: `GET`
   - **Description**: Fetches users who share a specific interest.
   - **Response**: JSON list of users sharing the interest or 404 if the interest is not found.

### To Be Implemented Routes

6. **User Login** (Commented Out)
   - **Endpoint**: `/login`
   - **Method**: `POST`
   - **Description**: Handles user login by checking username and password.
   - **Response**: JSON object of the user's details upon successful login or appropriate error message.
   - **Status**: Not fully implemented (commented out).

7. **User Signup**
   - **Endpoint**: `/signup`
   - **Method**: `POST`
   - **Description**: Placeholder for user signup functionality.
   - **Response**: Placeholder response.

8. **User Logout**
   - **Endpoint**: `/logout`
   - **Method**: `POST`
   - **Description**: Placeholder for user logout functionality.
   - **Response**: Placeholder response.


## Database Schema

The database is designed to store user data, interests, and matches efficiently. Here's an overview of the schema:

- **Users**: Stores user details including username, email, password hash, personal information like first name and last name, optional bio, profile picture, location, and timestamps for record creation and updates.

- **Interests**: Stores interest names that users can associate with their profiles. Each interest has a unique name and timestamps for when it was created and last updated.

- **User_Interests**: Manages the many-to-many relationship between users and their interests. It links user IDs to interest IDs, ensuring that each user can have multiple interests without duplication.

- **Matches**: Stores match data linking two users together, including the status of the match (e.g., 'pending', 'accepted', 'rejected') and the timestamp for when the match was created.


## License

This project is licensed under the MIT License.


