# comp.py
simp_module_called = False

def sum_of_digits(number):
    """Calculate the sum of digits of a given number."""
    # Check if simp_module_called flag is set
    if not simp_module_called:
        print("Functions in comp module cannot be called before calling at least one function in simp module.")
    else:
        return result
  # or raise an exception, depending on your requirements
    
    # Convert the number to a string to iterate through its digits
    num_str = str(number)
    
    # Use a list comprehension to get individual digits as integers
    digits = [int(digit) for digit in num_str]

    # Calculate the sum of digits
    result = sum(digits)

    # Print the sum of digits
    print(f"The sum of digits in {number} is: {result}")

    # Return the result if needed
    return result



    
    
    
       

# comp.py

def ispal(number):
    """Check if a number is a palindrome."""
    num_str = str(number)
    return num_str == num_str[::-1]
