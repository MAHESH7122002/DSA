# Example 1:
# Input:N = 4554
# Output:Palindrome Number
# Explanation: The reverse of 4554 is 4554 and therefore it is palindrome number
# Example 2:
# Input:N = 7789
# Output: Not Palindrome
# Explanation: The reverse of number 7789 is 9877 and therefore it is not palindrome


def brute_force(n):
    return int(str(n)[::-1])==n

def optimal(n):
    res=0
    while n>0:
        res=(n%10)+(res*10)
        n=n//10
    return res==n

n=4554
print("Brute Force Approach:",brute_force(n)) #TC-O(N) SC-O(1)
print("Optimal:",optimal(n))     #TC-O(logN) SC-O(1)

#LINK: https://takeuforward.org/data-structure/check-if-a-number-is-palindrome-or-not/