import random
import mysql.connector as sql

def Database():
    mydb = sql.connect(
    host="localhost",
    user="new_user",
    password="password",database = "timetable"
    )
    
    cur_home_course_data = mydb.cursor()
    cur_home_course_data.execute('select * from home_course_data')
    data1 = cur_home_course_data.fetchall()

    cur_home_teacher_data = mydb.cursor()
    cur_home_teacher_data.execute('select * from home_teacher_data')
    data2 = cur_home_teacher_data.fetchall()

    cur_home_timing_data = mydb.cursor()
    cur_home_timing_data.execute('select * from home_timing_data')
    data3 = cur_home_timing_data.fetchall()

    cur_home_workingdays_data = mydb.cursor()
    cur_home_workingdays_data.execute('select * from home_workingdays_data')
    data4 = cur_home_workingdays_data.fetchall()

    cur_home_infrastructure_data = mydb.cursor()
    cur_home_infrastructure_data.execute('select * from home_infrastructure_data')
    data5 = cur_home_infrastructure_data.fetchall()

    # key variables: sec_subjects, classes,time,day, teacher
    sec_subjects = {}
    classes = {}
    time = {}
    day = {}
    teacher = {}
    
    for i in data1:
        sec_subjects[i[1]] = i[3].split(',')
    

    
    for i in data2:
        teacher[i[1]] = i[3].split(',')
    

    
    for i in data3:
        time[i[2]] = i[1]
    

    
    for i in data4:
        day[i[1]] = i[2]
    

    for i in data5:
        if i[1] in classes:
            classes[i[1]][i[2]] = i[3].split(',')
        else:
            classes[i[1]] = {i[2]: i[3].split(',')}

    class_name = list(sec_subjects)
    each_day = day['Each day']
    working_days = day['Working days']
    sudo_slots = Logic(class_name, each_day, working_days)
    time_table = arrangement(sec_subjects, classes,time,day, teacher,sudo_slots)
    mydb.close()
    return time_table, each_day,working_days

def main():
    time_table, each_day, working_days = Database()
    days_var = ['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday']
    final = {}
    tt = {}
    for data,value in time_table.items():
        index = 0
        for item in value:
            for f in item:
                day_s = item[f]
                var = list(day_s.values())
            final[days_var[index]]=var
            index += 1
        tt[data] = final
    return tt, each_day, working_days
   

def Logic(class_name, Periods, working_days):
    days = ['Mon', 'Tue', 'Wed','Thurs','Fri','Sat','Sun']
    working_days = days[:working_days]
    sudo_slots = {}
    for Class_name in class_name:
        sudo_slots[Class_name] = [{j:{f'Slot{i}': None for i in range(Periods)}} for j in working_days] 
    return sudo_slots

'''def Data():
    sec_subjects = {'B.tech 1':['Python','Engineering','Python(Lab)','MySql','MySql(Lab)','Bootstrap'],
               'B.tech 2':['Java','Java(Lab)','Artificial Intelligence','AI(Lab)','JavaScript','Numpy','Deeplearning'],
               'Bca 1':['HTML','HTML(Lab)','CSS','C','Data Structure','Pandas'],
               'Bca 2':['Bootstrap','Pytorch','Pytorch(Lab)','Machine Learning','ML(Lab)','Data Science']}
    classes = {'Study':{'Lt1':'B.tech 1','Lt2':'B.tech 2','Lt3':'Bca 1','Lt4':'Bca 2'},'Extra':{'Lab1':['Python(Lab)','AI(Lab)','Pytorch(Lab)','ML(Lab)'],'Lab2':['MySql(Lab)','HTML(Lab)','Java(Lab)']}}
    time = {'Classes':50, 'Labs':100} # time is in minutes
    day = {'each_day':4, 'working_day':5}
    teacher = {'Vibhor':['Python','C','Java','Engineering','Python(Lab)','C(Lab)','Java(Lab)'],
               'Vibhor Singh':['HTML', 'CSS','JavaScript','Bootstrap','HTML(Lab)'],
               'Vibhor Singh Bisht':['Artificial Intelligence', 'Machine Learning', 'Deeplearning','AI(Lab)','ML(Lab)'],
               'VSB':['Pytorch', 'Numpy', 'Pandas',"Pytorch(Lab)"],
               'Vibhor Bisht':['MySql', 'Data Science', 'Data Structure','MySql(Lab)']
               }
    class_name = list(sec_subjects)
    each_day = day['each_day']
    working_days = day['working_day']
    sudo_slots = Logic(class_name, each_day, working_days)
    time_table = arrangement(sec_subjects, classes,time,day, teacher,sudo_slots)
    return time_table
'''

