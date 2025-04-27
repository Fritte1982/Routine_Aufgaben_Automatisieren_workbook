import re



txt ='Cell: 415-555-9999 Work: 212-555-0000'

regex = r"\d{3}-\d{3}-\d{4}"
phoneNumRegex = re.compile(regex)
liste_matches =phoneNumRegex.findall(txt)
print(liste_matches)

regex_groups = r"(\d{3})-(\d{3})-(\d{4})"
phoneNumRegex = re.compile(regex_groups)
list_with_tuples = phoneNumRegex.findall(txt)
print(list_with_tuples)
