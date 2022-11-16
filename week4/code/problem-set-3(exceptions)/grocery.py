def main():
    grocery=get_grocery_list()
    display_items(grocery)
def get_grocery_list()-> dict:
    grocery_list={}
    while True:
        try:
            item=input().strip().upper()
            grocery_list[item]=grocery_list.get(item,0)+1
        except EOFError:
             break
    return grocery_list
def display_items(grocery:dict)->None:
    for item,frequency in sorted(grocery.items()):
        print(frequency,item)
if __name__=="__main__":
    main()

