# Python3 implementation of the approach
import math
 
# Function to convert decimal number n
# to its binary representation
# stored as an array arr[]
def decBinary(arr, n):
    k = int(math.log2(n))
    while (n > 0):
        arr[k] = n % 2
        k = k - 1
        n = n//2
 
# Function to convert the number
# represented as a binary array
# arr[] its decimal equivalent
def binaryDec(arr, n):
    ans = 0
    for i in range(0, n):
        ans = ans + (arr[i] << (n - i - 1))
    return ans
 
# Function to concatenate the binary
# numbers and return the decimal result
def concat(m, n):
 
    # Number of bits in both the numbers
    k = int(math.log2(m)) + 1
    l = int(math.log2(n)) + 1
 
    # Convert the bits in both the gers
    # to the arrays a[] and b[]
    a = [0 for i in range(0, k)]
    b = [0 for i in range(0, l)]
 
    # c[] will be the binary array
    # for the result
    c = [0 for i in range(0, k + l)]
    decBinary(a, m)
    decBinary(b, n)
 
    # Update the c[] array
    iin = 0
    for i in range(0, k):
        c[iin] = a[i]
        iin = iin + 1
    for i in range(0, l):
        c[iin] = b[i]
        iin = iin + 1
 
    # Return the decimal equivalent
    # of the result
    return (binaryDec(c, k + l))
 
# Driver code
m = 33
n = 57
 
print(concat(m, n))
 
# This code is contributed by Sanjit_Prasad