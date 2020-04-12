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

"""
    Above, we're defining the variables that we plan to POST to the url we apecify.
    From there, below, we're needing to first url encode all of the values.
    This is basically things like converting "spaces" to %20, for example

    Then we encode to the utf-8 bytes. We make our request,
    by adding in one more value, data, which is the encoded dictionary of keys
    and values, or better understood in this scenario as variables and
    their values. Then we open the url with the request that we've built,
    which we call a response, since that's what we get with it. Finally, we read
    that response with a.read().
"""
data = urllib.parse.urlencode(values)
data = data.encode('utf-8') # data should be in bytes
#req = urllib.request.Request(url, data)
#resp = urllib.request.urlopen(req)
#respData = resp.read()

#print(respData)

"""
    Whenever you visit a link, you send in a header, which is just some basic information
    about you. This is how Google Analytics knows what browser you are using.

    Within the header, there is a value called user-agent, which defines the browser
    that is accessing the website's server.
    If you are using the default python user-agent with urllib, then you are announcing
    yourself as Python-urllib/3.4, if Python version is 3.4. This is either foreign to
    the website, or they will just block it entirely. A work around for this is to just
    identify yourself as something else.
"""
try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    #print(x.read())
    savefile = open('noheaders.txt', 'w')
    savefile.write(str(x.read()))
    savefile.close()
except Exception as e:
    print(str(e))

"""
    The above output is from Google, who knows you are Python. Over the years, how Google
    and other websites have handled programs has changed, so this might change as well in time.
    The current response they are giving is just a default search page, once you parse through
    all the mess of code that is returned.

"""
try:
    url = 'https://www.google.com/search?q=python'
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    savefile = open('withheaders.txt', 'w')
    savefile.write(str(respData))
    savefile.close()
except Exception as e:
    print(str(e))