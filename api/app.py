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


#* Not fully implemented
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

# Creates a match
@bp.route('/create_match', methods=['GET', 'POST'])
def create_match():
    cursor = None
    db_conn = None
    create_match_response = None
    if request.method == 'POST':
        try:
            source_user = request.form['user1_id']
            target_user = request.form['user2_id']
            if get_user(source_user).status_code != 200 or get_user(target_user).status_code != 200:
                print("User not found")  # Debug print
                return make_response(jsonify({'error': 'User not found'}), 404)
            if source_user == target_user:
                print("Can't match user to self")  # Debug print
                return make_response(jsonify({'error': 'Can\'t match user to self'}), 409)
            db_conn = db.get_db()
            cursor = db_conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            # Check if match already exists
            cursor.execute("SELECT * FROM matches WHERE user1_id = %s AND user2_id = %s", (source_user, target_user))
            match = cursor.fetchone()
            if match is not None:
                print(f"Match already exists between {source_user} and {target_user}")  # Debug print
                return make_response(jsonify({'error': 'Match already exists'}), 409) # I think 409 is right?
            # Create match
            cursor.execute("INSERT INTO matches (user1_id, user2_id) VALUES (%s, %s)", (source_user, target_user))
            db_conn.commit()
            # Check if match was created # TODO implement error handling
            cursor.execute("SELECT * FROM matches WHERE user1_id = %s AND user2_id = %s", (source_user, target_user))
            create_match_response = dict(cursor.fetchone())
            print(f"Created match between {source_user} and {target_user}")  # Debug print
        except Exception as e:
            print(f"Error creating match: {e}")
            return make_response(jsonify({'error': 'Error creating match'}), 500)
        finally:
            if cursor:
                cursor.close()
            if db_conn:
                db_conn.close()
    print(f"New match created: {create_match_response}")
    return make_response(jsonify(create_match_response))

# Returns the profiles of users matched to the source user
@bp.route('/matches/<int:user_id>', methods=['GET', 'POST'])
def matches(user_id):
    user = get_user(user_id) # make sure user exists
    user_matches = None
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
            #return make_response(jsonify(user_matches))
        except Exception as e:
            print(f"Error fetching user matches: {e}")
        finally:
            if cursor:
                cursor.close()
            if db_conn:
                db_conn.close()
    matched_users = []
    # TODO: Implement error handling for retrieving this data
    for match in user_matches:
        if match['user1_id'] == user_id:
            m = get_user(match['user2_id']).get_json() # get_user() returns response object
        else:
            m = get_user(match['user1_id']).get_json()
        if m is not None:
            print(f"Matched user: {m}")
            matched_users.append(m)
    return make_response(jsonify(matched_users))

@bp.route('/signup', methods=['GET', 'POST'])
def signup():
    signup_response = {'place': 'holder'}
    return make_response(jsonify(signup_response))

@bp.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_response = {'place': 'holder'}
    return make_response(jsonify(logout_response))

# Get users by interest
@bp.route('/users/interest/<string:interest>', methods=['GET'])
def get_users_by_interest(interest):
    print(f"Getting users by interest: {interest}")
    users = []
    cursor = None
    db_conn = None
    try:
        interest_id = db.fetch_interest_id(interest)
        print(f"Interest ID: {interest_id}")
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