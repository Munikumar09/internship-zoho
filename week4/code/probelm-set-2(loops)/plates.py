def main():
    plate=input("Plate:")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
def is_valid(plate:str)->str:
    if len(plate)<2 or len(plate)>6:
        return False
    if plate[0].isdigit() or plate[1].isdigit():
        return False
    for c in range(len(plate)):
        if not (plate[c].lower()>='a' and plate[c].lower()<='z' or plate[c].isdigit()):
           return False
        if plate[c].isdigit() and (c!=len(plate)-1 and not plate[c+1].isdigit()):
            return False
        if plate[c]=='0' and (c!=len(plate)-1 and plate[c+1]!=0):
            return False
    return True
if __name__=="__main__":
    main()