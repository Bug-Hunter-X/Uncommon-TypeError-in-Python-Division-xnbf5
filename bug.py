def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid input types")
        return None

# Example of the bug: passing a string as an argument
result = function_with_uncommon_error(10, "hello")
print(result)  # Output: Error: Invalid input types
None