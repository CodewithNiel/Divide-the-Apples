'''
Author: Niel
Date: 21 March 2021
Purpose: Python Practice
'''

n = int(input("Enter the number of apples that Harry has "
              "got\n"))
mn = int(input("What is the minimum number\n"))
mx = int(input("What is the maximum number\n"))


# Error handling
if mn == mx:
    print(f"This is not a range and {mn} is equal to {mx}.")
elif mn >= mx or mn > mx:
    print(f"This is not a range and {mn} is greater than"
          f" {mx}.")

# loop iterating from the given mn number to mx number +1
for i in range(mn, mx+1):
    if n%i == 0:
        print(f"{i} is the divisor of {n}")
    elif n%i != 0:
        print(f"{i} is not a divisor of {n}")

# Example
# if n = 20 and mn = 2 and mx = 5
#     2 is the divisor of 20
#     3 is not a divisor of 20
#     4 is a divisor of 20
#     5 is a divisor of 20