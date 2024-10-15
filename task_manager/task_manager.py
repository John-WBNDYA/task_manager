# =====importing libraries===========
"""This is the section where you will import libraries"""
from datetime import datetime
import datetime as dt


# ====Functions==========
def register_user():
    """
    Registers a new user by prompting for a username and password.
    Writes the username and password to user.txt.
    """
    while True:
        new_username = input("Enter a new username: ").lower()
        if new_username in username_list:
            print("Username already exists. Please choose a different one.")
        else:
            new_password = input("Enter a new password: ")
            confirm_password = input("Confirm password: ")
            if new_password == confirm_password:
                with open("user.txt", "a") as user_file:
                    user_file.write(f"\n{new_username}, {new_password}")
                print("User registered successfully!")
                break
            else:
                print("Passwords don't match. Please try again.")


def add_task():
    """ Adds a new task to the task list by asking 
        the user to input the task details."""
    task_username = input("Username: ")
    task_title = input("Task Title: ")
    task_description = input("Task Description: ")
    task_date = input("Task Date (DD MM YYYY): ")
    due_date = input("Task Due Date (DD MM YYYY): ")
    task_done = "No"

    with open("tasks.txt", "a") as task_file:
        task_file.write(
            f"""\n{task_username}, {task_title}, {task_description},\
                {task_date}, {due_date}, {task_done}"""
        )
    print("Task added successfully!")


def view_all():
    """
    Displays all tasks in the tasks list
    in a user-friendly, easy to read format"""
    with open("tasks.txt", "r") as task_file:
        for tasks in task_file:
            temp = tasks.strip().split(", ")
            print(f"Username:         {temp[0]}")
            print(f"Task Title:       {temp[1]}")
            print(f"Task Description: {temp[2]}")
            print(f"Task Date:        {temp[3]}")
            print(f"Task Due Data:    {temp[4]}")
            print(f"Task Complete:    {temp[5]}")
            print("-" * 20)


def view_mine():
    """
    Displays tasks assigned to the current user and
    allows for task selection, completion, or editing.
    """
    with open("tasks.txt", "r") as tasks_file:
        tasks = tasks_file.readlines()

    user_tasks = []
    task_index = 1

    for task in tasks:
        task_details = task.strip().split(", ")
        if task_details[0] == username:
            user_tasks.append(task)
            print(f"{task_index}. Username:         {task_details[0]}")
            print(f"   Task title:       {task_details[1]}")
            print(f"   Task Description: {task_details[2]}")
            print(f"   Assigned date:    {task_details[3]}")
            print(f"   Due date:         {task_details[4]}")
            print(f"   Task complete:    {task_details[5]}")
            print()
            task_index += 1

    if user_tasks:
        while True:
            task_choice = input(
                "Enter the number of the task you want to select (or -1 to return to the menu): "
            )
            if task_choice == "-1":
                break
            elif task_choice.isdigit() and 1 <= int(task_choice) <= len(user_tasks):
                selected_task_index = int(task_choice) - 1
                selected_task = user_tasks[selected_task_index]

                while True:
                    action = input(
                        f"Do you want to mark task {task_choice} as complete or edit it? (c/e/b): "
                    ).lower()
                    if action == "c":
                        # Mark task as complete
                        with open("tasks.txt", "r") as tasks_file:
                            tasks = tasks_file.readlines()
                        with open("tasks.txt", "w") as tasks_file:
                            for i, task in enumerate(tasks):
                                if task.strip() == selected_task.strip():
                                    tasks[i] = task.replace("No", "Yes")
                                    print(f"Task {task_choice} marked as complete.")
                                    break
                            else:
                                print("Task not found.")
                            tasks_file.writelines(tasks)
                        break
                    elif action == "e":
                        # Edit task
                        while True:
                            edit_choice = input(
                                "What do you want to edit? (u - username, d - due date, b - back): "
                            ).lower()
                            if edit_choice == "u":
                                new_username = input("Enter the new username: ")
                                with open("tasks.txt", "r") as tasks_file:
                                    tasks = tasks_file.readlines()
                                with open("tasks.txt", "w") as tasks_file:
                                    for i, task in enumerate(tasks):
                                        if task.strip() == selected_task.strip():
                                            tasks[i] = tasks[i].replace(
                                                username, new_username
                                            )
                                            print(
                                                f"Username updated for task {task_choice}."
                                            )
                                            break
                                    else:
                                        print("Task not found.")
                                    tasks_file.writelines(tasks)
                                break
                            elif edit_choice == "d":
                                new_due_date = input(
                                    "Enter the new due date (DD-MM-YYYY): "
                                )
                                print(new_due_date)
                                with open("tasks.txt", "r") as tasks_file:
                                    tasks = tasks_file.readlines()
                                with open("tasks.txt", "w") as tasks_file:
                                    for i, task in enumerate(tasks):
                                        if task.strip() == selected_task.strip():
                                            tasks[i] = tasks[i].replace(
                                                selected_task.split(", ")[4],
                                                new_due_date,
                                            )
                                            print(
                                                f"Due date updated for task {task_choice}."
                                            )
                                            break
                                    else:
                                        print("Task not found.")
                                    tasks_file.writelines(tasks)
                                break
                            elif edit_choice == "b":
                                break
                            else:
                                print("Invalid choice. Please enter 'u', 'd', or 'b'.")
                        break
                    elif action == "b":

                        break
                    else:
                        print("Invalid choice. Please enter 'c', 'e', or 'b'.")
                break
            else:
                print("Invalid choice. Please enter a valid number or -1.")
    else:
        print(f"No tasks found for user {username}.")


