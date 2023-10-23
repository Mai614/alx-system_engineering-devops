#!/usr/bin/python3

"""
a Python script that, using this REST API, for a given employee ID, returns 
information about his/her TODO list progress and exports the data in CSV format.
"""

import csv
from requests import get
from sys import argv

if __name__ == "__main__":
    response = get('https://jsonplaceholder.typicode.com/todos/')
    tasks_data = response.json()
    employee_id = int(argv[1])

    response2 = get(f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    user_data = response2.json()
    employee_name = user_data.get('username', 'Unknown Employee')

    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in tasks_data:
            if task.get('userId') == employee_id:
                task_completed_status = "COMPLETED" if task.get('completed') else "NOT COMPLETED"
                task_title = task.get('title')
                csv_writer.writerow([employee_id, employee_name, task_completed_status, task_title])

    print(f"CSV data has been exported to {csv_filename}")

