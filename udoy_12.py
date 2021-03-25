# Regular Expressions Ranges

import re

# Ranges

# ranges [ a-z ], [ A, Z], [ 0-9 ]
text = "Do you know how to be a script kiddi? It's simple, just copy me. 2"

out1 = re.findall('[a-z]+', text)
ou1 = re.findall('[0-9]+', text)
# print(out)


out2 = re.findall('[A-Z]+', text)
# print(out2)

out3 = re.findall('[A-Z][a-z]+', text)
# print(out3)

out4 = re.findall('[A-Za-z]+', text)
# print(out4)