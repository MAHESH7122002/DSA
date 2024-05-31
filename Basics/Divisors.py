# Example 1:
# Input:N = 36
# Output:[1, 2, 3, 4, 6, 9, 12, 18, 36]
# Explanation: The divisors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, 36.
# Example 2:
# Input:N =12
# Output: [1, 2, 3, 4, 6, 12]
# Explanation: The divisors of 12 are 1, 2, 3, 4, 6, 12.


def brute_force(n):
    return  [i for i in range(1,n+1) if n%i==0]

def optimal(n):
    import math
    res=[]
    m=int(math.sqrt(n))
    for i in range(1,m+1):
        if n%i==0:
            res.append(i)
            if i!=n//i:
                res.append(n//i)
    return res
n=36
print("Brute Force Approach:",brute_force(n)) #TC-O(N) SC-O(N)
print("Optimal:",optimal(n))     #TC-O(sqrtN) SC-O(sqrtN)

#Link: https://takeuforward.org/data-structure/print-all-divisors-of-a-given-number/