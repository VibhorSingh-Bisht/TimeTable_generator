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
            if len(i[3].split(',')) == 1:
                string = i[3].split(',')[0]
                classes[i[1]][i[2]] = string
            else:
                classes[i[1]][i[2]] = i[3].split(',')
        else:
            if len(i[3].split(',')) == 1:
                string = i[3].split(',')[0]
                classes[i[1]] = {i[2]: string}
            else:
                classes[i[1]] = {i[2]: i[3].split(',')}
    mydb.close()
    class_name = list(sec_subjects)
    each_day = day['Each day']
    working_days = day['Working days']
    teacher_names = list(teacher)
    Labs_name = list(classes['Extra'])
    sudo_slots, sudo_slots_teach, sudo_slots_lab = Logic(class_name, each_day, working_days,teacher_names,Labs_name)
    time_table, sudo_slots_teach, sudo_slots_lab = arrangement(sec_subjects, classes,day, teacher,sudo_slots,sudo_slots_teach, sudo_slots_lab)
    return time_table,working_days,each_day, sudo_slots_teach, sudo_slots_lab




def main():
    time_table,working_days,each_day, sudo_slots_teach, sudo_slots_labs = Database()
    print('Time Table')

    days_var = ['Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday']
    final = {}
    tt = {}
    tt_teach = {}
    tt_labs = {}
    for data,value in time_table.items():
        index = 0
        for item in value:
            for f in item:
                day_s = item[f]
                var = list(day_s.values())
            final[days_var[index]]=var
            index += 1
        tt[data] = final

    for data,value in sudo_slots_teach.items():
        index = 0
        for item in value:
            for f in item:
                day_s = item[f]
                var = list(day_s.values())
            final[days_var[index]]=var
            index += 1
        tt_teach[data] = final

    for data,value in sudo_slots_labs.items():
        index = 0
        for item in value:
            for f in item:
                day_s = item[f]
                var = list(day_s.values())
            final[days_var[index]]=var
            index += 1
        tt_labs[data] = final

    print(tt)
    print(tt_teach)
    print(tt_labs)
        
    return tt,working_days,each_day, tt_teach, tt_labs

    

'''def Data(sec_subjects,classes,time,day,teacher, sudo_teach, sudo_lab):
    sec_subjects = {'B.tech 1':['Python','Engineering','Python(Lab)','MySql','MySql(Lab)','Bootstrap'],
               'B.tech 2':['Java','Java(Lab)','Artificial Intelligence','AI(Lab)','JavaScript','Numpy','Deeplearning'],
               'Bca 1':['HTML','HTML(Lab)','CSS','C','Data Structure','Pandas'],
               'Bca 2':['Bootstrap','Pytorch','Pytorch(Lab)','Machine Learning','ML(Lab)','Data Science']}
    #classes = {'Study':{'Lt1':'B.tech 1','Lt2':'B.tech 2','Lt3':'Bca 1','Lt4':'Bca 2'},'Extra':{'Lab1':['Python(Lab)','AI(Lab)','Pytorch(Lab)','ML(Lab)'],'Lab2':['MySql(Lab)','HTML(Lab)','Java(Lab)']}}
    #time = {'Classes':50, 'Labs':100} # time is in minutes
    #day = {'Each day':4, 'Working days':5}
    teacher = {'Vibhor':['Python','C','Java','Engineering','Python(Lab)','C(Lab)','Java(Lab)'],
               'Vibhor Singh':['HTML', 'CSS','JavaScript','Bootstrap','HTML(Lab)'],
               'Vibhor Singh Bisht':['Artificial Intelligence', 'Machine Learning', 'Deeplearning','AI(Lab)','ML(Lab)'],
               'VSB':['Pytorch', 'Numpy', 'Pandas',"Pytorch(Lab)"],
               'Vibhor Bisht':['MySql', 'Data Science', 'Data Structure','MySql(Lab)']
               }
    class_name = list(sec_subjects)
    each_day = day['Each day']
    working_days = day['Working days']
    sudo_slots,sudo_slots_teach, sudo_slots_labs = Logic(class_name, each_day, working_days,sudo_teach,sudo_lab)
    time_table = arrangement(sec_subjects, classes,day, teacher,sudo_slots,sudo_teach, sudo_lab)
    return time_table, sudo_slots_teach, sudo_slots_labs'''

