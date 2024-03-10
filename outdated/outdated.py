months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

flag = ''
while flag != 'EXIT':
    date_user = input('Date: ')
    if '/' in date_user:
        split_date_user = date_user.split('/')
        year = int(split_date_user[2])
        month = int(split_date_user[0])
        day = int(split_date_user[1])
        if day > 31 or month > 12:
            continue
        else:
            print(f'{year}-{month:02d}-{day:02d}')
            break

    else:
        for item in months:
 #           if item not in date_user:
#                break
            if item in date_user:
                month = months.index(item) + 1
                replaced_date_user = date_user.replace(',', '')
                split_date_user = replaced_date_user.split()
                try:
                    year = int(split_date_user[2])
                    day = int(split_date_user[1])
                    if day > 31 or month > 12:
                        continue
                    else:
                        print(f'{year}-{month:02d}-{day:02d}')
                        flag = 'EXIT'
                        break
                except:
                    continue
