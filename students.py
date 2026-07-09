import sqlite3

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    marks INTEGER NOT NULL
)
""")              

def add_student(name,marks):
    if marks<0 or marks>100:
      print("marks should be between 0 and 100.")
      return
    cursor.execute("INSERT INTO students (name,marks) VALUES (?, ?)", (name, marks))
    conn.commit()
    print("Student added successfully.")
def show_students():
    cursor.execute("SELECT * FROM students")
    row=cursor.fetchall()
    print("\n ========== Student List ==========")
    for student in row:
      print(f"ID: {student[0]}, Name: {student[1]}, Marks: {student[2]}")
def update_student(student_id, new_marks):
    if new_marks<0 or new_marks>100:
      print("marks should be between 0 and 100.")
      return
    cursor.execute("UPDATE students SET marks= ? WHERE id= ?",(new_marks, student_id))
    if cursor.rowcount ==0:
        print("Student not found.")
    else:
     conn.commit()
     print(f"Student ID updated successfully.")
def search_student(student_id):
    cursor.execute("SELECT * FROM students WHERE id = ?", (student_id,))
    student = cursor.fetchone()

    if student:
        print("\n========== Student Found ==========")
        print(f"ID    : {student[0]}")
        print(f"Name  : {student[1]}")
        print(f"Marks : {student[2]}")
    else:
        print("Student not found.")
def delete_student(student_id):
    cursor.execute("DELETE FROM students WHERE id = ?",(student_id,))
    if cursor.rowcount==0:
        print("Student not found.")
    else:
     conn.commit()
     print(f"Student ID deleted successfully.")


def menu():
    while True:
        print("\n ========== Student Management System Via SQLite DB ==========")
        print("1. Add Student")
        print("2. Show All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")
        
        choice=input("Enter your choice(1-6):")
        if choice=="1":
            name= input("Enter student name:")
            try:
                marks= int(input("Enter student marks:"))
                add_student(name,marks)
            except ValueError:
               print("Please enter valid numeric marks.")
        elif choice=="2":
            show_students()
        elif choice=="3":
            try:
               student_id=int(input("Enter student ID to update:"))
               new_marks=int(input("Enter new marks:"))
               update_student(student_id, new_marks)
            except ValueError:
               print("Please enter valid numbers.")
        elif choice=="4":
            try:
                student_id=int(input("Enter student ID to delete:"))
                delete_student(student_id)
            except ValueError:
               print("Please enter a valid ID.")
        elif choice=="5":
            try:
               student_id=int(input("Enter student ID to search:"))
               search_student(student_id)
            except ValueError:
               print("Please enter a valid ID.")
        elif choice=="6":
            print("Exiting the system.Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ =="__main__":
 menu()
conn.close()