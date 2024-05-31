# Example 1:
# Input:N1 = 9, N2 = 12
                
# Output:3
# Explanation:Factors of 9: 1, 3 and 9
# Factors of 12: 1, 2, 3, 4, 6, 12
# Common Factors: 1, 3 out of which 3 is the greatest hence it is the GCD.
# Example 2:
# Input:N1 = 20, N2 = 15
                
# Output: 5
# Explanation:Factors of 20: 1, 2, 4, 5
# Factors of 15: 1, 3, 5
# Common Factors: 1, 5 out of which 5 is the greatest hence it is the GCD.

def brute_force(n1,n2):
    res=1
    for i in range(1,min(n1,n2)+1):
        if n1%i==0 and n2%i==0:
            res=i
    return res
def better(n1,n2):
    res=1
    for i in range(min(n1,n2)+1,0,-1):
        if n1%i==0 and n2%i==0:
            res=i
    return res
def optimal(n1,n2):
    def gcd(a,b):
        while a>0 and b>0:
            if a>b:
                a=a-b
            else:
                b=b-a
            if a==0:
                return b
        return a

    return gcd(n1,n2)

print("Brute Force Approach:",brute_force(20,15)) #TC-O(min(n1,n2)) SC-O(1)
print("Better Approach:",brute_force(20,15)) #TC-O(min(n1,n2)) SC-O(1)
print("Optimal:",optimal(20,15))      #TC-O(min(n1,n2)) SC-O(1)

#Link: https://takeuforward.org/data-structure/find-gcd-of-two-numbers/
