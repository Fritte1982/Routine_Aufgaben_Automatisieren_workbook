import re

test_text = "richard "
def own_strip(text:str, char:str = None) -> str:
    regex= r"(?P<space_1>\s*)(?P<word>\w+)(?P<space_2>\s*)"
    if not char:
        char = ""

    def repl_func(m: re.Match):
        left = char if m.group("space_1") else ""
        right = char if m.group("space_2") else ""
        return f"{left}{m.group('word')}{right}"

    new_text = re.sub(regex,  repl_func ,text,0, re.IGNORECASE)
    return new_text

print(own_strip(test_text))

