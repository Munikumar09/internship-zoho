def main():
    user_input=input("Greeting: ")
    print(f"${get_prize( user_input)}")
def get_prize(greetings:str)->int:
    greetings=greetings.lstrip().lower()
    prize=0
    if greetings[0]!='h':
        prize= 100
    elif greetings[0]=='h' and greetings[0:5]!='hello':
        prize=20
    return prize
main()