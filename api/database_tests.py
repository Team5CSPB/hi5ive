import psycopg2
from psycopg2 import sql

def run_query(conn, query, data=None):
    with conn.cursor() as cur:
        cur.execute(query, data)
        conn.commit()

def test_users_table(conn):
    # Insert a new user
    try:
        run_query(conn, """
            INSERT INTO Users (username, email, password_hash, first_name, last_name)
            VALUES (%s, %s, %s, %s, %s)
        """, ('testuser', 'testuser@example.com', 'hashedpassword', 'Test', 'User'))
        print("Insert new user: Passed")
    except Exception as e:
        print(f"Insert new user: Failed ({e})")

    # Unique username and email
    try:
        run_query(conn, """
            INSERT INTO Users (username, email, password_hash, first_name, last_name)
            VALUES (%s, %s, %s, %s, %s)
        """, ('testuser', 'anotheremail@example.com', 'hashedpassword', 'Another', 'User'))
        print("Unique username: Failed")
    except Exception as e:
        print(f"Unique username: Passed ({e})")

    try:
        run_query(conn, """
            INSERT INTO Users (username, email, password_hash, first_name, last_name)
            VALUES (%s, %s, %s, %s, %s)
        """, ('anotheruser', 'testuser@example.com', 'hashedpassword', 'Another', 'User'))
        print("Unique email: Failed")
    except Exception as e:
        print(f"Unique email: Passed ({e})")

    # Update user information
    try:
        run_query(conn, """
            UPDATE Users
            SET first_name = %s, last_name = %s
            WHERE username = %s
        """, ('Updated', 'User', 'testuser'))
        print("Update user information: Passed")
    except Exception as e:
        print(f"Update user information: Failed ({e})")

    # Delete user
    try:
        run_query(conn, """
            DELETE FROM Users
            WHERE username = %s
        """, ('testuser',))
        print("Delete user: Passed")
    except Exception as e:
        print(f"Delete user: Failed ({e})")

def test_interests_table(conn):
    # Insert a new interest
    try:
        run_query(conn, """
            INSERT INTO Interests (name)
            VALUES (%s)
        """, ('Hiking',))
        print("Insert new interest: Passed")
    except Exception as e:
        print(f"Insert new interest: Failed ({e})")

    # Unique interest name
    try:
        run_query(conn, """
            INSERT INTO Interests (name)
            VALUES (%s)
        """, ('Hiking',))
        print("Unique interest name: Failed")
    except Exception as e:
        print(f"Unique interest name: Passed ({e})")

    # Update interest name
    try:
        run_query(conn, """
            UPDATE Interests
            SET name = %s
            WHERE name = %s
        """, ('Mountain Climbing', 'Hiking'))
        print("Update interest name: Passed")
    except Exception as e:
        print(f"Update interest name: Failed ({e})")

    # Delete interest
    try:
        run_query(conn, """
            DELETE FROM Interests
            WHERE name = %s
        """, ('Mountain Climbing',))
        print("Delete interest: Passed")
    except Exception as e:
        print(f"Delete interest: Failed ({e})")

def test_user_interests_table(conn):
    # Link user to interest
    try:
        run_query(conn, """
            INSERT INTO User_Interests (user_id, interest_id)
            VALUES (%s, %s)
        """, (1, 1))
        print("Link user to interest: Passed")
    except Exception as e:
        print(f"Link user to interest: Failed ({e})")

    # Unique user-interest combination
    try:
        run_query(conn, """
            INSERT INTO User_Interests (user_id, interest_id)
            VALUES (%s, %s)
        """, (1, 1))
        print("Unique user-interest combination: Failed")
    except Exception as e:
        print(f"Unique user-interest combination: Passed ({e})")

    # Delete user-interest link
    try:
        run_query(conn, """
            DELETE FROM User_Interests
            WHERE user_id = %s AND interest_id = %s
        """, (1, 1))
        print("Delete user-interest link: Passed")
    except Exception as e:
        print(f"Delete user-interest link: Failed ({e})")

def test_matches_table(conn):
    # Create a match
    try:
        run_query(conn, """
            INSERT INTO Matches (user1_id, user2_id, status)
            VALUES (%s, %s, %s)
        """, (1, 2, 'pending'))
        print("Create a match: Passed")
    except Exception as e:
        print(f"Create a match: Failed ({e})")

    # Update match status
    try:
        run_query(conn, """
            UPDATE Matches
            SET status = %s
            WHERE user1_id = %s AND user2_id = %s
        """, ('accepted', 1, 2))
        print("Update match status: Passed")
    except Exception as e:
        print(f"Update match status: Failed ({e})")

    # Delete a match
    try:
        run_query(conn, """
            DELETE FROM Matches
            WHERE user1_id = %s AND user2_id = %s
        """, (1, 2))
        print("Delete a match: Passed")
    except Exception as e:
        print(f"Delete a match: Failed ({e})")

def main():
    conn = psycopg2.connect(
        dbname='hifive_db',
        user='hifive_db_user',
        password='04eNJnua5k8jJ7OW4Y276Vemse291F3d',
        host='dpg-cqm62u3qf0us73a5si30-a.oregon-postgres.render.com',
        port='5432'
    )

    try:
        test_users_table(conn)
        test_interests_table(conn)
        test_user_interests_table(conn)
        test_matches_table(conn)
    finally:
        conn.close()

if __name__ == "__main__":
    main()
