import random

def main():
    time_table = Data()
    print("Time Table:")
    for i in time_table:
        print(i,time_table[i])
        print()
   

def Data():
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

def Logic(class_name, Periods, working_days):
    days = ['Mon', 'Tue', 'Wed','Thurs','Fri','Sat','Sun']
    working_days = days[:working_days]
    sudo_slots = {}
    for Class_name in class_name:
        sudo_slots[Class_name] = [{j:{f'Slot{i}': None for i in range(Periods)}} for j in working_days] 
    return sudo_slots

def arrangement(sec_sub, room_avl, times,days,teach_subs,sudo_tt):
    list_sec_sub = list(sec_sub)
    days_ = ['Mon', 'Tue', 'Wed','Thurs','Fri','Sat','Sun']
    is_room_avl = set(room_avl['Extra'])
    is_teach_avl = set(teach_subs)
    working_day = days_[:days['working_day']]
    for index, i in enumerate(working_day):
        for k in range(days['each_day']):
            for l in list_sec_sub:
                try:
                    if 'Lab' in sudo_tt[l][index][i][f'Slot{k-1}']:
                        continue
                except:
                    pass
                ran = random.choice(sec_sub[l])
                
                try:
                    if 'Lab' in ran and is_room_avl:
                        for lab,subject in room_avl['Extra'].items():
                            if ran in subject:
                                is_room_avl.remove(lab)
                                if sudo_tt[l][index][i][f'Slot{k}'] == None and sudo_tt[l][index][i][f'Slot{k+1}'] == None:
                                    print('hi')
                                    sudo_tt[l][index][i][f'Slot{k}'] = ran
                                    sudo_tt[l][index][i][f'Slot{k+1}'] = ran
                                else:
                                    sudo_tt = placement(l,index,i,k,sudo_tt,sec_sub,is_room_avl,room_avl,is_teach_avl,teach_subs)
                        else:
                            sudo_tt = placement(l,index,i,k,sudo_tt,sec_sub,is_room_avl,room_avl,is_teach_avl,teach_subs)
                    elif is_teach_avl:
                        for teach, subject in teach_subs.items():
                            if ran in subject:
                                is_teach_avl.remove(teach)
                                sudo_tt[l][index][i][f'Slot{k}'] = ran
                                break
                        else:
                            sudo_tt = placement(l,index,i,k,sudo_tt,sec_sub,is_room_avl,room_avl,is_teach_avl,teach_subs)
                    else:
                        sudo_tt = placement(l,index,i,k,sudo_tt,sec_sub,is_room_avl,room_avl,is_teach_avl,teach_subs)
                except KeyError:
                    sudo_tt = placement(l,index,i,k,sudo_tt,sec_sub,is_room_avl,room_avl,is_teach_avl,teach_subs)
                    
            is_room_avl = set(room_avl)
            is_teach_avl = set(teach_subs)
    
    return sudo_tt
                        

def placement(l,index,i,k,sudo_tt,sec_sub,is_room_avl,room_avl,is_teach_avl,teach_subs):
    ran = random.choice(sec_sub[l])
    try:
        if 'Lab' in ran and is_room_avl:
            for lab,subject in room_avl['Extra'].items():
                if ran in subject:
                    is_room_avl.remove(lab)
                    if sudo_tt[l][index][i][f'Slot{k}'] == None and sudo_tt[l][index][i][f'Slot{k+1}'] == None:
                        sudo_tt[l][index][i][f'Slot{k}'] = ran
                        sudo_tt[l][index][i][f'Slot{k+1}'] = ran
                    else:
                        sudo_tt = placement(l,index,i,k,sudo_tt,sec_sub,is_room_avl,room_avl,is_teach_avl,teach_subs)
            else:
                placement(l,index,i,k,sudo_tt,sec_sub,is_room_avl,room_avl,is_teach_avl,teach_subs)
        elif is_teach_avl:
            for teach, subject in teach_subs.items():
                if ran in subject:
                    is_teach_avl.remove(teach)
                    sudo_tt[l][index][i][f'Slot{k}'] = ran
                    break
            else:
                placement(l,index,i,k,sudo_tt,sec_sub,is_room_avl,room_avl,is_teach_avl,teach_subs)
        else:
            placement(l,index,i,k,sudo_tt,sec_sub,is_room_avl,room_avl,is_teach_avl,teach_subs)
    except KeyError:
        placement(l,index,i,k,sudo_tt,sec_sub,is_room_avl,room_avl,is_teach_avl,teach_subs)
            
    is_room_avl = set(room_avl)
    is_teach_avl = set(teach_subs)
    return sudo_tt

if __name__ == '__main__':
    main()
