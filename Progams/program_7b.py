class Employee:
    def __init__(self):
        self.name=" "
        self.empID=" "
        self.dept=" "
        self.salary=0

    def getEmpDetails(self):
        self.name=input("Enter the employee name: ")
        self.empID=input("Enter employee ID : ")
        self.dept=input("Enter employee department: ")
        self.salary=int(input("Enter employee salary : "))

    def showEmpDetails(self):
        print("Employee details: ")
        print("Name: ",self.name)
        print("ID : ",self.empID)
        print("Dept : ",self.dept)
        print("Salary : ",self.salary)

    def updSalary(self):
        self.salary=int(input("Enter new salary: "))
        print("Updated salary: ",self.salary)

e1=Employee()
e1.getEmpDetails()
e1.showEmpDetails()
e1.updSalary()
