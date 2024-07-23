import mysql.connector as connector

class DB:
    def __init__(self): 
        self.con = connector.connect(  
                host='localhost',
                user='root',
                password='', 
                database='college',
                port=3306
            )
        query = 'CREATE TABLE IF NOT EXISTS students(id INT PRIMARY KEY, student_name VARCHAR(200), father_name VARCHAR(200), address VARCHAR(200), fees INT NOT NULL, department VARCHAR(200), grade VARCHAR(50))'
        cur = self.con.cursor()
        cur.execute(query)
        print("table created")

    def insert_students(self, id, student_name, father_name, address, fees, department, grade):
        query = "INSERT INTO students(id, student_name, father_name, address, fees, department, grade) VALUES({},'{}','{}','{}',{},'{}','{}')".format(id, student_name, father_name, address, fees, department, grade)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()  # for parmanent changes
        print("student data saved successfully!")

    def fetch_all(self):
        query = "SELECT * FROM students"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(row)

    def fetch_one(self, id):
        query = "SELECT * FROM students WHERE id = {}".format(id)
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print(row)

    def delete_student(self, id):
        query = "DELETE FROM students WHERE id = {}".format(id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Student whose id is {} is deleted successfully! ".format(id))

    def update_Student(self, id,newAdress, newFees):
        query = "UPDATE students SET address = '{}', fees = '{}' WHERE id = {}".format(newAdress, newFees, id)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Student data has been Updated Successfully !")
