def convert_lower_case(s:str)->str:
    result=""
    for c in s:
        if c>="A" and c<="Z":
            c=chr(ord(c)+32)
        result=result+c
    return result
user_input=input()
print(convert_lower_case(user_input))
