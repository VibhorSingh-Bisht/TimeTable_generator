import mysql.connector as sql


mydb = sql.connect(host="localhost",
            user="new_user",
            password="password",database = "timetable")

def data_clean_teach():
    cur1 = mydb.cursor()
    query1 = "select * from home_Teacher_data"
    cur1.execute(query1)
    output1 = cur1.fetchall()
    cleaned_data_t = []
    cleaned_data_teach = []
    for i in output1:
        b = i[1].split(',')
        cleaned_data_t.append(b)
    for j in cleaned_data_t[0]:
        a = j.lstrip()
        b = a.rstrip()
        cleaned_data_teach.append(b)
        
    return cleaned_data_teach


def data_clean_course():
    cur2 = mydb.cursor()
    query2 = "select * from home_course_data"
    cur2.execute(query2)
    output2 = cur2.fetchall()
    cleaned_data_c = []
    cleaned_data_course = []
    for i in output2:
        c = i[1].split(',')
        cleaned_data_c.append(c)
    for j in cleaned_data_c[0]:
        a = j.lstrip()
        b = a.rstrip()
        cleaned_data_course.append(b)
    
    return cleaned_data_course


def data_clean_subjects():
    cur = mydb.cursor()
    query = "select * from home_subjects_data"
    cur.execute(query)
    output = cur.fetchall()
    cleaned_data_s = []
    cleaned_data_sub = []
    for i in output:
        a = i[1].split(',')
        cleaned_data_s.append(a)
    for j in cleaned_data_s[0]:
        a = j.lstrip()
        b = a.rstrip()
        cleaned_data_sub.append(b)
    
    return cleaned_data_sub


def main():
    cleaned_data_teach = data_clean_teach()
    cleaned_data_course = data_clean_course()
    cleaned_data_sub = data_clean_subjects()
    print(cleaned_data_sub)
    print(cleaned_data_teach)
    print(cleaned_data_course)

if __name__ == '__main__':
    main()


