import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if re.search("^[0-9]{1,2}(:[0-9]{1,2})? (AM|PM) to [0-9]{1,2}(:[0-9]{1,2})? (AM|PM)",s):
        times=s.split(" to ")
        print(times)
        print(twelve_to_24(times[0]),"to",twelve_to_24(times[1]))
def twelve_to_24(time_str):
    times=time_str.split(" ")
    if times[-1]=="AM":
        return times[0]
    return int(times[0])+12
if __name__ == "__main__":
    main()
"""
9:00 AM to 5:00 PM
9 AM to 5 PM

"""