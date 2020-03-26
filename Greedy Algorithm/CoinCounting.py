'''
COIN COUNTING PROBLEM

we wish to compute the minimum number of coin required to make a given amount A, where we have an infinte
supply of the given coin's values.

The algorithm to obtain the minimum numer of coins to provide a given amount A using denominations
(a1,a2,a3...an):
1. We sort the list of denominations (a1,a2,a3...an).
2. we get the largest denominations in (a1,a2,a3...an) which is smaller than A.
3. We obtain the division by dividing A by the largest denominations.
4. We get remaining amount of A by getting remainder.
5. If the value of A becomses 0, we return the result.
6. Else if the value of A is greater than 0, we append the largest denomination
   and division variable in the result variable. And repeat the steps 2-5.
'''
def basic_small_change(denom, total_amount):
    sorted_denom = sorted(denom, reverse= True)

    number_of_denoms = []
    for i in sorted_denom:
        div = total_amount//i
        total_amount = total_amount%i
        if div > 0:
            number_of_denoms.append((i,div))
    return number_of_denoms

'''
However, there are some possible instances where this algorithm may fail.

A better greedy algorithm is presetedhere. this time, the funtion retuens
a list of tuples that allow us to invistigate the best results.
'''

def optimal_small_change(denom, total_amount):
    sorted_denom = sorted(denom, reverse= True)
    series = []
    for j in range(len(sorted_denom)):
        term = sorted_denom[j:]
        number_of_denoms = []
        local_total = total_amount
        for i in term:
            div = local_total//i
            local_total = local_total%i
            if div > 0:
                number_of_denoms.append((i, div))
        series.append(number_of_denoms)
    return series
