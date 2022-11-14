def main():
    item=input("Item: ")
    calories=get_nutrition(item)
    if calories>=0:
        print(f"Calories: {calories}")
def get_nutrition(item:str)->int:
    calories={
        "Apple":130,
        "Avocado":50,
        "Banana":110,
        "Cantaloupe":50,
        "Grapefruit":60,
        "Grapes":90,
        "Honeydew Melon":50,
        "Kiwifruit":90,
        "Lemon":15,
        "Lime":20,
        "Nectarine":60,
        "Orange":80,
        "Peach":60,
        "Pear":100,
        "Pineapple":50,
        "Plums":70,
        "Strawberries":50,
        "Sweet Cherries":100,
        "Tangerine":50,
        "Watermelon":80

    }
    return calories.get(item.title(),-1)
if __name__=="__main__":
    main()