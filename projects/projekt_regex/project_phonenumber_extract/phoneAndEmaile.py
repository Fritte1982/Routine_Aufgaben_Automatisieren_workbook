# phoneAndEmail.py - Findet Telefonnummern und E-Mail-Adressen
# in der Zwischenablage.
import pyperclip, re

url_nostarch_contact = "https://nostarch.com/contactus"

test_string:str = """Contact Us
Reach Us by Email - email is the best way to reach us
Help with your order: support@nostarch.com
General inquiries: info@nostarch.com
Bulk orders and special sales questions: sales@nostarch.com
Academic requests: academic@nostarch.com (Further information)
Conference and event inquiries: conferences@nostarch.com
Errata - please send any errata reports to: errata@nostarch.com
Media requests: media@nostarch.com
Proposals or editorial inquiries: editors@nostarch.com
Rights inquiries: rights@nostarch.com (Further information)
Interested in working with us? 
View our current job openings
Reach Us by Mail
Mailing Address

No Starch Press
329 Primrose Road,  #42
Burlingame, CA 94010-4093
USA

NOTE: Below are our business phone numbers but we are a completely remote company. Please email support@nostarch.com with your questions and we will do our best to promptly resolve any issues that you may have.

Phone: 800.420.7240 or +1 415.863.9900
Fax: +1 415.863.9950

Reach Us on Social Media
Twitter Facebook Instagram Linkedin Pinterest"""



phoneregex = re.compile(r"""(
(\d{3}|\(\d{3}\))?                          # Bereichsvorwahl
)
""",re.VERBOSE )