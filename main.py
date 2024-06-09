# Task:

# Implement a class (school class) management system, which will consist of 3 classes, User class (student, CR, teacher), Student class, Classroom class.

# Student class will have the details of the student, subjects that the student has registered in, and the marks.

# User class will consist of the credentials and the type of user (student, CR, instructor/teacher)

# Classroom class will have many students with each of them having different stuff, a student can only access his/her own things, CR can access all students' data, instructor can do everything ranging from updating marksheets to removing and adding students in the class.

class User:
    def __init__(self, name, email, password, type):
        self.__name = name
        self.__email = email 
        self.__password = password
        self.__type = type 

    def get_credentials(self, requester):
        if requester.__type == "Teacher" or requester.__type == "CR":
            return {"name": self.__name, "email": self.__email, "password": self.__password, "type": self.__type}
        else:
            return "You can't access user data!"

    def set_credentials(self, name, email, password, type):
        self.__name = name
        self.__email = email
        self.__password = password
        self.__type = type

class Classroom:
    def __init__(self, teacher, CR):
        self.__students = []
        self.__teacher = teacher
        self.__CR = CR

    def change_teacher(self, teacher):
        self.__teacher = teacher

    def change_CR(self, CR):
        self.__CR = CR

    def add_student(self, student, requester_email):
        if requester_email == self.__teacher.__email or requester_email == self.__CR.__email:
            self.__students.append(student)
        else:
            return "You can't add students to the class"

    def remove_student(self, student, requester_email):
        if requester_email == self.__teacher.__email or requester_email == self.__CR.__email:
            if student in self.__students:
                self.__students.remove(student)
            else:
                return "Student not found"  
        else:
            return "You can't remove students from the class"
        
    def get_students(self, requester):
        if requester == self.__teacher or requester == self.__CR:
            return self.__students
        else:
            return "You can't access students data!"
        
