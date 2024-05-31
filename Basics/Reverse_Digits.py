# Example 1:
# Input:N = 12345
# Output:54321
# Explanation: The reverse of 12345 is 54321.
# Example 2:
# Input:N = 7789
# Output: 9877
# Explanation: The reverse of number 7789 is 9877.

def brute_force(n):
    return int(str(n)[::-1])

def optimal(n):
    res=0
    while n>0:
        res=(n%10)+(res*10)
        n=n//10
    return res

n=7789
print("Brute Force Approach:",brute_force(n)) #TC-O(N) SC-O(1)
print("Optimal:",optimal(n))     #TC-O(logN) SC-O(1)

#LINK: https://takeuforward.org/maths/reverse-digits-of-a-number