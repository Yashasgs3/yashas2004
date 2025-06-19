# Function to swap two numbers using tuple unpacking
def swap_numbers(a, b):
    print("Before swapping: a =", a, ", b =", b)
    
    # Swapping using tuple unpacking
    a, b = b, a
    
    print("After swapping: a =", a, ", b =", b)

# Example usage
num1 = 5
num2 = 10
swap_numbers(num1, num2)
