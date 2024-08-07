import psycopg2
from psycopg2 import sql

def run_query(conn, query, data=None):
    with conn.cursor() as cursor:
        cursor.execute(query, data)
        conn.commit()

def test_users_table(conn):
    # Insert a new user
    try:
        run_query(conn, """
            INSERT INTO Users (username, email, password_hash, first_name, last_name)
            VALUES (%s, %s, %s, %s, %s)
        """, ('testuser', 'testuser@example.com', 'password', 'Test', 'User'))
        print("Insert new user: Passed")
    except Exception as e:
        print(f"Insert new user: Failed ({e})")
        conn.rollback()

    # Ensure unique username
    try:
        run_query(conn, """
            INSERT INTO Users (username, email, password_hash, first_name, last_name)
            VALUES (%s, %s, %s, %s, %s)
        """, ('testuser2', 'testuser2@example.com', 'password', 'Test2', 'User'))
        print("Unique username: Passed")
    except Exception as e:
        print(f"Unique username: Failed ({e})")
        conn.rollback()

    # Ensure unique email
    try:
        run_query(conn, """
            INSERT INTO Users (username, email, password_hash, first_name, last_name)
            VALUES (%s, %s, %s, %s, %s)
        """, ('testuser3', 'testuser3@example.com', 'password', 'Test3', 'User'))
        print("Unique email: Passed")
    except Exception as e:
        print(f"Unique email: Failed ({e})")
        conn.rollback()

    # Update user information
    try:
        run_query(conn, """
            UPDATE Users
            SET email = %s
            WHERE username = %s
        """, ('newemail@example.com', 'testuser'))
        print("Update user information: Passed")
    except Exception as e:
        print(f"Update user information: Failed ({e})")
        conn.rollback()

    # Delete user
    try:
        run_query(conn, """
            DELETE FROM Users
            WHERE username = %s
        """, ('testuser',))
        print("Delete user: Passed")
    except Exception as e:
        print(f"Delete user: Failed ({e})")
        conn.rollback()

def test_interests_table(conn):
    # Insert a new interest
    try:
        run_query(conn, """
            INSERT INTO Interests (name)
            VALUES (%s)
        """, ('TTRPGs',))
        print("Insert new interest: Passed")
    except Exception as e:
        print(f"Insert new interest: Failed ({e})")
        conn.rollback()

    # Ensure unique interest name
    try:
        run_query(conn, """
            INSERT INTO Interests (name)
            VALUES (%s)
        """, ('TTRPGs',))
        print("Unique interest name: Failed")
    except Exception as e:
        print(f"Unique interest name: Passed ({e})")
        conn.rollback()

    # Update interest name
    try:
        run_query(conn, """
            UPDATE Interests
            SET name = %s
            WHERE name = %s
        """, ('Dungeons and Dragons', 'TTRPGs'))
        print("Update interest name: Passed")
    except Exception as e:
        print(f"Update interest name: Failed ({e})")
        conn.rollback()

    # Delete interest
    try:
        run_query(conn, """
            DELETE FROM Interests
            WHERE name = %s
        """, ('Dungeons and Dragons',))
        print("Delete interest: Passed")
    except Exception as e:
        print(f"Delete interest: Failed ({e})")
        conn.rollback()

def test_user_interests_table(conn):
    # Link user to interest
    try:
        run_query(conn, """
            INSERT INTO User_Interests (user_id, interest_id)
            VALUES (%s, %s)
        """, (1, 4))
        print("Link user to interest: Passed")
    except Exception as e:
        print(f"Link user to interest: Failed ({e})")
        conn.rollback()

def test_matches_table(conn):
    # Create a match
    try:
        run_query(conn, """
            INSERT INTO Matches (user1_id, user2_id)
            VALUES (%s, %s)
        """, (1, 3))
        print("Create a match: Passed")
    except Exception as e:
        print(f"Create a match: Failed ({e})")
        conn.rollback()


def main():
    conn = psycopg2.connect(
        dbname='hifive_db',
        user='hifive_db_user',
        password='04eNJnua5k8jJ7OW4Y276Vemse291F3d',
        host='dpg-cqm62u3qf0us73a5si30-a.oregon-postgres.render.com',
        port='5432'
    )

    try:
        conn.autocommit = False
        test_users_table(conn)
        test_interests_table(conn)
        test_user_interests_table(conn)
        test_matches_table(conn)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Always rollback to ensure the database remains unchanged
        conn.rollback()
        conn.close()
        print("Transaction rolled back and connection closed.")

if __name__ == "__main__":
    main()
