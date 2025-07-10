import re

class RegexClass:
    def __init__(self,txt, regex) -> None:
        regex = rf"{regex}"
        self.txt = txt
        self.regex = regex
    
    def set_attribute(self,text=None, regex= None):
        if text:
            self.txt = text
        if regex:
            self.regex = regex
    
    def RegExSearch(self):
        self.compRegex = re.compile(fr"{self.regex}")
        self.mo = self.compRegex.search(self.txt)
        return self.mo
    
    def ausgabe_group(self, gruppe:int= 0)-> str:
        match = self.RegExSearch()
        if match:
            return match.group(gruppe)
        else:
            return "None, Kein Match gefunden. "
    
    def all_in_one(self, txt=None, regex = None, gruppe = 0):
        if txt or regex:
            self.set_attribute(txt, regex)
        self.match_group = self.ausgabe_group(gruppe)
        return self.match_group
    
    