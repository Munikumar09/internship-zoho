import datetime
import sys


class NumToWordConverter:
    less_than_20 = [
        "",
        "One",
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Eleven",
        "Twelve",
        "Thirteen",
        "Fourteen",
        "Fifteen",
        "Sixteen",
        "Seventeen",
        "Eighteen",
        "Nineteen",
    ]
    tens = [
        "",
        "Ten",
        "Twenty",
        "Thirty",
        "Forty",
        "Fifty",
        "Sixty",
        "Seventy",
        "Eighty",
        "Ninety",
    ]
    thousands = ["", "thousand", "million", "billion"]
    def num_to_word(self,num):
        if num==0:
            return "zero"
        ans=""
        i=0
        while num>0:
            if num%1000 !=0:
                ans=self.get_word(num%1000)+" "+self.thousands[i]+", "+ans
                i+=1
                num=num//1000
        return ans.strip()
    def get_word(self,num):
        if num==0:
            return ""
        elif num<20:
            return self.less_than_20[num]
        elif num<100:
            return self.tens[num//10]+"-"+self.get_word(num%10)
        else:
            return self.less_than_20[num//100]+" hundred "+self.get_word(num%100)



def main():
    dob = input("Date of Birth: ")
    print(age_in_seconds(dob))


def age_in_seconds(dob):
    try:
        dob_date = datetime.datetime.strptime(dob, "%Y-%m-%d").date()
        today_date = datetime.date.today()
        delta = today_date - dob_date
        age_in_seconds = delta.days * 24 * 60
        num_to_word_converter=NumToWordConverter()
        words=num_to_word_converter.num_to_word(age_in_seconds)
        words=(words[:-1]).strip()
        while words[-1]=='-' or words[-1]==',':
            words=(words[:-1]).strip()
        words=(words+" minutes").capitalize()
        return words
    except ValueError:
        sys.exit("Invalid Date")


if __name__ == "__main__":
    main()
