'''
    The Boyer-Moore pattern matching algorithm is another such algorithm that further improves the
    performance of pattern matching by skipping some comparisons using some methods. You need to understand
    the following concepts to be able to use the Boyer-Moore algorithm:
    1. In this algorithm, we shift the pattern in the direction from left to right, similar to the KP algorithm.
    2. We compare the characters of the pattern and the text string from the right to the left direction,
       which is the opposite of the KMP algorithm.
    3. The algorithm skips the unnecessary comparisons by using the good-suffix and bad-character shifts concept.

    The Boyer Moore algorithm compares the pattern over the text from right to the left. It uses the information
    of the various possible alignments in the pattern by preprocessing it. the main idea of this algorithm is that
    we compare the end characters of the pattern with the text. If they do not match, then the pattern can be
    moved on further. If the characters do not match in the end, there is no need for further comparisons.

    The Boyer-Moore algorithm has two heuristics to determine the maximum shift possible for the pattern where we find
    a mismatch:
    1. Bad Character Heuristic
    2. Good suffix Heuristic

    At the time of mismatch, each of these heuristics suggests possible shifts, and the Boyer-Moore algorithm shifts
    the pattern by considering the maximum shift possible due to bad character and good suffix heuristics.
'''

text  = "acbaacacababacacac"
pattern = "acacac"

matched_index = []
i = 0
flag = True
while i<=len(text)-len(pattern):
    for j in range(len(pattern)-1,-1,-1):#reverse searching from right to left
        if pattern[j] != text[i+j]:
            flag = False #there is a mismatch
            if j == len(pattern)-1:# if good suffix is not pressent we check bad character
                if text[i+j] in pattern[0:j]:
                    i = i+j - pattern[0:j].rfind(text[i+j]) # i+j is index of bad character, this line is used for jumping pattern to match bad character of text with same character in the pattern
                else:
                    i = i+j+1 #if bad character is not present
            else:
                k = 1
                while text[i+j+k:i+len(pattern)] not in pattern[0:len(pattern)-1]: #used for finding sub-part of good suffix
                    k = k+1
                if len(text[i+j+k:i+len(pattern)]) != 1:
                    gsshift = i+j+k-pattern[0:len(pattern)-1].rfind(text[i+j+k:i+len(pattern)]) #jumps pattern to a position where good-suffix of patter matches with good-suffix of text
                else:
                    gsshift = 0
                if text[i+j] in pattern[0:j]:
                    bcshift = i+j-pattern[0:j].rfind(text[i+j])
                else:
                    bcshift = i+j+1
                i = max((bcshift, gsshift))
            break
    if flag:
        matched_index.append(i)
        i = i+1
    else:
        flag = True
print("Pattern found at", matched_index)
