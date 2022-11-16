def main():
    while True:
        try:
            date=get_date()
            print(f"{int(date[2]):04d}-{int(date[0]):02d}-{int(date[1]):02d}")
        except EOFError:
            break
def get_date():
    while True:
        try:
            input_date=input().strip()
            delimeter=None
            if '/' in input_date:
                if len(date := slash_format(input_date))>0:
                    return date
            elif ',' in input_date:
                return space_format(input_date)
        except ValueError:
            continue
def slash_format(input_date:str)-> list:
    date=input_date.split('/')
    return validate_date(date)
def space_format(input_date:str)->list:
    months=[
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
    date=input_date.split(' ')
    if date[0].title() in months:
        date[0]=months.index(date[0].title())+1
    date[1]=date[1][:-1]
    return validate_date(date)

def validate_date(date):
    if int(date[0])>12 or int(date[1])>31:
        return []
    return date

main()