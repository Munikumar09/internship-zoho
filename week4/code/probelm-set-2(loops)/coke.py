def main():
    get_input()
def get_input():
    due=50
    while True:
        print(f"Amount Due: {due}")
        coin=int(input("Insert Coin: "))
        if coin==25 or coin == 10 or coin ==5:
            due=due-coin
        if due<=0:
            print(f"Amount Owed: {due* (-1)}")
            break
if __name__=="__main__":
    main()