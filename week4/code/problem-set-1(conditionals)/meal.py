def main():
    time_24hours_format=input("What time is it? ")
    time=convert(time_24hours_format)
    type_of_meal=""
    if 7<=time<=8:
        type_of_meal="breakfast time"
    elif 12<=time<=13:
        type_of_meal="lunch time"
    elif 18<=time<=19:
        type_of_meal="dinner time"
    print(type_of_meal)

def convert(time_24f:str)->float:
    time_24f=time_24f.strip()
    time_split=time_24f.split(":")
    time=float(time_split[0])+float(time_split[1])/60
    return time
if __name__=="__main__":
    main()