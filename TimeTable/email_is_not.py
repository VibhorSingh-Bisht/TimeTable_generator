import mysql.connector as sql

def email_present(email):
    try:
        # Establish the database connection
        mydb = sql.connect(
            host="localhost",
            user="new_user",
            password="password",
            database="timetable"
        )
        cur = mydb.cursor()
        
        # Query to check if email exists
        query = "SELECT EXISTS (SELECT 1 FROM students_data WHERE email = %s)"
        cur.execute(query, (email,))
        result = cur.fetchone()
        
        # Close the cursor and connection
        cur.close()
        mydb.close()
        
        # Return True if email exists, otherwise False
        return result[0] == 1
    
    except sql.Error as err:
        print(f"Error: {err}")
        return False

if __name__ == '__main__':
    print(email_present('vibhor0711bp@gmail.com'))
