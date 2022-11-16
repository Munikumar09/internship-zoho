from pyfiglet import Figlet
import sys
def main():
    if len(sys.argv)==0 or len(sys.argv)==3:
        font="slant"
        if len(sys.argv)==3:
            if sys.argv[1]=='-f' or sys.argv[1]=='--font':
                font=sys.argv[2]
            else:
                sys.exit("invalid usage")

        try:
            f = Figlet(font=font)
            input_text=input()
            f = Figlet(font=font)
            print (f.renderText(input_text))
        except:
            sys.exit("invalid usage")
    else:
        sys.exit("invalid usage")
if __name__=="__main__":
    main()