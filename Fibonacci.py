def fibonacci(n):
    """
    Calculate the n-th Fibonacci number recursively.

    Parameters
    ----------
    n : int
        The position in the Fibonacci sequence.

    Returns
    -------
    int
        The n-th Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)




def main():
    """Function main of the module.

    The function main of this module is used to test the function fibonacci.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """
    print("=================================================================.")
    print("Test Case 1: Calculate the 0-th Fibonacci number.")
    print("=================================================================.")
    if fibonacci(0) == 0:
        print("Test PASS. The 0-th Fibonacci number is correct.")
        print("The 0-th Fibonacci number is: ", fibonacci(0))
    else:
        print("Test FAIL. The 0-th Fibonacci number is incorrect.")

    print("=================================================================.")
    print("Test Case 2: Calculate the 1-st Fibonacci number.")
    print("=================================================================.")
    if fibonacci(1) == 1:
        print("Test PASS. The 1-st Fibonacci number is correct.")
        print("The 1-st Fibonacci number is: ", fibonacci(1))
    else:
        print("Test FAIL. The 1-st Fibonacci number is incorrect.")

    print("=================================================================.")
    print("Test Case 3: Calculate the 2-nd Fibonacci number.")
    print("=================================================================.")
    if fibonacci(2) == 1:
        print("Test PASS. The 2-nd Fibonacci number is correct.")
        print("The 2-nd Fibonacci number is: ", fibonacci(2))
    else:
        print("Test FAIL. The 2-nd Fibonacci number is incorrect.")

    print("=================================================================.")
    print("Test Case 4: Calculate the 10-th Fibonacci number.")
    print("=================================================================.")
    if fibonacci(10) == 55:
        print("Test PASS. The 10-th Fibonacci number is correct.")
        print("The 10-th Fibonacci number is: ", fibonacci(10))
    else:
        print("Test FAIL. The 10-th Fibonacci number is incorrect.")

    print("=================================================================.")
    print("Test Case 5: Calculate the 15-th Fibonacci number.")
    print("=================================================================.")
    if fibonacci(15) == 610:
        print("Test PASS. The 15-th Fibonacci number is correct.")
        print("The 15-th Fibonacci number is: ", fibonacci(15))
    else:
        print("Test FAIL. The 15-th Fibonacci number is incorrect.")

    print("=================================================================.")
    print("Test Case 6: Calculate the 20-th Fibonacci number.")
    print("=================================================================.")
    if fibonacci(20) == 6765:
        print("Test PASS. The 20-th Fibonacci number is correct.")
        print("The 20-th Fibonacci number is: ", fibonacci(20))
    else:
        print("Test FAIL. The 20-th Fibonacci number is incorrect.")

if __name__ == "__main__":
    main()

