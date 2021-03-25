# Regular Expressions Exclusions

import re

# Exclusions

'''

^  - not including certain patters

'''

text = "This is a sample exclamation! Don't! overreact. mate?"
out = re.findall('[^!?. ]+', text)
out = re.findall('[^as ]+', text)
print(out)