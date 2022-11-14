def main():
    camel_case=input("camelCase: ")
    print(f"snake_case: {convert_to_snake_case(camel_case)}")
def convert_to_snake_case(camel_case_str:str)->str:
    snake_case=""
    for c in camel_case_str:
        if c>="A" and c<="Z":
            c="_"+chr(ord(c)+32)
        snake_case+=c
    return snake_case
if __name__=="__main__":
    main()