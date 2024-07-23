from Db import DB

def main():

    obj = DB()

    while True:
        print("--------------Welcome--------------")
        print()
        print("Press 1 to Insert new Students")
        print("Press 2 to Display all Students")
        print("Press 3 to Delete the Student")
        print("Press 4 to Update the Student")
        print("Press 5 to Exit the program" )
        print()
        try:
            choice = int(input())
            if choice == 1:
                #insert student 
                id = int(input("Enter Student ID (Roll number)"))
                name = input("Enter Student's Name")
                father_name = input("Enter Stuednt's Father Name ")
                address = input("Enter Student's Address")
                Fees = input("Enter Student's Fees")
                dep = input("Enter Student's Department")
                grade = input("Enter Student's grade")
                obj.insert_students(id, name, father_name, address, Fees, dep, grade)

            elif choice == 2:
                #display students
                obj.fetch_all()
                
            elif choice == 3:
                #Delete student
                id = int(input("Enter Student Id which you want to delete "))
                obj.delete_student(id)

            elif choice == 4:
                #update student
                u_id = int(input("Enter Id of Student whose data you want to update"))
                newAdress = input("Enter new Adress")
                newFees = input("Enter new Fees")
                obj.update_Student(newAdress, newFees, u_id)

            elif choice == 5:
                break
            else:
                print("Invalid input Try Again! ")
        except Exception as e:
            print(e)
            print("Try Again! ")

if __name__ == "__main__":
    main()