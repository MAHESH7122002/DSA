# Example 1:
# Input:N = 12345
# Output:5
# Explanation:  The number 12345 has 5 digits.
# Example 2:
# Input:N = 7789
# Output: 4
# Explanation: The number 7789 has 4 digits.

def brute_force(n):
    cnt=0
    while n>0:
        cnt+=1
        n=n//10
    return cnt

def optimal(n):
    import math
    return int(math.log10(n))+1

n=1234
res1 = brute_force(n)
res2 = optimal(n)
print(res1) #TC-O(logN) SC-O(1)
print(res2) #TC-O(1) SC-O(1)

#LINK: https://takeuforward.org/data-structure/count-digits-in-a-number/