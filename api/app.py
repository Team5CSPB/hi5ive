from flask import Blueprint, make_response, jsonify
from flask_cors import CORS
from . import db, create_app
import psycopg2.extras

app = create_app()
CORS(app, origins=["http://localhost:3000"])
# Generates a blueprint for routing and registering routes with the app factory
bp = Blueprint('api', __name__)
CORS(bp, origins=["http://localhost:3000"])  # Apply CORS to the blueprint


@bp.route('/users')
def get_users():
    users = []
    cursor = None
    db_conn = None
    try:
        db_conn = db.get_db()  # Ensure this function returns a psycopg2 connection
        cursor = db_conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        print(f"Fetched users: {users}")  # Debug print
    except Exception as e:
        print(f"Error fetching users: {e}")
    finally:
        if cursor:
            cursor.close()
        if db_conn:
            db_conn.close()

    users_list = [dict(user) for user in users]
    print(f"Users list: {users_list}")  # Debug print
    return make_response(jsonify(users_list), 200)

# Get user by ID
@bp.route('/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = None
    cursor = None
    db_conn = None
    try:
        db_conn = db.get_db()  # Ensure this function returns a psycopg2 connection
        cursor = db_conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        print(f"Fetched user: {user}")  # Debug print
    except Exception as e:
        print(f"Error fetching user: {e}")
    finally:
        if cursor:
            cursor.close()
        if db_conn:
            db_conn.close()

    if user is None:
        return make_response(jsonify({"error": "User not found"}), 404)

    user_dict = dict(user)
    print(f"User dict: {user_dict}")  # Debug print
    return make_response(jsonify(user_dict), 200)

# Get users by interest
@app.route('/users/interest/<string:interest>', methods=['GET'])
def get_users_by_interest(interest):
    users = []
    cursor = None
    db_conn = None
    try:
        interest_id = db.fetch_interest_id(interest)
        if interest_id is None:
            return make_response(jsonify({"error": "Interest not found"}), 404)

        db_conn = db.get_db()  # Ensure this function returns a psycopg2 connection
        if db_conn.closed:
            print("Database connection is already closed after get_db()")
            return make_response(jsonify({"error": "Database connection is closed"}), 500)

        cursor = db_conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        cursor.execute("""
            SELECT u.* 
            FROM users u
            JOIN user_interests ui ON u.id = ui.user_id
            WHERE ui.interest_id = %s
        """, (interest_id,))
        users = cursor.fetchall()
        print(f"Fetched users: {users}")  # Debug print
    except Exception as e:
        print(f"Error fetching users: {e}")
    finally:
        if cursor:
            cursor.close()
        if db_conn and not db_conn.closed:
            db_conn.close()

    users_list = [dict(user) for user in users]
    print(f"Users list: {users_list}")
    return make_response(jsonify(users_list), 200)

app.register_blueprint(bp)

if __name__ == '__main__':
   app.run(port=5000)