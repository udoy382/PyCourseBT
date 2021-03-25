import re

text = "The Hacker news A hacker make a script and hack%the govornment bank in Bangladesh this is most powerful script be safe"

match = re.search('script', text)
# print(type(match))
# print(match.start())
# print(match.end())

# use [ % ] this since for split the text...

# print(re.split('%', text))
# print(text.split('%'))

# out = re.findall('hacker', text)
# print(out)

#---------------------------------
# if re.search('script', text):
#     print("Match was found")
# else:
#     print("Match was nto found")
