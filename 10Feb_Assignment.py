#1)Print if given no. is odd or even 
"""""
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is an even number.")    
else:
    print(num, "is an odd number.")

"""
#2)print numbers from 10 to 1
"""
for i in range(10, 0, -1):
    print(i)
"""
#3)Keep taking input ffrom user and sum them until user enters 0
"""
total_sum = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total_sum += num
print("The total sum is:", total_sum)
"""