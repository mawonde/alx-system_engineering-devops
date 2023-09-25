#!/usr/bin/python3

"""Script that, uses REST API, for a given employee ID, 
returns information about  TODO list
"""
import requests
import sys

# Define the base URL of the REST API
base_url = "https://jsonplaceholder.typicode.com"


def get_employee_todo_progress(employee_id):
    """Takes in employee ID and make requests to API"""
    response = requests.get(f"{base_url}/todos?userId={employee_id}")
    if response.status_code == 200:
        todos = response.json()

        completed_tasks = [task for task in todos if task["completed"]]

        total_tasks = len(todos)

        num_completed_tasks = len(completed_tasks)

        # Make another request to get the employee's name
        user_response = requests.get(f"{base_url}/users/{employee_id}")
        user_data = user_response.json()
        employee_name = user_data.get("name", "Unknown")

        # Print the progress information
        print(
            f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):"
        )
        for task in completed_tasks:
            print(f"\t{task['title']}")
    else:
        print(f"Failed to retrieve data for employee ID {employee_id}.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
