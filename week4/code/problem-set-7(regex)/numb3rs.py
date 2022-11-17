import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.match(r"[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}",ip)==None:
        return False
    blocks=ip.split(".")
    for block in blocks:
        if int(block)<0 or int(block)>255:
            return False
    return True

if __name__ == "__main__":
    main()