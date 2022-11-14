def main():
    user_input=input("Input: ")
    print(remove_vowels(user_input))
def remove_vowels(input:str)->str:
    output=""
    vowels=['a','e','i','o','u','A','E','I','O','U']
    for c in input:
        if c not in vowels:
            output+=c
    return output
if __name__=="__main__":
    main()