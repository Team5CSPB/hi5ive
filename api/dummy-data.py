import requests
import psycopg2
import configparser

# Database connection parameters
config = configparser.ConfigParser()

# Read the configuration file
config.read('config.ini')

def run_sql_script(filename):
    with open(filename, 'r') as file:
        sql_script = file.read()

    conn = psycopg2.connect(
        dbname=config['database']['dbname'],
        user=config['database']['user'],
        password=config['database']['password'],
        host=config['database']['host'],
        port=config['database']['port']
    )
    cursor = conn.cursor()
    cursor.execute(sql_script)
    conn.commit()
    cursor.close()
    conn.close()

def generate_avatar_url():
    response = requests.get('https://randomuser.me/api/')
    data = response.json()
    return data['results'][0]['picture']['large']

def insert_dummy_data():
    # Connect to the database
    conn = psycopg2.connect(
        dbname=config['database']['dbname'],
        user=config['database']['user'],
        password=config['database']['password'],
        host=config['database']['host'],
        port=config['database']['port']
    )
    cursor = conn.cursor()

    # Dummy data
    # Insert dummy data into Users table
    users = [
        ('john_doe', 'john@example.com', 'hashed_password_1', 'John', 'Doe', 'Bio for John Doe', 'profile_pic_1.jpg', 'Location 1'),
        ('jane_smith', 'jane@example.com', 'hashed_password_2', 'Jane', 'Smith', 'Bio for Jane Smith', 'profile_pic_2.jpg', 'Location 2'),
        ('alice_jones', 'alice@example.com', 'hashed_password_3', 'Alice', 'Jones', 'Bio for Alice Jones', 'profile_pic_3.jpg', 'Location 3')
    ]

    # Insert data into Users table
    insert_user_query = """
    INSERT INTO Users (username, email, password_hash, first_name, last_name, bio, profile_picture, location)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    RETURNING id
    """
    user_ids = []
    for user in users:
        cursor.execute(insert_user_query, user)
        user_id = cursor.fetchone()[0]
        user_ids.append(user_id)

    # Insert dummy data into Interests table
    interests = ['hiking', 'reading', 'cooking', 'traveling', 'gaming']
    insert_interests_query = "INSERT INTO Interests (name) VALUES (%s) RETURNING id"
    interest_ids = []
    for interest in interests:
        cursor.execute(insert_interests_query, (interest,))
        interest_id = cursor.fetchone()[0]
        interest_ids.append(interest_id)

    # Insert dummy data into User_Interests table
    user_interests = [
        (user_ids[0], interest_ids[0]), # John Doe likes Hiking
        (user_ids[0], interest_ids[1]), # John Doe likes Reading
        (user_ids[1], interest_ids[2]), # Jane Smith likes Cooking
        (user_ids[1], interest_ids[3]), # Jane Smith likes Traveling
        (user_ids[2], interest_ids[4])  # Alice Jones likes Gaming
    ]
    insert_user_interests_query = "INSERT INTO User_Interests (user_id, interest_id) VALUES (%s, %s)"
    for user_interest in user_interests:
        cursor.execute(insert_user_interests_query, user_interest)

    # Insert dummy data into Matches table
    matches = [
        (user_ids[0], user_ids[1]), # John Doe matched with Jane Smith
        (user_ids[1], user_ids[2])  # Jane Smith matched with Alice Jones
    ]
    insert_matches_query = "INSERT INTO Matches (user1_id, user2_id, matched_at) VALUES (%s, %s, CURRENT_TIMESTAMP)"
    for match in matches:
        cursor.execute(insert_matches_query, match)

    # Commit the transaction
    conn.commit()

    # Close the connection
    cursor.close()
    conn.close()

def test_dummy_data():
    # Connect to the database
    conn = psycopg2.connect(
        dbname=config['database']['dbname'],
        user=config['database']['user'],
        password=config['database']['password'],
        host=config['database']['host'],
        port=config['database']['port']
    )
    cursor = conn.cursor()

    # Query and print Users table
    cursor.execute("SELECT * FROM Users;")
    users = cursor.fetchall()
    print("Users Table:")
    for user in users:
        print(user)

    # Query and print Interests table
    cursor.execute("SELECT * FROM Interests;")
    interests = cursor.fetchall()
    print("\nInterests Table:")
    for interest in interests:
        print(interest)

    # Query and print User_Interests table
    cursor.execute("SELECT * FROM User_Interests;")
    user_interests = cursor.fetchall()
    print("\nUser_Interests Table:")
    for user_interest in user_interests:
        print(user_interest)

    # Query and print Matches table
    cursor.execute("SELECT * FROM Matches;")
    matches = cursor.fetchall()
    print("\nMatches Table:")
    for match in matches:
        print(match)

    # Close the connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    run_sql_script('postgres-db.sql')
    insert_dummy_data()
    test_dummy_data()