'''
The rabin-karp matching algorithm is is an improved version of the brute force approach for finding the loaction of given pattern
in the text string. The performance of rabin-karp algorithm is improved by reducing the number of comaprisons with the help
of hashing.

The algorithm is faster than brute force approach as it avoids unnecessary comparisons, character by character.
Instead, the hash alue of the patter is compared with the hash value of the substring of the text string all at once.
If the hash values are not matched, the pattern is moved one position, and so there is no need to compare all the characters
of the pattern one by one.

This algorithm is based on the concept that if the hash values of the two strings are equal, then it is assumed that
both of these strings are also equal. The main problem with this algorith is that there can be two different strings whose
hash values are equal. In that case, the algorithm may not work; this situation is known as spurious hit. To avoid this problem,
after matching the hash values of the pattern and the substring, we ensure that the pattern is actually matched by comparing
them character by character.

The rabin-Karp patern matching algorithm works as follows:
1. First, we preprocess the pattern before starting the search, that is, we cmpute the hash value of the pattern of length m
   and the hash values of all possible substrings of the text of length m. So, the total number of possible substrings
   would be (n-m+1). Here, n is the length of the text.
2. We compare the hash value of the pattern and compare it with the hash value of the substrings of the text one by one.
3. If the hash values are not matched, then we ove the pattern by one position.
4. If the hash alue of the pattern and the hash value of the substring of the text matches, then we compare the pattern and
   substring character by character to ensure that the pattern is actually found in the text.
5. We continue the process of steps 2-4 until we reach the end of the given text string.
'''

def generate_hash(text, pattern):
    ord_text = [ord(i) for i in text]
    ord_pattern = [ord(j) for j in pattern]
    len_text = len(text)
    len_pattern = len(pattern)
    hash_pattern = sum(ord_pattern)
    len_hash_array = len_text - len_pattern + 1
    hash_text = [0]*len_hash_array
    for i in range(len_hash_array):
        if i == 0:
            hash_text[i] = sum(ord_text[:len_pattern]) #initial value of hash
        else:
            hash_text[i] = ((hash_text[i-1] - ord_text[i-1]) + ord_text[i+len_pattern-1]) #calculating next hash value using previous value.
    return [hash_text, hash_pattern] # returning the hash values

def Rabin_Karp_Matcher(text, pattern):
    text = str(text) # Convert text into string format
    pattern = str(pattern) #Convert pattern into string format
    hash_text, hash_pattern = generate_hash(text, pattern) #generate hash values using gernerate_hash function
    len_text = len(text)
    len_pattern = len(pattern)

    flag = False
    for i in range(len(hash_text)):
        if hash_text[i] == hash_pattern:#if the hash value matches
            count = 0
            for j in range(len_pattern):
                if pattern[j] == text[i+j]:
                    count += 1
                else:
                    brreak
            if count == len_pattern:
                flag = True
    return flag




