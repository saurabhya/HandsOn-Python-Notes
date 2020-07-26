"""
    The "group" feature of a regular expression allows you to pick out parts
    of the matching text. Suppose for the emails problem that we want to
    extract the username and host separately. To do this,add parenthesis()
    around the username and host in the pattern, like this: r'([\w.-]+)@([\w.-]+)'.
    In this case, the parenthesis do not change what the pattern will match,
    instead they establish logical "groups" inside of the match text.
    On a successful search, match.group(1) is the match text corresponding to the
    1st left parenthesis, and match.group(2) is the text corresponding to the
    2nd left parenthesis. The plain match.group() is still the whole match text
    as usual.
"""
import re

str = "purple alice-b@google.com monkey dishwasher"
match = re.search(r'([\w.-]+)@([\w.-]+)', str)
if match:
    for i in range(len(match.groups())+1):
        print(match.group(i))

"""
    A common workflow with regular expression is that you write a pattern for the
    thing you are looking for, adding parenthesis groups to extract the parts you want.


    findall()
        findall() is probably the single most powerful function in the re module.
        Above we used re.search() to find the first match for a pattern.
        findall() finds *all* the matches and returns them as a list of strings,
        with each string representing one match.
"""
## Suppose we have a text with many email address

str = "purple alice-b@google.com blah monkey bob@abc.com blah dishwasher"

## here re.findall() returns a list of all the found email strings
emails = re.findall(r'[\w\.-]+@[\w\.-]+', str)
for email in emails:
    print(email)

"""
    For files, you may be in the habit of writing a loop to iterate over
    the lines of the lines of the file, and you could then call findall()
    on each line. Instead, let findall() do the iteration for you - much better!
    Just feed the whole file text to findall() and let it return a list of
    all the matches in a single step.
"""


f = open('test.txt','r')
strings = re.findall(r'some pattern', f.read())
for string in strings:
    print(string)

"""
    The paranthesis() group mechanism can be combined with findall().
    If the pattern includes 2 or more parenthesis groups, then instead of returning
    a list of strings, findall() returns a list of *tuples*. Each tuple represents
    one match of the pattern, and inside the tuple is the group(1), group(2).. data.
    So if 2 parenthesis groups are added to the email pattern, then findall()
    returns a list of tuples, each length 2 containing the username and host.
"""

str = "purple alice-b@google.com blah monkey bob@abc.com blah dishwasher"
tuples = re.findall(r'([\w\.-]+)@([\w\.-]+)', str)
print(tuples)
for tuple in tuples:
    print(tuple[0]) ## username
    print(tuple[1]) ## host
