from DataAccessLayer.queries import get_employees

def fetch_employees_data():
    employees = get_employees()
    employee_list = [{"ID": emp[0], "JobTitle": emp[1]} for emp in employees]
    return employee_list


