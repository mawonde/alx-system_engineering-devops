#!/usr/bin/python3
"""Script that, uses REST API, for a given employee ID, returns information about  TODO list 
"""

import requests
import sys
import json

# Define the base URL of the REST API
base_url = "https://jsonplaceholder.typicode.com"


def get_all_employees_todo_progress():
  """Takes in employee ID and make requests to API """
  user_response = requests.get(f"{base_url}/users")
  users = user_response.json()

  all_data = {}

  for user in users:
    user_id = user["id"]
    username = user["username"]

    response = requests.get(f"{base_url}/todos?userId={user_id}")

    if response.status_code == 200:
      todos = response.json()
      completed_tasks = [task for task in todos if task["completed"]]

      # Create a list of tasks for this user
      user_tasks = [{
        "username": username,
        "task": task["title"],
        "completed": task["completed"]
      } for task in completed_tasks]

      all_data[user_id] = user_tasks
    else:
      print(f"Failed to retrieve data for employee ID {user_id}.")

  # Save the JSON data to a file
  json_filename = "todo_all_employees.json"
  with open(json_filename, "w") as json_file:
    json.dump(all_data, json_file, indent=4)

  print(f"Data exported to {json_filename} in JSON format.")


if __name__ == "__main__":
  if len(sys.argv) != 1:
    print("Usage: python script.py")
    sys.exit(1)

  get_all_employees_todo_progress()
