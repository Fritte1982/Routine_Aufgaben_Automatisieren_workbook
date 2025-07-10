import re
from pathlib import Path
print(Path.cwd())
path_with_txt = Path.cwd()


such_ausdruck1 = r"(Schrödinger)"
such_ausdruck1 = re.compile(such_ausdruck1, re.VERBOSE)
c = []
generator =[]
x = []

machtes = []
for element in path_with_txt.iterdir():
    if element.is_file() and element.name.endswith(".txt"):
        generator.append(element)
#print(generator)        
for file in generator:        
    c.append(file.read_text("UTF-8").split("\n"))
for i in c:
    for j in i:
        x = x + j.split("\n")
for g in x:
    if such_ausdruck1.findall(g):
        machtes.append(g)
    for i in machtes:
        if i in g:
            print(g)    
   # 
   #print(such_ausdruck1.findall(g))
#print(machtes)        
