# Prime number area
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Area where the user's need to give a positive prime number to start the program
def display_primes_in_range(start, end):
    if start < 0:
        print("Please enter a non-negative number.")
        return
# Condition to start at positive number
    if end <= start:
        print(f"Enter a number greater than {start}.")
        return

    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")


# The Main Program
while True:
    start = int(input("Enter the start number: "))

    if start == 0:
        print("The Program has been terminated.")
        break

    end = int(input("Enter the end number: "))

    display_primes_in_range(start, end)
    print("\n")
