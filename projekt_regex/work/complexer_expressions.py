import re

## re.VERBOSE erlaubt whitespaces und Kommentar in der Zeile für umfangreichere Ausdrücke.

phoneRegex = re.compile(r"""(
(\d{3}|\(\d{3}\))?              # Bereichsvorwahl
(\s|-|\.)?                      # Trennzeichen
\d{3}                           # ersten 3 Stellen
(\s|-|\.)                       # Trennzeichen
\d{4}                           # letzte 4 Stellen
(\s*(ext|x|ext.)\s*\d{2,5})?    # Durchwahl
)""", re.VERBOSE)

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL) # mit der Pipe "|" können Sie bis zu allen 3 Argumenten angeben.
someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL | re.VERBOSE)

variable = r"""(
(\d{3}|\(\d{3}\))?              # Bereichsvorwahl
(\s|-|\.)?                      # Trennzeichen
\d{3}                           # ersten 3 Stellen
(\s|-|\.)                       # Trennzeichen
\d{4}                           # letzte 4 Stellen
(\s*(ext|x|ext.)\s*\d{2,5})?    # Durchwahl
)"""
phoneRegex = re.compile(variable, re.VERBOSE)