# ====Login Section====
login = False

# Empty lists that will store the usernames and passwords
username_list = []
password_list = []

# all usernames will not be case sensitive
# Makes login easier and for input validation
username = input("Username: ").lower()
password = input("Password: ")

with open("user.txt", "r") as user_file:
    for lines in user_file:
        temp = lines.strip()
        temp = temp.split(", ")

        # Extract all usernames in textfile into
        usernames = temp[0]

        username_list.append(usernames)


with open("user.txt", "r") as user_file:
    for lines in user_file:
        temp = lines.strip()
        temp = temp.split(", ")

        # second items in the list assigned to passwords
        passwords = temp[1]

        password_list.append(passwords)

while not login:
    if username in username_list:
        # Index of password and username must be the same
        index = username_list.index(username)
        if password_list[index] == password:
            print(f"Welcome {username}!!")
            login = True
            print(" ")

        else:
            print("Incorrect password")
            password = input("Password: ")

    else:
        print(f"User {username} not recognised")
        username = input("Username: ").lower
        password = input("Passord: ")

while True:
    # Present the menu to the user and
    # make sure that the user input is converted to lower case.
    if username != "admin":
        menu = input(
            """Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks                                         
e - exit
: """
        ).lower()

    else:
        menu = input(
            """Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
gr - generate reports
ds - display statistics                                          
e - exit
: """
        ).lower()

    if menu == "r":
        register_user()

    elif menu == "a":
        add_task()

    elif menu == "va":
        view_all()

    elif menu == "vm":
        view_mine()

    elif menu == "gr":
        print(" ")

        with open("tasks.txt", "r") as tasks_file:
            tasks = tasks_file.readlines()

        # Calculate overall task statistics
        total_tasks = len(tasks)
        completed_tasks = sum(1 for task in tasks if "Yes" in task.split(", ")[5])
        incomplete_tasks = total_tasks - completed_tasks
        overdue_incomplete_tasks = sum(
            1
            for task in tasks
            if "No" in task.split(", ")[5]
            and datetime.strptime(task.split(", ")[4], "%d %B %Y").date()
            < dt.date.today()
        )
        incomplete_task_percentage = (
            (incomplete_tasks / total_tasks) * 100 if total_tasks > 0 else 0
        )
        overdue_task_percentage = (
            (overdue_incomplete_tasks / total_tasks) * 100 if total_tasks > 0 else 0
        )

        # Generate task overview report
        with open("task_overview.txt", "w") as task_overview_file:
            task_overview_file.write("Task Overview\n\n")
            task_overview_file.write(f"Total Tasks: {total_tasks}\n")
            task_overview_file.write(f"Completed Tasks: {completed_tasks}\n")
            task_overview_file.write(f"Incomplete Tasks: {incomplete_tasks}\n")
            task_overview_file.write(
                f"Overdue Incomplete Tasks: {overdue_incomplete_tasks}\n"
            )
            task_overview_file.write(
                f"Percentage of Incomplete Tasks: {incomplete_task_percentage:.2f}%\n"
            )
            task_overview_file.write(
                f"Percentage of Overdue Tasks: {overdue_task_percentage:.2f}%\n"
            )

        print("Reports generated successfully!")
        print(" ")
        with open("task_overview.txt", "r") as file:
            for lines in file:
                print(lines)
            print(" ")

        # Generate user overview report
        with open("user_overview.txt", "w") as user_overview_file:
            user_overview_file.write("User Overview\n\n")

            # Read user data from user.txt
            with open("user.txt", "r") as user_file:
                user_data = user_file.readlines()
            total_users = len(user_data)
            user_overview_file.write(f"Total Users: {total_users}\n")

            # Read task data from tasks.txt
            with open("tasks.txt", "r") as tasks_file:
                tasks = tasks_file.readlines()
            total_tasks = len(tasks)
            user_overview_file.write(f"Total Tasks: {total_tasks}\n\n")

            # Calculate user-specific statistics
            user_stats = {}
            for user in username_list:
                user_tasks = [
                    task for task in tasks if task.strip().split(", ")[0] == user
                ]
                user_stats[user] = {
                    "total_tasks": len(user_tasks),
                    "completed_tasks": sum(
                        1 for task in user_tasks if "Yes" in task.strip().split(", ")[5]
                    ),
                    "incomplete_tasks": len(user_tasks)
                    - sum(
                        1 for task in user_tasks if "Yes" in task.strip().split(", ")[5]
                    ),
                    "overdue_incomplete_tasks": sum(
                        1
                        for task in user_tasks
                        if "No" in task.strip().split(", ")[5]
                        and datetime.strptime(
                            task.strip().split(", ")[4], "%d %B %Y"
                        ).date()
                        < dt.date.today()
                    ),
                }
                user_stats[user]["total_tasks_percentage"] = (
                    (user_stats[user]["total_tasks"] / total_tasks) * 100
                    if total_tasks > 0
                    else 0
                )
                user_stats[user]["completed_tasks_percentage"] = (
                    (
                        user_stats[user]["completed_tasks"]
                        / user_stats[user]["total_tasks"]
                    )
                    * 100
                    if user_stats[user]["total_tasks"] > 0
                    else 0
                )
                user_stats[user]["incomplete_tasks_percentage"] = (
                    (
                        user_stats[user]["incomplete_tasks"]
                        / user_stats[user]["total_tasks"]
                    )
                    * 100
                    if user_stats[user]["total_tasks"] > 0
                    else 0
                )
                user_stats[user]["overdue_incomplete_tasks_percentage"] = (
                    (
                        user_stats[user]["overdue_incomplete_tasks"]
                        / user_stats[user]["total_tasks"]
                    )
                    * 100
                    if user_stats[user]["total_tasks"] > 0
                    else 0
                )

            # Generate user-specific reports
            for user, stats in user_stats.items():
                user_overview_file.write(f"User: {user}\n")
                user_overview_file.write(
                    f"   Total Tasks Assigned: {stats['total_tasks']}\n"
                )
                user_overview_file.write(
                    f"   Total Tasks Assigned Percentage: {stats['total_tasks_percentage']:.2f}%\n"
                )
                user_overview_file.write(
                    f"   Completed Tasks Percentage: {stats['completed_tasks_percentage']:.2f}%\n"
                )
                user_overview_file.write(
                    f"   Incomplete Tasks Percentage: {stats['incomplete_tasks_percentage']:.2f}%\n"
                )
                user_overview_file.write(
                    f"""   Overdue Incomplete Tasks Percentage:\
                    {stats['overdue_incomplete_tasks_percentage']:.2f}%\n\n"""
                )

        with open("user_overview.txt", "r") as file:
            for lines in file:
                print(lines)

    elif menu == "ds":
        print("Business Statistics:\n")
        task_stats = 0
        users_stats = 0

        with open("tasks.txt", "r") as file:
            for line in file:
                task_stats += 1

        with open("user.txt", "r") as file:
            for line in file:
                users_stats += 1

        print(f"Total Tasks: {task_stats}")
        print(f"Total users: {users_stats}")

    elif menu == "e":
        print("Goodbye!!!")
        exit()

    else:
        print("You have entered an invalid input. Please try again")
