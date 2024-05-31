# Example 1:
# Input:N = 2
# Output:True
# Explanation: 2 is a prime number because it has two divisors: 1 and 2 (the number itself).

# Example 2:
# Input:N =10
# Output: False
# Explanation: 10 is not prime, it is a composite number because it has 4 divisors: 1, 2, 5 and 10.

def brute_force(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def optimal(n):
    import math
    m=int(math.sqrt(n))+1
    for i in range(2,m):
        if n%i==0 and n//i!=i:
                return False
    return True

n=38
print("Brute Force Approach:",brute_force(n)) #TC-O(N) SC-O(1)
print("Optimal:",optimal(n))     #TC-O(logN) SC-O(1)

#Link: https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/