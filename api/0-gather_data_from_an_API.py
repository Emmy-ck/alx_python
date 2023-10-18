import csv
import requests
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1]

    # Fetch employee data
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response_employee = requests.get(employee_url)
    
    if response_employee.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return
    
    employee_data = response_employee.json()

    # Fetch employee TO DO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response_todos = requests.get(todos_url)
    
    if response_todos.status_code != 200:
        print(f"Failed to fetch todos for employee {employee_data['name']}.")
        return

    todos_data = response_todos.json()

    # CSV file
    csv_file = f"{employee_id}.csv"
    with open(csv_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            csv_writer.writerow([employee_id, employee_data['name'], task['completed'], task['title']])

    print(f"Data exported to {csv_file}.")


if __name__ == "__main__":
    main()
