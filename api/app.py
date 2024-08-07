from flask import Blueprint, make_response, jsonify, request, session
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

@bp.route('/find_matches', methods=['GET', 'POST'])
def find_matches():
    return None


# @bp.route('/login', methods=['GET', 'POST'])
# def login():
    # user = None
    # cursor = None
    # db_conn = None
    # if request.method == 'POST':
    #     try:
    #         username = request.form['username']
    #         password = request.form['password_hash']
    #         db_conn = db.get_db()
    #         cursor = db_conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    #         cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    #         user = cursor.fetchone()
    #         print(f"User: {user}")  # Debug print
    #         # user = dict(user)
    #         if user is None:
    #             print("User not found")
    #             return make_response(jsonify({'error': 'Invalid username'}), 401)
    #         if user['password_hash'] != password:
    #             print("Invalid password")
    #             return make_response(jsonify({'error': 'Invalid password'}), 401)
    #         # print(f"Logged in user: {user}")  # Debug print
    #     except Exception as e:
    #         print(f"Error logging in user: {e}")
    #         return make_response(jsonify({'error': 'Invalid username or password'}), 401)
    #     finally:
    #         if cursor:
    #             cursor.close()
    #         if db_conn:
    #             db_conn.close()
    #     if user:
    #         print("User found")
    #         login_response = dict(user)
    #         return make_response(jsonify(login_response))
    #     else:
    #         print("User not found")
    #         login_response = {'error': 'user not found'}
    #         return make_response(jsonify(login_response))
        
    return make_response(jsonify({'place': 'holder'}), 200)


    # login_response = {'place': 'holder'}
    # return make_response(jsonify(login_response))

# TODO write create_match, test create_match
@bp.route('/create_match', methods=['GET', 'POST'])
def create_match():
    create_match_response = {'place': 'holder'}
    return make_response(jsonify(create_match_response))

# TODO: finish implementation.
# As is, returns entire matches. Should return just the id, or return get_user() of matched users.
@bp.route('/matches/<int:user_id>', methods=['GET', 'POST'])
def matches(user_id):
    user = get_user(user_id)
    if user is None:
        return make_response(jsonify({"error": "User not found"}), 404)
    else:
        cursor = None
        db_conn = None
        try:
            db_conn = db.get_db()  # Ensure this function returns a psycopg2 connection
            cursor = db_conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cursor.execute("SELECT * FROM matches WHERE user1_id = %s OR user2_id = %s", (user_id,user_id))
            user_matches = cursor.fetchall()
            print(f"User matches: {user_matches}")  # Debug print
            return make_response(jsonify(user_matches))
        except Exception as e:
            print(f"Error fetching user matches: {e}")
        finally:
            if cursor:
                cursor.close()
            if db_conn:
                db_conn.close()
    return make_response(jsonify({"error": "User not found"}), 404)

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_response = {'place': 'holder'}
    return make_response(jsonify(signup_response))

@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_response = {'place': 'holder'}
    return make_response(jsonify(logout_response))

# Get users by interest
# TODO write pytest for route
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