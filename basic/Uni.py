class Person:
    def __init__(self,name,address,age):
        self.__name=name
        self.__address=address
        self.__age=age
    def occupation(self):
        print("Nada, Occupation is not defined")
    def information(self):
        print(f"Name: {self.__name}, Address: {self.__address}, Age: {self.__age}")    

class Student(Person):     
    def __init__(self,name,address,age,course):
        super().__init__(name,address,age)
        self.__course=course
    def occupation(self):
        print("Student")
    def courseInfo(self):
        print(f"Course: {self.__course}")    
class Teacher(Person):
    def __init__(self,name,address,age,subject):
        super().__init__(name,address,age)
        self.__subject=subject
    def occupation(self):
        print("Teacher")
    def subjectInfo(self):
        print(f"Subject: {self.__subject}")    


std1 = Student("Alice", "123 Main St", 20, "Computer Science")
std1.occupation()  # Output: Student      
std1.information()  # Output: Name: Alice, Address: 123 Main St, Age: 20
std1.courseInfo()  # Output: Course: Computer Science

tch1 = Teacher("Bob", "456 Elm St", 40, "Mathematics")
tch1.occupation()  # Output: Teacher
tch1.information()  # Output: Name: Bob, Address: 456 Elm St, Age: 40
tch1.subjectInfo()  # Output: Subject: Mathematics