def Logic(class_name, Periods, working_days,teacher_name,Labs_name):
    sudo_slots_teach = {}
    sudo_slots_labs = {}
    days = ['Mon', 'Tue', 'Wed','Thurs','Fri','Sat','Sun']
    working_days = days[:working_days]
    sudo_slots = {}
    for Class_name in class_name:
        sudo_slots[Class_name] = [{j:{f'Slot{i}': None for i in range(Periods)}} for j in working_days]

    for Teacher_name in teacher_name:
        sudo_slots_teach[Teacher_name] = [{j:{f'Slot{i}': None for i in range(Periods)}} for j in working_days]

    for Lab_Name in Labs_name:
        sudo_slots_labs[Lab_Name] = [{j:{f'Slot{i}': None for i in range(Periods)}} for j in working_days]

    return sudo_slots , sudo_slots_teach, sudo_slots_labs

def arrangement(sec_sub, room_avl, days,teach_subs,sudo_tt,sudo_slots_teach, sudo_slots_labs):
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
                                if (sudo_tt[l][index][i][f'Slot{k}']) == None and (sudo_tt[l][index][i][f'Slot{k+1}'] == None):
                                    is_room_avl.remove(lab)
                                    sudo_tt[l][index][i][f'Slot{k}'] = ran
                                    sudo_tt[l][index][i][f'Slot{k+1}'] = ran
                                    sudo_slots_labs[lab][index][i]['Slot{k}'] = ran
                                    sudo_slots_labs[lab][index][i][f'Slot{k+1}'] = ran
                                    break
                                else:
                                    sudo_tt, is_room_avl, is_teach_avl, sudo_slots_teach, sudo_slots_lab = placement(l,index,i,k,sudo_tt,sec_sub,is_room_avl,room_avl,is_teach_avl,teach_subs,sudo_slots_teach, sudo_slots_labs)
                        
                    elif is_teach_avl:
                        for teach, subject in teach_subs.items():
                            if ran in subject:
                                is_teach_avl.remove(teach)
                                sudo_tt[l][index][i][f'Slot{k}'] = ran
                                sudo_slots_teach[teach][index][i][f'Slot{k}'] = ran
                                break
        
                except KeyError:
                    sudo_tt, is_room_avl, is_teach_avl,sudo_slots_teach, sudo_slots_lab = placement(l,index,i,k,sudo_tt,sec_sub,is_room_avl,room_avl,is_teach_avl,teach_subs,sudo_slots_teach, sudo_slots_labs)
                    
                    
            is_room_avl = set(room_avl['Extra'])
            is_teach_avl = set(teach_subs)
    return sudo_tt, sudo_slots_teach, sudo_slots_lab
                        

def placement(l,index,i,k,sudo_tt,sec_sub,is_room_avl,room_avl,is_teach_avl,teach_subs,sudo_slots_teach, sudo_slots_labs):
    ran = random.choice(sec_sub[l])
    try:
            if 'Lab' in ran and is_room_avl:
                for lab,subject in room_avl['Extra'].items():
                    if ran in subject:
                        if sudo_tt[l][index][i][f'Slot{k}'] == None and sudo_tt[l][index][i][f'Slot{k+1}'] == None:
                            is_room_avl.remove(lab)
                            sudo_tt[l][index][i][f'Slot{k}'] = ran
                            sudo_tt[l][index][i][f'Slot{k+1}'] = ran
                            sudo_slots_labs[lab][index][i][f'Slot{k}'] = ran
                            sudo_slots_labs[lab][index][i][f'Slot{k+1}'] = ran
                        else:
                            sudo_tt, is_room_avl, is_teach_avl,sudo_slots_teach, sudo_slots_labs = placement(l,index,i,k,sudo_tt,sec_sub,is_room_avl,room_avl,is_teach_avl,teach_subs,sudo_slots_teach, sudo_slots_labs)
                            

            elif is_teach_avl:
                for teach, subject in teach_subs.items():
                    if ran in subject:
                        is_teach_avl.remove(teach)
                        sudo_tt[l][index][i][f'Slot{k}'] = ran
                        sudo_slots_teach[teach][index][i][f'Slot{k}'] = ran
                        break

    except KeyError:
            sudo_tt, is_room_avl, is_teach_avl,sudo_slots_teach, sudo_slots_labs = placement(l,index,i,k,sudo_tt,sec_sub,is_room_avl,room_avl,is_teach_avl,teach_subs,sudo_slots_teach, sudo_slots_labs)
            

            
    return sudo_tt, is_room_avl, is_teach_avl, sudo_slots_teach, sudo_slots_labs

if __name__ == '__main__':
    main()
