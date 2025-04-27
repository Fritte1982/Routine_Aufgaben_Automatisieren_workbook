import re

txt = "Batman and Tina Fey."
txt2 = "Tina Fey and Batman"

regex = re.compile(r"Batman|Tina Fey")
mo1 = regex.search(txt)
print(mo1.group())

mo2 = regex.search(txt2)
print(mo2.group())