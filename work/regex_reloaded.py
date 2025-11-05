import re

phone_regex = re.compile(r"""
( 
(\d{3}|\(\d{3}\))?              # Bereichsvorwahl
(\s|-|\.)?                      # Trennzeichen
\d{3}                           # Erste 3 stellen
(\s|-|\.)                       # Trennzeichen
\d{4}                           # Letzte 4 Stellen
(\s*(ext|x|ext.)\s*\d{2,5})?    # Durchwahl
)""", re.VERBOSE)

# TODO nicht nur Email, Name u. Tele-Nr. extrahieren gleich in ein MSSQL-Insert-Skript bringen.