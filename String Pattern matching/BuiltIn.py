'''
    The prefix of a string s is present at the starting of the string. For example 'He' is the prefix of string "Hello World"
    The suffix of a string s is present at the end of the string. For example 'd' id the suffix of string "Hello World"

    Python has buil-in functions to check whether a string has a given prefix or suffix:
'''
string = "Lorem ipsum dolor sit amet consectetur adioiscing elit"
suffix = "elit"
prefix = "Lorem"

print(string.endswith(suffix))
print(string.startswith(prefix))
