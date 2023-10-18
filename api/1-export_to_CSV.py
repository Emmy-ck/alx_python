import requests
import sys
import csv

def get_employee_data(employee_id):
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    try:
        response_employee = requests.get(employee_url)
        response_employee.raise_for_status()
        employee_data = response_employee.json()

        response_todos = requests.get(todos_url)
        response_todos.raise_for_status()
        todos_data = response_todos.json()

        return employee_data, todos_data

    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
        sys.exit(1)

def export_to_csv(employee_id, employee_data, todos_data):
    filename = f"{employee_id}.csv"

    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for todo in todos_data:
            csvwriter.writerow([str(employee_id), f'"{employee_data.get("name")}"', str(todo["completed"]), f'"{todo["title"]}"'])

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    employee_data, todos_data = get_employee_data(employee_id)

    export_to_csv(employee_id, employee_data, todos_data)
    print(f"Data exported to {employee_id}.csv")

if __name__ == "__main__":
    main()
