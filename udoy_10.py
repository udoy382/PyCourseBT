# Regular Expressions 2

import re

# Character Sets

'''

[ ab ] - a or b
s[ ab ]+ - s with one or more a or b

'''

text = "This is a sample paragraph. Do you like paragliding?. No I like parasailing."
out  = re.findall('[pa]+', text)
out  = re.findall('para[sg]+', text)
print(out)