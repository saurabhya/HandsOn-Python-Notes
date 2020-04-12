import re

# match = re.search(pat, str)

"""
    The re.search() method takes a regular expression patter and a string and
    searches for that pattern within the string. If the search is successful,
    search() returns a match object or None otherwise. Therefore, the search
    is usually immediately followed by an if-statement to test if the search
    succeeded.
"""
str ="an exmple word:cat!!!"
match = re.search(r'word:\w\w\w', str)

if match:
    print("Found", match.group(0))
else:
    print("Did not find")

"""
    The 'r' at the start of the pattern  string designates a python "raw" string
    which passes through backslashes without change which is very handy for
    regular expressions.

    The power of regular expressions id that they can specify patterns
    not just fixed characters. Here are the most basic patterns which match
    single chars:
    1. a,X,9 <- ordinary characters just match themselves exactly. The meta-
       characters which do not match themselves because they have special meanings
       are: ^$*+?{[]\|()
    2. . (a period) --  matches any single character except newline '\n'
    3. \w --  (lowercase w) matches a single "word" charcter:[a-zA-Z0-9_]
    4. \b --  boundary between word and non-word
    5. \s --  (lowercase s ) matches a single whitespace character:[\n\t\r\f]
    6. \t,\n,\r --  Tab, newline, return
    7. \d --  decimal digit[0-9]
    8. ^ = start, $ = end
    9. \ --  inhibit the "specialness" of a character. So, for example, use \. for
        a preriod.
"""

# Some examples
print(re.search(r'iii', 'piiig'))
print(re.search(r'igs', 'piiig'))

print(re.search(r'..g', 'piiig'))
print(re.search(r'\d\d\d', 'p123g'))
print(re.search(r'\w\w\w', '@@abcd!!'))

"""
    Things get more intersting when you use + and * specify repetition in the pattern
    1. + -- 1 or more ocurences
    2. * -- 0 or more occurences
    3. ? -- match 0 or 1 occurrences of the pattern


"""

# Some examples

print(re.search(r'pi+', 'piiig'))
print(re.search(r'i+', 'piigiiii'))
print(re.search(r'\d\s*\d\s*\d', 'xx1 2   3xx'))
print(re.search(r'\d\s*\d\s*\d', 'xx12  3xx'))
print(re.search(r'\d\s*\d\s*\d', 'xx123xx'))

print(re.search(r'^b\w+', 'foobar'))
print(re.search(r'b\w+', 'foobar'))


# Emails example:

str = 'purple alice-b@google.com monkey dishwasher'
match = re.search(r'\w+@\w+', str)
if match:
    print( match.group())


"""
    Square brackts can be used to indicate a set of chars, so [abc] matches
    'a' or 'b' or 'c'. The codes \w, \s etc. work inside square brackets too
    with the one exception that dot(.) just means a literal dot. For the email
    problem, the square brackets are an easy way to add '.' and '-' to the set
    of chars which can appear around the @ with the pattern r'[\w._]+@[\w.-]+'
    to get the whole email address.
"""
match = re.search(r'[\w._]+@[\w.-]+', str)
if match:
    print(match.group())