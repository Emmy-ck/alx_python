"""This program fetches employee data and exports it to both CSV and JSON format

"""

import json
import requests
import sys

if __name__ == '__main__':
    employee_id = sys.argv[1]

    # getting user
    employee_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    employee = requests.get(employee_url)
    employee_data = employee.json()

    # getting todos
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)
    todos = requests.get(todo_url)
    todos_data = todos.json()

    # exporting to a json
    json_file = "{}.json".format(employee_id)
    
    employee_info = {
        f"{employee_id}": [
            {
                "task": items['title'],
                "completed": items['completed'],
                "username": employee_data['username'],
            }

            for items in todos_data
        ]
    }

    # write data to json file
    with open(json_file, 'w') as json_files:
        json.dump(employee_info, json_files)
