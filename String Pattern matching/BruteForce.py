'''
    The brute-force or naive approach for the pattern matching algorithm, is very basic. Using this, we simply test all the possible
    ombinations of the input pattern in the given string to find the position of the ocurence of the pattern. this algorithm is very
    naive and is not suitable if the text is very long.

    Here, we start by comparing the characters of the pattern and the text string one by one, and if all the characters of the
    pattern are matched with text, we return the index position of the text where the first character of the pattern is placed.
    If any character of the pattern is mismatched with the text string, we shift the pattern by one place. we continue comparing
    The pattern and text string by shifting the pattern by one index position.
'''

def brute_force(text, pattern):
    l1 = len(text)
    l2 = len(pattern)
    i = 0
    j = 0
    flag = False
    while i<l1:
        j = 0
        count = 0
        while j<l2:
            if i+j < l1 and text[i+j] == pattern[j]:
                count += 1
            j += 1
            if count == l2:
                print("\nPattern occurs at index : {}".format(i))
                flag = True
        i += 1
    if not flag:
        print("\nPattern is not at all present in the array")

brute_force('acbcabccababcaacbcac', 'acbcac')
