import re

txt = "Agent Alice gave the secret documents to Agent Bob."
names_regex =r"Agent \b\w+\b"
names_regex = re.compile(names_regex)
ersetzter_txt = names_regex.sub("CENSORED", txt)
print(ersetzter_txt)

agentNamesRegex = r"Agent (\w)\w+"
agentNamesRegex = re.compile(agentNamesRegex)
ersetzter_txt = agentNamesRegex.sub(r"\1****", txt)
print(ersetzter_txt)