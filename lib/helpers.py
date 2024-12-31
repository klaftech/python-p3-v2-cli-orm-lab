from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    print(employees)
    for employee in employees:
        print(employee)

def find_employee_by_name():
    name = input("Enter employee name: ")
    if employee := Employee.find_by_name(name):
        print(employee)
    else:
        print(f"Employee {name} not found")

def find_employee_by_id():
    id_ = input("Enter employee's id: ")
    if employee := Employee.find_by_id(id_):
        print(employee)
    else:
        print(f"Employee {id_} not found")

def create_employee():
    name = input("Enter employee's name: ")
    job_title = input("Enter employee's job title: ")
    dept_id_ = input("Enter employee's department id: ")
    dept_id_int_ = int(dept_id_)
    try:
        employee = Employee.create(name,job_title,dept_id_int_)
        print(f'Employee {employee} successfully added')
    except Exception as e:
        print("Error creating employee: ",e)

def update_employee():
    employee_id_ = input("Enter employee's id: ")
    if employee := Employee.find_by_id(employee_id_):
        try:
            name = input("Enter employee's new name: ")
            employee.name = name

            job_title = input("Enter employee's new job title: ")
            employee.job_title = job_title
            
            dept_id = input("Enter employee's new department id: ")
            employee.department_id = int(dept_id)
            
            employee.update()
            print("Employee updated successfully")
        except Exception as e:
            print("Employee could not be updated. ", e)
    else:
        print(f'Employee {employee_id_} not found.')

def delete_employee():
    employee_id_ = input("Enter employee's id: ")
    if employee := Employee.find_by_id(employee_id_):
        try:
            employee.delete()
            print(f'Employee {employee_id_} deleted')
        except Exception as e:
            print("Employee could not be deleted. ", e)
    else:
        print(f'Employee {employee_id_} not found.')


def list_department_employees():
    dept_id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(dept_id_):
        for i in [employee for employee in Employee.get_all() if employee.department_id == department.id]:
            print(i)
    else:
        print(f'Department {dept_id_} not found.')