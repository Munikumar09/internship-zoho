def main():
    user_input=input("Expression: ")
    print(calculate(user_input))
def calculate(expression:str)->float:
    a,b,c=expression.split(" ")
    a=float(a)
    c=float(c)
    match b:
        case "+":
            return a+c
        case "-":
            return a-c
        case "/":
            return a/c
        case "*":
            return a*c
main()