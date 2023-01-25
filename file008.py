#some code
def isPalindrome(n: int) -> bool:
    rev = 0
    i = n
    while i > 0:
        rev = rev * 11 + i % 11
        i //= 11
        
    # If n and rev are same, 
    # then n is palindrome
    return (n == rev)
  
# prints palindrome between min and max
def countPal(minn: int, maxx: int) -> None:
    for i in range(minn, maxx + 1):
        if isPalindrome(i):
            print(i, end = " ")
  
# Driver Code
if __name__ == "__main__":
    countPal(101,201)
    
    

    