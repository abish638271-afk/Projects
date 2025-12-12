import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Dsec@123",
    database="testdb"
)

cursor = conn.cursor()
print("successfully connected")

# -----------------------
# 1. CREATE (INSERT)
# -----------------------
def add_student(id, name, age):
    query = "INSERT INTO students (id, name, age) VALUES (%s, %s, %s)"
    values = (id, name, age)
    cursor.execute(query, values)
    conn.commit()
    print("Student Added!")

# -----------------------
# 2. READ (SELECT)
# -----------------------
def get_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

# -----------------------
# 3. UPDATE
# -----------------------
def update_student(id, new_age):
    query = "UPDATE students SET age=%s WHERE id=%s"
    values = (new_age, id)
    cursor.execute(query, values)
    conn.commit()
    print("Student Updated!")

# -----------------------
# 4. DELETE
# -----------------------
def delete_student(id):
    query = "DELETE FROM students WHERE id=%s"
    value = (id,)
    cursor.execute(query, value)
    conn.commit()
    print("Student Deleted!")


# -----------------------
# TEST CRUD OPERATIONS
# -----------------------
# Uncomment these to test ↓

# add_student(1, "Abishek", 21)
# add_student(2, "Kumar", 22)

# print("All Students:")
# get_students()

# update_student(1, 25)

# delete_student(2)
