"""This program fetches employee data and exports it to both CSV and JSON format
"""
import json
import requests
import sys


def data_to_json(user_id):
    """
    Fetches the employee's details and TODO list using the
    provided API endpoints,
    exports the informationto a JSON file.

    >>> data_to_json(-1)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0
    
    Parameters:
    - employee_id (int): The ID of the employee.

    Returns:
    None
    """
    # format url with input from user
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'\
    .format(user_id)
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'\
    .format(user_id)

    # request data frm todo and user api
    user_data = requests.get(user_url).json()
    todo_data = requests.get(todo_url).json()

    # creat a json data from the todo and user object
    json_data = {
        user_id : [ {
                "task":task['title'], "completed":task['completed'],
                "username":user_data['username'],
            }
            for task in todo_data
        ]
    }

    # Write to JSON file name filename
    filename = f"{user_id}.json"

    # open the and overwrite it content with w
    with open(filename, 'w') as file:
        json.dump(json_data, file, indent=2)

# Entry point
if __name__=='__main__':
    data_to_json(sys.argv[1])
