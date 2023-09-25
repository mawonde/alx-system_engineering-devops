#!/usr/bin/python3
"""Script that, uses REST API, for a given employee ID,
returns information about  TODO list
"""

import requests
import sys
import json

# Define the base URL of the REST API
base_url = "https://jsonplaceholder.typicode.com"


def get_employee_todo_progress(employee_id):
    """Takes in employee ID and make requests to API"""
    response = requests.get(f"{base_url}/todos?userId={employee_id}")

    if response.status_code == 200:
        todos = response.json()
        completed_tasks = [task for task in todos if task["completed"]]

        # Make another request to get the employee's name
        user_response = requests.get(f"{base_url}/users/{employee_id}")
        user_data = user_response.json()
        employee_name = user_data.get("name", "Unknown")

        # Create a JSON object
        json_data = {
            "USER_ID": [
                {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": employee_name,
                }
                for task in completed_tasks
            ]
        }

        # Save the JSON data to a file
        json_filename = f"{employee_id}.json"
        with open(json_filename, "w") as json_file:
            json.dump(json_data, json_file, indent=4)

        print(f"Data exported to {json_filename} in JSON format.")
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
