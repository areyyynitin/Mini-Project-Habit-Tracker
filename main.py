from user_model import register_user, login_user
from habit_model import add_habit, get_user_habits, delete_habit, mark_habit_as_done, view_habit_progress

def main():
    while True:
        print("1. Register New User")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")
            register_user(username, password)
            print("\nUser registered successfully!\n")
        elif choice == "2":
            username = input("Enter username: ")
            
            
            password = input("Enter password: ")
            user_id = login_user(username, password)
            if user_id:
                print("\nLogin successful!\n")
                while True:
                    print("1. Add Habit")
                    print("2. View Habits")
                    print("3. Delete Habit")
                    print("4. Mark Habit as Done")
                    print("5. View Habit Progress")
                    print("6. Logout")
                    habit_choice = input("\nEnter your choice: ")
                    if habit_choice == "1":
                        habit_name = input("Enter habit name: ")
                        add_habit(user_id, habit_name)
                        print("\nHabit added successfully!\n")
                    elif habit_choice == "2":
                        habits = get_user_habits(user_id)
                        if habits:
                            for habit in habits:
                                print(f"\nHabit ID: {habit[0]}, Habit Name: {habit[1]}")
                        else:
                            print("\nNo habits found!\n")
                    elif habit_choice == "3":
                        habits = get_user_habits(user_id)
                        if habits:
                            for habit in habits:
                                print(f"\n\nHabit ID: {habit[0]}, Habit Name: {habit[1]}")
                            habit_id_to_delete = int(input("Enter the habit ID to delete: "))
                            delete_habit(habit_id_to_delete)
                            print("\nHabit deleted successfully!\n")
                        else:
                            print("\nNo habits found!\n")
                    elif habit_choice == "4":
                        habits = get_user_habits(user_id)
                        if habits:
                            for habit in habits:
                                print(f"\nHabit ID: {habit[0]}, Habit Name: {habit[1]}")
                            habit_id_to_mark = int(input("Enter the habit ID to mark as done: "))
                            mark_habit_as_done(habit_id_to_mark)
                            print("\nHabit marked as done!")
                        else:
                            print("No habits found!")
                    elif habit_choice == "5":
                        habits = get_user_habits(user_id)
                        if habits:
                            for habit in habits:
                                print(f"Habit ID: {habit[0]}, Habit Name: {habit[1]}")
                            habit_id_to_view = int(input("Enter the habit ID to view progress: "))
                            progress = view_habit_progress(habit_id_to_view)
                            if progress:
                                for entry in progress:
                                    print(f"Date: {entry[0]}, Done: {entry[1]}")
                            else:
                                print("No progress found!")
                        else:
                            print("No habits found!")
                    elif habit_choice == "6":
                        break
                    else:
                        print("Invalid choice!")
            else:
                print("Invalid username or password!")
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()