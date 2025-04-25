from db import connect_db
import datetime

def add_habit(user_id, habit_name):
    cnx = connect_db()
    cursor = cnx.cursor()
    query = "INSERT INTO habits (user_id, habit_name) VALUES (%s, %s)"
    try:
        cursor.execute(query, (user_id, habit_name))
        cnx.commit()
    except Exception as e:
        print(f"Error adding habit: {e}")
        cnx.rollback()
    finally:
        cursor.close()
        cnx.close()

def get_user_habits(user_id):
    cnx = connect_db()
    cursor = cnx.cursor()
    query = "SELECT id, habit_name FROM habits WHERE user_id = %s"
    try:
        cursor.execute(query, (user_id,))
        habits = cursor.fetchall()
        return habits
    except Exception as e:
        print(f"Error getting habits: {e}")
        return []
    finally:
        cursor.close()
        cnx.close()

def delete_habit(habit_id):
    cnx = connect_db()
    cursor = cnx.cursor()
    query1 = "DELETE FROM habit_progress WHERE habit_id = %s"
    query2 = "DELETE FROM habits WHERE id = %s"
    try:
        cursor.execute(query1, (habit_id,))
        cursor.execute(query2, (habit_id,))
        cnx.commit()
    except Exception as e:
        print(f"Error deleting habit: {e}")
        cnx.rollback()
    finally:
        cursor.close()
        cnx.close()

def mark_habit_as_done(habit_id):
    cnx = connect_db()
    cursor = cnx.cursor()
    query = "INSERT INTO habit_progress (habit_id, progress_date, progress_time, is_done) VALUES (%s, CURDATE(), %s, %s)"
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    try:
        cursor.execute(query, (habit_id, current_time, True))
        cnx.commit()
    except Exception as e:
        print(f"Error marking habit as done: {e}")
        cnx.rollback()
    finally:
        cursor.close()
        cnx.close()

def view_habit_progress(habit_id):
    cnx = connect_db()
    cursor = cnx.cursor()
    query = "SELECT progress_date, is_done FROM habit_progress WHERE habit_id = %s"
    try:
        cursor.execute(query, (habit_id,))
        progress = cursor.fetchall()
        return progress
    except Exception as e:
        print(f"Error viewing habit progress: {e}")
        return []
    finally:
        cursor.close()
        cnx.close()

# Test the habit model
def test_habit_model():
    from user_model import register_user, login_user
    username = "test_user"
    password = "test_password"
    register_user(username, password)
    user_id = login_user(username, password)
    habit_name = "test_habit"
    add_habit(user_id, habit_name)
    habits = get_user_habits(user_id)
    if habits:
        print("Habit model working fine!")
        for habit in habits:
            print(f"Habit ID: {habit[0]}, Habit Name: {habit[1]}")
    else:
        print("Error in habit model")

if __name__ == "__main__":
    test_habit_model()