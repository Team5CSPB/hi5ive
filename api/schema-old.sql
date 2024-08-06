DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Interests;
DROP TABLE IF EXISTS User_Interests;
DROP TABLE IF EXISTS Matches;

-- Users Table
CREATE Table Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    bio TEXT,
    profile_picture TEXT,
    location TEXT
);

-- Interests Table
CREATE Table Interests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name UNIQUE NOT NULL
);

-- User_Interests Table
CREATE Table User_Interests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INT NOT NULL,
    interest_id INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (interest_id) REFERENCES Interests(id)
);

-- Matches Table
CREATE Table Matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user1_id INT NOT NULL,
    user2_id INT NOT NULL,
    status TEXT CHECK (status IN ('pending', 'accepted', 'rejected')),
    FOREIGN KEY (user1_id) REFERENCES Users(id),
    FOREIGN KEY (user2_id) REFERENCES Users(id)
);