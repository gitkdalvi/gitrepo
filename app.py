# A simple Python program

def greet(name):
    return f"Hello, {name}! Welcome to Python."

def add_numbers(a, b):
    return a + b

# Main execution
if __name__ == "__main__":
    print(greet("Kaustubh"))
    
    num1 = 10
    num2 = 20
    result = add_numbers(num1, num2)
    
    print(f"The sum of {num1} and {num2} is {result}")

