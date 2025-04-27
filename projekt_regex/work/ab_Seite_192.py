import re 
from icecream import ic

txt:str = "415-555-4242"
message:str = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
false_txt:str = "der Aufruf mit 'Moshi moshi' dagegen False"

def is_telefnumber(txt:str)-> bool:
    if len(txt) != 12:
        return False
    for i in range(3):
        if not txt[i].isdecimal():
            return False
    if txt[3] != '-':
        return False
    for i in range(4,7):
        if not txt[i].isdecimal():
            return False
        if txt[7] != '-':
            return False
    for i in range(8, len(txt)):
        if not txt[i].isdecimal():
            return False
    return True

def find_telenumber_in_string(txt: str)->str:
    find = 0
    for i in range(len(txt)):
        temp = txt[i: i+12]
        if is_telefnumber(temp):
            print("Found:",  temp)
            find  = find + 1    
    if find <= 0:
        print("No Match. ")

pattern= r"(\d{3})-(\d{3}-\d{4})"
def regex_all(string:str, regex:str)-> list[str] | str | list[tuple[str]]:
    regex = re.compile(regex)
    list_result_string =regex.findall(string)
    if not list_result_string:
        return "Keine Telfonummer gfunden. "
    return list_result_string


def main():
    ic(regex_all(message, pattern))


if __name__ == '__main__':
    main()