import re

from projects.projekt_regex.work.complexer_expressions import phoneRegex

example_txt = """Skip to main content
Home
Shopping cart
0 Items	Total: $0.00
Search
Enter your keywords 
Catalog
Merchandise
Blog
Early Access
Write for Us
About Us
Contact Us
Topics
Art & Design
General Computing
Hacking & Computer Security
Hardware / DIY
Kids
LEGO®
Linux & BSD
Manga
Programming
Python
R for All
Science & Math
Scratch
System Administration
Early Access
FREE ebook edition with every print book purchased from nostarch.com!
+

EARLY ACCESS lets you read full chapters months before a title's release date!
User login
Log in
Create account
Contact Us
Reach Us by Email - email is the best way to reach us
General inquiries or help with an order: info@nostarch.com
Bulk orders and special sales questions: sales@nostarch.com
Academic requests: academic@nostarch.com (Further information)
Conference and event inquiries: conferences@nostarch.com
Errata - please send any errata reports to: errata@nostarch.com
Media requests: media@nostarch.com
Proposals or editorial inquiries: editors@nostarch.com
Rights inquiries: rights@nostarch.com (Further information)
Interested in working with us? 
View our current job openings
Physical Address
No Starch Press Inc
245 8th Street
San Francisco, CA 94103
USA

Mailing Address
No Starch Press Inc
329 Primrose Road,  #42
Burlingame, CA 94010-4093
USA

Phone: 800.420.7240 or +1 415.863.9900
Fax: +1 415.863.9950

Reach Us on Social Media
Twitter Facebook Instagram Linkedin Pinterest

 
 

Navigation
My account
Want sweet deals?
Sign up for our newsletter.


About Us  |  Jobs!  |  Sales and Distribution  |  Rights  |  Media  |  Academic Requests  |  Conferences  |  FAQ  |  Contact Us  |  Write for Us  |  Privacy
Copyright 2025. No Starch Press, Inc"""

phoneRegex: re.Pattern = re.compile(r"""((:?\+\d\s)?(:?\d{3})?
\.\d{3}\.\d{4})""", re.VERBOSE)


# Regulärer Ausdruck für E-Mail-Adressen
emailRegex = re.compile(r'''( 
 [a-zA-Z0-9._%+-]+                      # Benutzername 
 @                                      # @-Symbol 2
 [a-zA-Z0-9.-]+                         # Domänenname 
 (\.[a-zA-Z]{2,4})                      # Punkt + irgendetwas 
 )''', re.VERBOSE)

machts_phone:list[str] = phoneRegex.findall(example_txt)

matches = []
for groups in phoneRegex.findall(example_txt):
    matches.append(groups[0])
for groups in emailRegex.findall(example_txt):
    matches.append(groups[0])

print(matches)