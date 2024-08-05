DROP TABLE IF EXISTS Users;

DROP TABLE IF EXISTS Interests;

DROP TABLE IF EXISTS User_Interests;

DROP TABLE IF EXISTS Matches;

-- Users Table
CREATE TABLE
    Users (
        id SERIAL PRIMARY KEY,
        username TEXT UNIQUE NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        bio TEXT,
        profile_picture TEXT,
        location TEXT,
        created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
    );

-- Interests Table
CREATE TABLE
    Interests (
        id SERIAL PRIMARY KEY,
        name TEXT UNIQUE NOT NULL,
        created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP
    );

-- User_Interests Table
CREATE TABLE
    User_Interests (
        id SERIAL PRIMARY KEY,
        user_id INT NOT NULL,
        interest_id INT NOT NULL,
        created_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES Users (id),
        FOREIGN KEY (interest_id) REFERENCES Interests (id),
        UNIQUE (user_id, interest_id)
    );

-- Matches Table
CREATE TABLE
    Matches (
        id SERIAL PRIMARY KEY,
        user1_id INT NOT NULL,
        user2_id INT NOT NULL,
        matched_at TIMESTAMPTZ DEFAULT CURRENT_TIMESTAMP,
        status TEXT CHECK (status IN ('pending', 'accepted', 'rejected')),
        FOREIGN KEY (user1_id) REFERENCES Users (id),
        FOREIGN KEY (user2_id) REFERENCES Users (id)
    );