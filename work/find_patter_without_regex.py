import re

example_number = "415-555-4242"
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
def is_phone_number(txt: str) -> bool:
    if len(txt) != 12:
        return False
    for i in range(0, 3):
        if not txt[i].isdecimal():
            return False
    if txt[3] != '-':
        return False
    for i in range(4, 7):
        if not txt[i].isdecimal():
            return False
    if txt[7] != '-':
        return False
    for i in range(8, 12):
        if not txt[i].isdecimal():
            return False
    return True

print(is_phone_number(example_number))

def is_phone_number_with_regex (txt: str) -> bool:
    regex = r"\d{3}-\d{3}-\d{4}"
    pattern= re.compile(regex)
    if pattern.search(txt):
        return True
    else:
        return False

for i in range(len(message)):
    chunk=message[i:i+12]
    if is_phone_number_with_regex(chunk):
        print(f"Nummer: {chunk}")
print("erledigt")

regex = r"\d{3}-\d{3}-\d{4}"
pattern= re.compile(regex)
numbers = pattern.findall(message)

for match in numbers:
    print("nummer", str(match))