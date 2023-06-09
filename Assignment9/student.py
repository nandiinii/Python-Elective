class Student:
    def __init__(self,name,roll_no):
        self.roll_no=roll_no
        self.name=name
    def setAge(self):
        age = int(input("Enter the age: "))
        self.age = age
    def setTestMarks(self):
        testMarks = float(input("Enter the marks of the test: "))
        self.testMarks = testMarks
    def display(self):
        print("Name: ",self.name)
        print("Roll No: ",self.roll_no)
        print("Age: ",self.age)
        print("Test Marks: ",self.testMarks)

stud = Student("Nandini",47)
stud.setAge()
stud.setTestMarks()
stud.display()
    