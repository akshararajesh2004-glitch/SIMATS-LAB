def forward_sum(n, accum=0):
    if n == 0:
        return accum  # Base case returns accumulated sum
    else:
        return forward_sum(n - 1, accum + n)  # Recursive call first, accumulate sum

# Test the function
result = forward_sum(5)
print("Sum of first 5 natural numbers using forward recursion:", result)
