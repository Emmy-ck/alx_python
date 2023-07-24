def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    fibonacci = [0, 1]
    while len(fibonacci) < n:
        num2 = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(num2)
        
    return(fibonacci)