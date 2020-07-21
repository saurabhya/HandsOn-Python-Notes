import re

text = "peter piper picked a peck of pickled peppers"

result = re.findall('p.*?e.*?r',text)

print(result)