'''
The Boyer-Moore pattern matching algorithm is another such algorithm that further improves the
performance of pattern matching by skipping some comparisons using some methods. You need to understand
the following concepts to be able to use the Boyer-Moore algorithm:
1. In this algorithm, we shift the pattern in the direction from left to right, similar to the KP algorithm.
2. We compare the characters of the pattern and the text string from the right to the left direction,
   which is the opposite of the KMP algorithm.
3. The algorithm skips the unnecessary comparisons by using the good-suffix and bad-character shifts concept.

The Boyer Moore algorithmcompares the pattern over the text from right to the left. It uses the information
of the various possible alignments in the pattern by preprocessing it. the main idea of this algorithm is that
we compare the end characters of the pattern with the text. If they do not match, then the pattern can be
moved on further. If the characters do not match in th end, there is no need for further comaprisons.
'''