'''
The Knuth-Morris-Pratt(KMP) algorithm is a pattern matching algorithm that is based on a precomputed prefix function
that stores the information of an overlapping text portion in the pattern. The KMP algorithm preprocesses this pattern
to avoid this unnecessary comparisons when using the prefix function. the algorithm utilizes the prefix function to estimate
how much the pattern should be shifted to search the apttern in the text string whenever we get a mismatch.
The KMP algorithm is efficient as it minimizes the comparisons of the given patterns with the respect of the text string.

The Prfix Function
The prefix function(also known as failure function) finds the pattern in the pattern itself. It rises to find how much the previous
comparisons can be reused due to repetition in the pattern itself when there is a mismatch. It has a value that is
mainly the longest prefix, which is also a suffix.

The KMP pattern amtching algorithm uses a pattern that has overlap in the pattern itself so that it avoids unncessary
comparisons. The main idea behind KMP algorithm is to dteect how much the pattern should be shifted, based on the overlaps
in the patterns. The algrithm works as follows:
1. First, we precompute the prefix function for the given pattern and initialize a counter, q, that represents the number
   of charaters that matched.
2. We startby comparing the first character of the pattern with the first character of the text string, and we compare the
   next character.
3. If there is a mismatch, then we assign the value of the precomputed prefix function for q to the index value of q.
4. We continue searching for the pattern in the text string until we reach the end of the text, that is, if we do not
   find any matches. If all of the characters in the pattern are matched in the text sttring, we return the position
   where the pattern is matched in the text and continue to search for another match.

The KMP algorithm has two phases, the preprocessing phase, which is where we compute the prefix function, it takes
the space and time complexity of O(m) and further, in the second phase, that searching, the KMP algorithm takes time
complexity of  O(n).
'''

def pfun(pattern): # function to generate prefix function for the given pattern
    n = len(pattern)
    prefix_fun = [0]*n
    k = 0

    for q in range(2, n):
        while k>0 and pattern[k+1] != pattern[q]:
            k = prefix_fun[k]
        if pattern[k+1] == pattern[q]:
            k += 1
        prefix_fun[q] = k
    return prefix_fun

def KMP_Matcher(text, pattern):
    m = len(text)
    n = len(pattern)
    flag = False
    text = '-'+text # append dummy character at the beginning to start index from 1
    pattern = '-'+pattern
    prefix_fun = pfun(pattern)
    q = 0
    for i in range(1, m+1):
        while q>0 and pattern[q+1] != text[i]:
            q = prefix_fun[q]
        if pattern[q+1] == text[i]:
            q += 1
        if q == n:
            print("Pattern occurs with shift",i-n)
            flag = True
        if not flag:
            print("\n No match found")



KMP_Matcher('aabaacaadaabaaba', 'abaac')