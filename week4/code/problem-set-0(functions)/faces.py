def convert(s:str)-> str:
    result=""
    i=0
    while i < len(s)-1:
        c=s[i]
        if s[i]==":":
            if s[i+1]==")":
                c="🙂"
                i+=1
            elif s[i+1]=="(":
                c="🙁"
                i+=1
        result+=c
        i+=1
    return result
def main():
    user_input=input()
    print(convert(user_input))
main()