## Generates time according to the organization

def main(iterations=4, start_hour=8, start_minute=50,increment_time = 50, special_break = 10):
    l = []
    l.append(f'{start_hour:02d}:{start_minute:02d}')
    if iterations > 6:
        iterations += 1
    for i in range(iterations):
        if i == 2:
            start_minute += special_break
            l.append(f'{start_hour:02d}:{start_minute:02d}')
            continue
        start_minute += increment_time
        if start_minute >= 60:
            start_hour += 1 
            start_minute %= 60
        l.append(f'{start_hour:02d}:{start_minute:02d}') 
        #hour = 0
    return l 

if __name__ == "__main__":
    print(main())
