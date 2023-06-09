# Function to check whether the string is palindrome or not
def palindrome(a):
  
    # finding the mid, start and last index of the string
    mid = (len(a)-1)//2     
    start = 0              
    last = len(a)-1
    flag = 0
 
    # A loop till the mid of the string
    while(start <= mid):
        # comparing letters from right and the letters from left
        if (a[start] == a[last]):
            start += 1
            last -= 1
        else:
            flag = 1
            break;  
        
    if flag == 0:
        print("The entered string is palindrome")
    else:
        print("The entered string is not palindrome")

# Function to check whether the
# string is symmetrical or not       
def symmetry(a):
    n = len(a)
    flag = 0
     
    # Check if the string's length is odd or even
    if n%2:
        mid = n//2 +1
    else:
        mid = n//2
         
    start1 = 0
    start2 = mid
     
    while(start1 < mid and start2 < n):
         
        if (a[start1]== a[start2]):
            start1 = start1 + 1
            start2 = start2 + 1
        else:
            flag = 1
            break

    if flag == 0:
        print("The entered string is symmetrical")
    else:
        print("The entered string is not symmetrical")
         
# Driver code
string = 'amaama'
palindrome(string)
symmetry(string)

# Output
# The entered string is palindrome
# The entered string is symmetrical

# Approach 2: We use slicing in this method.

string = 'ababa'
half = int(len(string) / 2)
print(half)
first_str = string[:half]
print(first_str)
second_str = string[half:] 
print(second_str)
# symmetric
if first_str == second_str:
    print(string, 'string is symmetrical')
else:
    print(string, 'string is not symmetrical')
 
# palindrome
if first_str == second_str[::-1]:  # ''.join(reversed(second_str)) [slower]
    print(string, 'string is palindrome')
else:
    print(string, 'string is not palindrome')
# Output
# amaama string is symmetrical
# amaama string is palindrome