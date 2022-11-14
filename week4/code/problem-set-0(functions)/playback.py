def convert_space_to_dots(s:str)->str:
    result=""
    for c in s:
        if c==" ":
            c="..."
        result+=c
    return result
user_input=input()
print(convert_space_to_dots(user_input))