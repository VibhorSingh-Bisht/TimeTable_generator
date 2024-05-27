
def data_clean_teach(data):
    cleaned_data_teach = []
    baba = data.split(',')
    for j in baba:
        a = j.lstrip()
        b = a.rstrip()
        cleaned_data_teach.append(b)
        
    return cleaned_data_teach


def data_clean_course(data):
    cleaned_data_course = []
    c = data.split(',')
    for j in c:
        a = j.lstrip()
        b = a.rstrip()
        cleaned_data_course.append(b)
    
    return cleaned_data_course


def data_clean_subjects(data):
    cleaned_data_sub = []
    aba = data.split(',')
    for j in aba:
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


