#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    """
    Fetches and displays the TODO list progress for a given employee ID from the JSONPlaceholder API.

    Args:
        employee_id (int): The ID of the employee whose TODO list progress is to be fetched.

    Returns:
        None: Prints the employee's TODO list progress to the standard output.
    """
    base_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    response = requests.get(base_url)

    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return

    todos = response.json()
    completed_tasks = [todo['title'] for todo in todos if todo['completed']]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todos)
    
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user_data = user_response.json()
    employee_name = user_data.get('name', 'Unknown Employee')

    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
    else:
        try:
            employee_id = int(sys.argv[1])
            get_employee_todo_progress(employee_id)
        except ValueError:
            print("Invalid employee ID. Please enter a valid integer.")

