import csv
import requests
import sys

def get_employee_data(employee_id):
    # URL to fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    # URL to fetch employee TO DO list
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    
    try:
        # Fetch employee data
        response_employee = requests.get(employee_url)
        response_employee.raise_for_status()
        employee_data = response_employee.json()
        
        # Fetch employee TO DO list
        response_todos = requests.get(todos_url)
        response_todos.raise_for_status()
        todos_data = response_todos.json()
        
        return employee_data,todos_data
    
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
        sys.exit(1)
      
def export_to_csv(employee_id, employee_data, todos_data):
    filename = f"{employee_id}.csv"
    
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Write the task data for the employee
        for todo in todos_data:
            csvwriter.writerow([employee_id, employee_data.get("name"), str(todo["completed"]), todo["title"]])
  
def read_csv_file(employee_id):
    filename = f"{employee_id}.csv"

    try:
        with open(filename, 'r') as f:
            for line in f:
                print(line, end='')
                
    except FileNotFoundError:
        print(f"File {filename} not found.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
        
    employee_id = int(sys.argv[1])
    employee_data, todos_data = get_employee_data(employee_id)
            
    # Export to CSV
    export_to_csv(employee_id, employee_data, todos_data)
    print(f"Data exported to {employee_id}.csv")
    
    read_csv_file(employee_id)

if __name__ == "__main__":
    main()
