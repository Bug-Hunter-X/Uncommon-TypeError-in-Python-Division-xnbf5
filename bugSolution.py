def function_with_uncommon_error(a, b):
    try:
        if not isinstance(a,(int, float)) or not isinstance(b,(int, float)):
            raise TypeError("Invalid input types: Both arguments must be numbers.")
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError as e:
        print(f"Error: {e}")
        return None

# Example of the bug being handled correctly
result = function_with_uncommon_error(10, "hello")
print(result)  # Output: Error: Invalid input types: Both arguments must be numbers.
None
result = function_with_uncommon_error(10, 0)
print(result) # Output: Error: Division by zero
None
result = function_with_uncommon_error(10,2)
print(result) # Output: 5.0