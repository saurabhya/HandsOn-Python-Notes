"""
    The urllib in Python 3 allows you to access websites via your program.
    This opens as many doors for your programs as the internet opens up for you.
    urllib in Python3 isslightly different than urllib2 in Python3, but they are
    mostly the same. Through urllib, you can access websites, download data,
    parse data, modify your headers, and do any GET and POST rquests you might
    need to do.
    Here is the first and easiest example of using urllib. We just need to import
    urllib.requests. From there, we assign the opening of the url to a variable,
    where we can finally use a.read() command to read the data. The result is a
    massive mess, but we did indeed read the source code.
"""
# Used to make requests
import urllib.request

x = urllib.request.urlopen('https://www.google.com')
print(x.read())

"""
    We can use regular expressions to clean up the result. The problem is web pages
    use all sorts of HTML, CSS and javascript to make webpages appending to the eye.
    Our program really just don't ccare what the website looks like. We just want the
    text usually, so we need to get rid of all the unnecessary stuff, to do that we
    need the power of regex.

    Sometimes, we want to put in values, or GET/POST, from/to a URL. There are two
    methods of data transfer with urls, and they are GET and POST. The natural method
    is a GET requests, which means you make a request and you get data.
    The other is POST, where you send data into the srever, like you post some data,
    and you get a request based on the post.
    An example:
    https://pythonprogramming.net/?s=basics&submit=Search

    Here, there are two variables, first denoted with a question mark, and all of
    the subsequent ones are denoted with the & sign.
    Similarly, there are multiple ways to pass values through like this,
    you can just hard-code them, or you can use urllib to do it.


"""

# used to parse value into the url
import urllib.parse

url = 'https://www.google.com/search'
values = {'q':'python tutorials'}