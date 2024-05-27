import mysql.connector as sql

def data_teach():
    mydb = sql.connect(host="localhost",
            user="new_user",
            password="password",database = "timetable")
    cur = mydb.cursor()
    query = "select * from home_teacher_data"
    cur.execute(query)
    output = cur.fetchall()
    data_teach = []
    for i in output:
        data_teach.append(i[1])

    return data_teach

def data_subject():
    mydb = sql.connect(host="localhost",
            user="new_user",
            password="password",database = "timetable")
    cur = mydb.cursor()
    query = "select * from home_subjects_data"
    cur.execute(query)
    output = cur.fetchall()
    data_teach = []
    for i in output:
        data_teach.append(i[1])

    return data_teach

def data_course():
    mydb = sql.connect(host="localhost",
            user="new_user",
            password="password",database = "timetable")
    cur = mydb.cursor()
    query = "select * from home_course_data"
    cur.execute(query)
    output = cur.fetchall()
    data_teach = []
    for i in output:
        data_teach.append(i[1])

    return data_teach

def main():
    print(data_teach())
    print(data_course())
    print(data_subject())

if __name__ =='__main__':
    main()
