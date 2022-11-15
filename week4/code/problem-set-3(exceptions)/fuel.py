import math
def main():
    print(get_input())
def get_input()-> str:
    try:
        fuel=input("Fraction: ").split("/")
        fraction=round((int(fuel[0])/int(fuel[1]))*100)
        if fraction>100:
            return get_input()
        if fraction<=1:
            return "E"
        elif fraction>=99:
            return "F"
        else:
            return str(fraction)+"%"
    except (ValueError,ZeroDivisionError):
        return get_input()

if __name__=="__main__":
    main()