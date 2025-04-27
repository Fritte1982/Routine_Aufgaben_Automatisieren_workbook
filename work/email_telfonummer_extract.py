import re, pyo

test_string: str = """DVFA Deutsche Vereinigung für Finanzanalyse und Asset Management GmbH

Mainzer Landstraße 47a
D-60329 Frankfurt am Main
Telefon +49 69 26 48 48 0
Telefax +49 69 26 48 48 488
eMail: info@dvfa.de
Internet: www.dvfa.de

Vertretungsberechtigter Geschäftsführer: Klaus Beinke

Registergericht: Amtsgericht Frankfurt am Main
Registernummer: HRB 87820

Umsatzsteuer-Identifikationsnummer gemäß §27a Umsatzsteuergesetz:
VAT DE 113543720

Inhaltlich verantwortlich (gemäß § 55 Abs. 2 RStV): Klaus Beinke, DVFA GmbH, Mainzer Landstraße 47a, D-60329 Frankfurt am Main

Haftungshinweis: Trotz sorgfältiger inhaltlicher Kontrolle übernehmen wir keine Haftung für die Inhalte externer Links. Für den Inhalt der verlinkten Seiten sind ausschließlich deren Betreiber verantwortlich.

Weitere rechtliche Hinweise entnehmen Sie bitte unserem Disclaimer (englisch).

CCrA - Certified Credit Analyst, CEFA - Certified European Financial Analyst, CeFM - Certified Financial Manager, CIIA - Certified International Investment Analyst, CREA - Certified Real Estate Investment Analyst, CRM - Certified Risk Manager und SCC_ Small Cap Conference sind geschützte Marken der DVFA GmbH.


Stand: 01. April 2020"""

phoneRegEx = re.compile(r"""(
    (\+\d{2,3})  # Länderkennung
    (\s|-|\.)?
    (\d{1,4})         # Erster Nummernblock
    (\s|-|\.)?        # Optionales Trennzeichen
    (\d{1,4})         # Zweiter Nummernblock
    (\s|-|\.)?        # Optionales Trennzeichen
    (\d{1,4})         # Dritter Nummernblock
    (\s|-|\.)?        # Optionales Trennzeichen
    (\d{1,4})?        # Vierter Nummernblock (optional)
    (\s|-|\.)?        # Optionales Trennzeichen
    (\d{1,4})?        # Vierter Nummernblock (optional)
    
)""",re.VERBOSE )

matches =phoneRegEx.findall(test_string)

ergebnisString = ''
for match in matches:
    #print(match[0])
    ergebnisString = ergebnisString +'  '+ str(match[0])

ergebnisString =ergebnisString.strip().replace("  ", ", ")

email_regex = re.compile(r"""
    \b
    \w+
    @
    \w+
    \.
    \w{2,4}
    \b
    """, re.VERBOSE)

email_match =  email_regex.findall(test_string)

for mail_match in email_match:
    ergebnisString = ergebnisString + "  "+ str(email_match [0])
    
ergebnisString =ergebnisString.strip().replace("  ","\n")


