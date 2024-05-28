import random


def main():
    time_table = Data()
    print("Time Table:")
    for i in time_table:
        print(i,time_table[i])
        print()
   

def Data():
    sec_subjects = {'B.Sc. (H) (Data Science) II':['Discrete Mathematics','Probability and Distribution Theory','Object Oriented Programming using C++','Data Structures','Data Warehousing and Mining','Disaster Management'],
               'B.Sc. (H) (Data Science) IV':['Estimation and Inferential Statistics','Introduction to Artificial Intelligence','Applied Data Science  using Python','Operating System','Design and Analysis of Algorithms','Personality Development Programme-II','Applied Data Science  using Python (Lab),Operating System (Lab)','Design and Analysis of Algorithms (Lab)'],
               'B.Sc. (H) (Data Science) VI':["Introduction to Deep Learning,Business Intelligence Tools and Applications",'Data Visualization Techniques','Cyber Security','Entrepreneurship Development','Introduction to Deep Learning (lab)', "Project Work - Phase -II"],
               'BCA (IV)':['Computer Based Numerical and Statistical Techniques','Database Management Systems','Design and Analysis of Algorithm','Programming  in JAVA','E-Commerce','Personality Development Programme-II',
'Computer Based Numerical and Statistical Techniques (Lab)','Database Management Systems (Lab),Design and Analysis of Algorithm (Lab)','Programming  in JAVA (Lab)']}
    
    
    classes = {
    'Study': {
        'Lt1': 'B.tech 1',
        'Lt2': 'B.tech 2',
        'Lt3': 'Bca 1',
        'Lt4': 'Bca 2'
    },
    'Extra': {
        'Lab1': [
            'Discrete Mathematics', 'Probability and Distribution Theory', 'Object Oriented Programming using C++',
            'Data Structures', 'Data Warehousing and Mining', 'Disaster Management',
            'Estimation and Inferential Statistics', 'Introduction to Artificial Intelligence', 
            'Applied Data Science using Python', 'Operating System', 'Design and Analysis of Algorithms', 
            'Personality Development Programme-II', 'Applied Data Science using Python (Lab)', 'Operating System (Lab)', 
            'Design and Analysis of Algorithms (Lab)', 'Introduction to Deep Learning', 
            'Business Intelligence Tools and Applications', 'Data Visualization Techniques', 'Cyber Security', 
            'Entrepreneurship Development', 'Introduction to Deep Learning (lab)', 'Project Work - Phase -II',
            'Computer Based Numerical and Statistical Techniques', 'Database Management Systems', 
            'Design and Analysis of Algorithm', 'Programming in JAVA', 'E-Commerce', 
            'Personality Development Programme-II', 'Computer Based Numerical and Statistical Techniques (Lab)', 
            'Database Management Systems (Lab)', 'Design and Analysis of Algorithm (Lab)', 'Programming in JAVA (Lab)'
        ],
        'Lab2': [
            'Probability and Distribution Theory', 'Object Oriented Programming using C++', 'Data Structures', 
            'Data Warehousing and Mining', 'Disaster Management', 'Estimation and Inferential Statistics', 
            'Introduction to Artificial Intelligence', 'Applied Data Science using Python', 'Operating System', 
            'Design and Analysis of Algorithms', 'Personality Development Programme-II', 'Applied Data Science using Python (Lab)', 
            'Operating System (Lab)', 'Design and Analysis of Algorithms (Lab)', 'Introduction to Deep Learning', 
            'Business Intelligence Tools and Applications', 'Data Visualization Techniques', 'Cyber Security', 
            'Entrepreneurship Development', 'Introduction to Deep Learning (lab)', 'Project Work - Phase -II', 
            'Computer Based Numerical and Statistical Techniques', 'Database Management Systems', 
            'Design and Analysis of Algorithm', 'Programming in JAVA', 'E-Commerce', 
            'Personality Development Programme-II', 'Computer Based Numerical and Statistical Techniques (Lab)', 
            'Database Management Systems (Lab)', 'Design and Analysis of Algorithm (Lab)', 'Programming in JAVA (Lab)'
        ]
    }
}


    time = {'Classes':50, 'Labs':100} # time is in minutes
    day = {'each_day':6, 'working_day':5}
    teacher = {'Harvinder Malhotra':['Cloud Computing'],
               'Dr. Ashutosh Bhatt ':[  'Computer Graphics', 'Formal Languages and Automata Theory',' Data Structures',' Computer Graphics Lab', 'Data Structures Lab'],
               'Mrs. Anupama Mishra'  :['Applied Data Science using Python, Machine Learning & Pattern Recognition',' OOP using Java, Applied Data Science using Python LAB',' Machine Learning & Pattern Recognition LAB',' OOP using Java LAB'],
               'Mr. Bineet Kumar Joshi' :['Network Security',' Artificial Intelligence',' Object Oriented Programming and Design using C++(A)', 'Artificial Intelligence LAB',' Object Oriented Programming and Design using C++ LAB'],
              'Dr. Deepak Srivastava':['Data Base Management Systems', 'Database Management Systems', 'Data Visualization Techniques', 'Database Management Systems Lab', 'Data Base Management Systems LAB'],
              'D.S. Rao':['Machine Learning', 'Introduction to IT Verticals'],
              'Mr. Gaurav Aggarwal':['Data Structures(Section B)', 'Web Development using PHP', 'Data Communication and Computer Networks (Section B)', 'Data Structures(Section B) Lab', 'Web Development using PHP Lab'],
              'Mr. Gaurav Sharma':['Data Communication and Computer Networks(Sec B)', 'Introduction to Deep Learning', 'E-Commerce, CBNST LAB', 'Introduction to Deep Learning Lab'], 
              'Dr. Pooja Joshi':['Data Communication and Computer Networks', 'Programming in JAVA, Operating System', 'Programming in JAVA Lab, Operating System Lab'],
              'Mr. PNS Rao':['Digital Electronics', 'Digital Electronics LAB', 'Computer Organization and Architecture'],
              'PrincyTyagi':['Design and Analysis of Algorithms', 'Operating Systems', 'Design and Analysis of Algorithms Lab', 'Operating Systems Lab', 'Operating Systems Lab'],
              'Mr. Rachit Lakhera':['Computer Organization and Architecture', 'Computer Networks', 'Software Engineering', 'Computer Networks LAB'],
              'Mr. Sanjay Kumar':['Computer Organization and Architecture (Sec-C)', 'Operating System, Data Structures Using ‘C’', 'Operating System LAB', 'Data Structures Using ‘C’ LAB'],
              'Ms. Shivani Sharma':['Theory of Automata', 'Data Communication and Computer Networks', 'Design and Analysis of Algorithm', 'Design and Analysis of Algorithm LAB'],
              'Mr. Satyendra Singh Rawat':['Design and Analysis of Algorithms', 'Cloud Computing Security and Management', 'Compiler Design', 'Design and Analysis of Algorithms LAB', 'Cloud Computing Security and Management LAB', 'Compiler Design LAB'],
              'Ms. Vaishali Gupta' :['Data Warehousing and Mining', 'Data Structures(Sec A)', 'Object Oriented Programming and Design using C++ (Sec C)', 'Data Structures LAB(Sec A)',' Object Oriented Programming and Design using C++ LAB(Sec C)'],
              'Dr. Vibhor Sharma':['Object Oriented Programming Using C++', 'Business Intelligence Tools and Applications', 'Object Oriented Programming and Design using C++(Sec B)', 'Object Oriented Programming Using C++ Lab', 'Object Oriented Programming and Design using C++ Lab (Sec B)'],
              
            'Dr. Vinay Avasthi'  :['Introduction to Cyber Security/Cyber Security'],
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
