# Example 1:
# Input:N = 153
# Output:True
# Explanation: 13+53+33 = 1 + 125 + 27 = 153
# Example 2:
# Input:N = 371
# Output: True
# Explanation: 33+53+13 = 27 + 343 + 1 = 371

def optimal(n):
    import math
    res=0
    digit_cnt = int(math.log10(n))+1
    while n>0:
        res+=(n%10)**digit_cnt
        n=n//10
    return res==n

print("Optimal:",optimal(153))      #TC-O(logN+1) SC-O(1)

#Link: https://takeuforward.org/maths/check-if-a-number-is-armstrong-number-or-not/