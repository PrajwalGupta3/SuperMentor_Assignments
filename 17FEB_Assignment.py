#Assignment (17/02/2026)

#Assignment Name : Logic Builder
#Description : Print numbers 1–50 with Fizz/Buzz logic and count occurrences using loops and functions.
def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)       
fizz_count = 0
buzz_count = 0  
for i in range(1, 51):
    result = fizz_buzz(i)
    print(result)
    if result == "Fizz":
        fizz_count += 1
    elif result == "Buzz":
        buzz_count += 1
print(f"Fizz count: {fizz_count}")
print(f"Buzz count: {buzz_count}")