def arrangement(sec_sub, room_avl, times,days,teach_subs,sudo_tt):
    list_sec_sub = list(sec_sub)
    days_ = ['Mon', 'Tue', 'Wed','Thurs','Fri','Sat','Sun']
    is_room_avl = set(room_avl['Extra'])
    is_teach_avl = set(teach_subs)
    working_day = days_[:days['Working days']]
    for index, i in enumerate(working_day):
        for k in range(days['Each day']):
            for l in list_sec_sub:
                try:
                    if 'Lab' in sudo_tt[l][index][i][f'Slot{k-1}'] and k == 1:
                        continue
                    elif ('Lab' in sudo_tt[l][index][i][f'Slot{k-1}']) and ('Lab' in sudo_tt[l][index][i][f'Slot{k-2}']):
                        pass
                    elif 'Lab' in sudo_tt[l][index][i][f'Slot{k-1}']:
                        continue
                except:
                    pass
                ran = random.choice(sec_sub[l])
                
                try:
                    if 'Lab' in ran and is_room_avl:
                        for lab,subject in room_avl['Extra'].items():
                            if ran in subject:
                                if sudo_tt[l][index][i][f'Slot{k}'] == None and sudo_tt[l][index][i][f'Slot{k+1}'] == None:
                                    is_room_avl.remove(lab)
                                    sudo_tt[l][index][i][f'Slot{k}'] = ran
                                    sudo_tt[l][index][i][f'Slot{k+1}'] = ran
                                else:
                                    sudo_tt, is_room_avl, is_teach_avl = placement(l,index,i,k,sudo_tt,sec_sub,is_room_avl,room_avl,is_teach_avl,teach_subs)
                                    
                    elif is_teach_avl:
                        for teach, subject in teach_subs.items():
                            if ran in subject:
                                is_teach_avl.remove(teach)
                                sudo_tt[l][index][i][f'Slot{k}'] = ran
                                break
        
                    else:
                        continue
                except KeyError:
                    sudo_tt, is_room_avl, is_teach_avl = placement(l,index,i,k,sudo_tt,sec_sub,is_room_avl,room_avl,is_teach_avl,teach_subs)
                    
            is_room_avl = set(room_avl['Extra'])
            is_teach_avl = set(teach_subs)
    return sudo_tt
                        

def placement(l,index,i,k,sudo_tt,sec_sub,is_room_avl,room_avl,is_teach_avl,teach_subs):
    ran = random.choice(sec_sub[l])
    try:
            if 'Lab' in ran and is_room_avl:
                for lab,subject in room_avl['Extra'].items():
                    if ran in subject:
                        if sudo_tt[l][index][i][f'Slot{k}'] == None and sudo_tt[l][index][i][f'Slot{k+1}'] == None:
                            is_room_avl.remove(lab)
                            sudo_tt[l][index][i][f'Slot{k}'] = ran
                            sudo_tt[l][index][i][f'Slot{k+1}'] = ran
                        else:
                            sudo_tt, is_room_avl, is_teach_avl = placement(l,index,i,k,sudo_tt,sec_sub,is_room_avl,room_avl,is_teach_avl,teach_subs)

            elif is_teach_avl:
                for teach, subject in teach_subs.items():
                    if ran in subject:
                        is_teach_avl.remove(teach)
                        sudo_tt[l][index][i][f'Slot{k}'] = ran
                        break

    except KeyError:
            sudo_tt, is_room_avl, is_teach_avl = placement(l,index,i,k,sudo_tt,sec_sub,is_room_avl,room_avl,is_teach_avl,teach_subs)

            
    return sudo_tt, is_room_avl, is_teach_avl

if __name__ == '__main__':
    main()
