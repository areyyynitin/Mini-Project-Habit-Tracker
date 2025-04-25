from db import connect_db

def register_user(username, password):
    cnx = connect_db()
    cursor = cnx.cursor()
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    try:
        cursor.execute(query, (username, password))
        cnx.commit()
    except Exception as e:
        print(f"Error registering user: {e}")
        cnx.rollback()
    finally:
        cursor.close()
        cnx.close()

def login_user(username, password):
    cnx = connect_db()
    cursor = cnx.cursor()
    query = "SELECT id FROM users WHERE username = %s AND password = %s"
    try:
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        cursor.fetchall()  # Fetch any remaining results
        if result is not None:
            user_id = result[0]
        else:
            user_id = None
        return user_id
    except Exception as e:
        print(f"Error logging in user: {e}")
        return None
    finally:
        cursor.close()
        cnx.close()

# Test the user model
def test_user_model():
    username = "test_user"
    password = "test_password"
    register_user(username, password)
    user_id = login_user(username, password)
    if user_id:
        print("User model working fine!")
    else:
        print("Error in user model")

if __name__ == "__main__":
    test_user_model()