class Person:
    def __init__(self, name):
        self.name = name


class Employee:
    def __init__(self, emp_id):
        self.emp_id = emp_id


class Manager(Person, Employee):
    def __init__(self, name, emp_id, department):
        Person.__init__(self, name)
        Employee.__init__(self, emp_id)
        self.department = department

    def display(self):
        print("Name:", self.name)
        print("Employee ID:", self.emp_id)
        print("Department:", self.department)


# Example
m = Manager("Rudra", 101, "IT")
m.display()