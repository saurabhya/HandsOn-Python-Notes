"""
    Let’s learn to check the correctness of user-input formatting.
    Say you write a web application that calculates health statistics
    based on the sleep duration of your users. Your users enter the
    time they went to bed and the time they wake up. An example
    for a correct time format is 12:45, but because web bots are
    spamming your user input fields, a lot of “dirty” data is
    causing unnecessary processing overhead on your servers. To
    address this issue, you write a time-format checker that
    determines whether the input is worth processing further with
    your backend application. With regular expressions, writing
    the code takes only a few minutes.

    We'll use the regex pattern{m,n} that matches between m and n instances of the
    regex pattern, but no more no less.
"""

import re

print(re.findall('x{3,5}y','xy'))

print(re.findall('x{3,5}y','xxxy'))

print(re.findall('x{3,5}y','xxxxxy'))

print(re.findall('x{3,5}y','xxxxxxy'))

"""
    Our goal is to write a function input_ok that takes a string
    argument and checks whether it has the (time) format XX:XX,
    where X is a number from 0 to 9.
"""

## Data
inputs = ['18:29', '23:55', '123', 'ab:de', '18:299', '99:99']

input_ok = lambda x: re.fullmatch('[0-9]{2}:[0-9]{2}', x) != None

## Result
for x in inputs:
    print(input_ok(x))