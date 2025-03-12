def is_narc(n):#funcname_error
    """Check if a number is narc."""
    num_str = str(n)
    num_digits = len(num_str)
    
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)#there were three asteriks
    
    return sum_of_powers == n

def print_narcis_numbers(start ,end):#colon error
    """Print all narc numbers in a given range."""
    for num in range(start, end + 1): #colon error
        if is_narc(num): #colon error,funcname_error
            print(num)

print_narcis_numbers(1000, 5000)