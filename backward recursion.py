def backward_sum(n):
    if n == 1:
        return 1  # Base case
    else:
        return n + backward_sum(n - 1)  # Recursive call

# Test the function
result = backward_sum(5)
print("Sum of first 5 natural numbers using backward recursion:", result)
