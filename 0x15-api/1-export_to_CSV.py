#!/usr/bin/python3
"""Script that, uses REST API, for a given employee ID,
returns information about  TODO list
"""

import requests
import sys
import csv

# Define the base URL of the REST API
base_url = "https://jsonplaceholder.typicode.com"


def get_employee_todo_progress(id):
    """Takes in employee ID and make requests to API"""
    response = requests.get(f"{base_url}/todos?userId={id}")

    if response.status_code == 200:
        todos = response.json()
        completed_tasks = [task for task in todos if task["completed"]]
        all_tks = len(todos)
        tasks_done = len(completed_tasks)

        # Make another request to get the employee's name
        user_response = requests.get(f"{base_url}/users/{id}")
        user_data = user_response.json()
        name = user_data.get("name", "Unknown")

        # Print the progress information
        print(f"Employee {name} is done with tasks ({tasks_done}/{all_tks}):")
        for task in completed_tasks:
            print(f"\t{task['title']}")

        # Export data to CSV
        csv_filename = f"{id}.csv"
        with open(csv_filename, mode="w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(
                ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            )
            for task in completed_tasks:
                csv_writer.writerow([id, name, "Completed", task["title"]])

        print(f"Data exported to {csv_filename} in CSV format.")
    else:
        print(f"Failed to retrieve data for employee ID {id}.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <id>")
        sys.exit(1)

    try:
        id = int(sys.argv[1])
        get_employee_todo_progress(id)
    except ValueError:
        print("Employee ID must be an integer.")
