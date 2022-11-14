def main():
    user_input=input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    print(is_correct(user_input))
def is_correct(answer:str)->str:
    answer=answer.lower().strip()
    if answer=="42" or answer=="forty-two" or answer=="forty two":
        return "Yes"
    else:
        return "No"
main()