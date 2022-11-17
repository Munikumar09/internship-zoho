import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(r"https?://(?:www\.)?youtube\.com/embed/([a-z0-9_]+)", s, re.IGNORECASE):
        id=matches.group(1)
        return "https://youtu.be/"+id
    return None


if __name__ == "__main__":
    main()